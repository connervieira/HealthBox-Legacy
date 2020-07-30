# This file provides classes with methods to parse route URLs (e.g. "/api/v2/<string:api_endpoint>"),
# check URLs (e.g. "/api/v2/test") against those parsed route URLs,
# and extract URL variables (e.g. "test") from a URL that matches a route URL.
# It isn't perfect but it covers most basic use cases, with only one known badly handled edge case, which is documented here.

# KNOWN ISSUE: This route URL and URL pair still fails to match, while Flask/Werkzeug handles it """fine""". (The parser doesn't fail, that is.)
# See the TODO about "iterative backtracking".
# It shouldn't matter anyway; having multiple variables directly adjacent is an edge case that shouldn't exist in practice.
# There isn't any logical reason to have multiple integers next to each other without a separator; even if they are parsed to be valid,
# the developer has no way of knowing where the separator between the integers was supposed to go.
# route_url = "/front_segment/<string:front_string>/<string:string_with_ints><int:int_one><int:int_two>/<path:middle_path>/middle_segment/<string:last_variable>"
# url = "/front_segment/front_string/test420/middle/path/here/middle_segment/last_variable_value"

import re, string, copy

class InternalParsingError (Exception): pass # This error should only be thrown if there's an issue with the internal URL parsing

class RouteURLParser:
    @staticmethod
    def _generate_regex_for_variable_specifier_type (*, variable_specifier_type):
        if "default" not in variable_specifier_type:
            default = False
        else:
            default = variable_specifier_type ["default"]
        type_name = variable_specifier_type ["type_name"]
        # Returns a regular expression that matches instances of <TYPE:NAME>
        # where TYPE == type_string and NAME is an alphanumeric variable name.
        # If default is set, <NAME> will also be matched by the regex.
        return f"<{type_name}:[^.<>:]+>{'|<[^.<>:]+>' if default else ''}"
    variable_specifier_types = [
        {"type_name": "string", "default": True}, # "default" defaults to False
        {"type_name": "int"}, # "default" is not specified since it defaults to False
        {"type_name": "float"},
        {"type_name": "path"},
        # {"type_name": "uuid"} UUID parsing is disabled due to the added complexity of having a required string length.
    ]
    @staticmethod
    def _get_name_from_variable_specifier_string (*, variable_specifier_string):
        # Argument variable_specifier_string should follow the format <TYPE:NAME> or <NAME>
        # The return value is NAME
        def raise_error (*, reason): raise InternalParsingError (f"Bad variable specifier string {variable_specifier_string}, reason: {reason}")
        if not (variable_specifier_string.startswith ('<') and variable_specifier_string.endswith ('>')):
            raise_error (reason = "missing < and/or >")
        inner_string_part = variable_specifier_string [1:-1] # Removes <> (<TYPE:NAME> --> TYPE:NAME)
        type_and_name_or_name = tuple (inner_string_part.split (':'))
        if not (len (type_and_name_or_name) == 1 or len (type_and_name_or_name) == 2):
            raise_error (reason = "string doesn't follow NAME or TYPE:NAME format")
        if len (type_and_name_or_name) == 2: # ("TYPE", "NAME")
            _type, name = type_and_name_or_name # Expands ("TYPE", "NAME") into _type = "TYPE", name = "NAME"
        else: # ("NAME")
            name = type_and_name_or_name # Expands ("NAME") into name = "NAME"
        return name
    @staticmethod
    def _find_variable_specifiers (*, route_url):
        all_matches = []
        for variable_specifier_type in RouteURLParser.variable_specifier_types:
            regex = RouteURLParser._generate_regex_for_variable_specifier_type (variable_specifier_type = variable_specifier_type)
            matches = list (re.finditer (regex, route_url))
            all_matches += list ({
                "type_name": variable_specifier_type ["type_name"],
                "variable_name": RouteURLParser._get_name_from_variable_specifier_string (
                    variable_specifier_string = match.group ()
                ),
                "re_match": match
            } for match in matches)
        return all_matches
    @staticmethod
    def _segment_route_url_based_on_variable_specifiers (*, route_url, variable_specifiers):
        segments = []
        route_url_position = 0
        # To make sure the target string is parsed from start to end,
        # first the list of variable specifiers is sorted by the lower boundary of each specifier.
        variable_specifiers = sorted (variable_specifiers, key = lambda type_specifier: type_specifier ["re_match"].span () [0])
        for variable_specifier in variable_specifiers:
            string_segment = ""
            lower_boundary = variable_specifier ["re_match"].span () [0]
            while route_url_position < lower_boundary: # While our position in the route URL hasn't caught up to the lower boundary of this variable specifier,
                string_segment += route_url [route_url_position:route_url_position + 1]
                route_url_position += 1
            if string_segment != "": segments.append ({"type": "string", "string": string_segment})
            segments.append ({"type": "variable_specifier", "variable_type": variable_specifier ["type_name"], "variable_name": variable_specifier ["variable_name"]})
            route_url_position = variable_specifier ["re_match"].span () [1]
        if route_url_position <= len (route_url) - 1: # Check if there's a string part after the last variable specifier.
            segments.append ({"type": "string", "string": route_url [route_url_position:]}) # Add this final string part to the list of segments.
        return segments
    @staticmethod
    def parse_route_url (*, route_url):
        # Generate a list of segments -- both strings and variable specifiers --
        # that a URL has to have to match the route URL.
        variable_specifiers = RouteURLParser._find_variable_specifiers (route_url = route_url)
        segments = RouteURLParser._segment_route_url_based_on_variable_specifiers (route_url = route_url, variable_specifiers = variable_specifiers)
        return segments
    def _generate_pretty_segment_printout (*, segments, string_color = "BLUE", variable_specifier_color = "GREEN"): # WARNING: needs Color from utils.py
        from utils import color # utils.py
        out = ""
        print_without_newline = lambda variable: print (variable, end = "")
        for segment in segments:
            if segment ["type"] == "string":
                out += f"{getattr (color, string_color)}{segment ['string']}{color.END}"
            elif segment ["type"] == "variable_specifier":
                out += f"{getattr (color, variable_specifier_color)}<{segment ['variable_type']}:{segment ['variable_name']}>{color.END}"
        return out

class URLVariableValidator: # This class is used internally by URLMatcher. The inclusion of a "yieldable character check" in each validator is superfluous and will be cleaned up in the future.
    @staticmethod
    def validate_url_variable (*, url_variable, _type): # Offloads the validation of the URL variable to another function based on its type
        if _type not in URLVariableValidator.validators.keys ():
            raise InternalParsingError (f"Validation of URL variable type {_type} is unimplemented")
        return URLVariableValidator.validators [_type] (url_variable = url_variable)
    @staticmethod
    def string_validator (*, url_variable, _skip_yieldable_character_check = False):
        if len (url_variable) == 0: return False if _skip_yieldable_character_check else (False, False)
        is_valid = True
        for character in url_variable:
            # if character not in string.ascii_letters + string.digits:
            if character == '/': # "accepts any text without a slash" from https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
                is_valid = False
        if _skip_yieldable_character_check:
            return is_valid
        else:
            can_yield_character = URLVariableValidator.string_validator (
                url_variable = url_variable [:-1], _skip_yieldable_character_check = True
            )
            return is_valid, is_valid and can_yield_character
    @staticmethod
    def int_validator (*, url_variable, _skip_yieldable_character_check = False):
        if len (url_variable) == 0: return False if _skip_yieldable_character_check else (False, False)
        is_valid = True
        for character in url_variable:
            if character not in string.digits:
                is_valid = False
        if _skip_yieldable_character_check:
            return is_valid
        else:
            can_yield_character = URLVariableValidator.int_validator (
                url_variable = url_variable [:-1], _skip_yieldable_character_check = True
            )
            return is_valid, is_valid and can_yield_character
    @staticmethod
    def float_validator (*, url_variable, _skip_yieldable_character_check = False):
        if len (url_variable) == 0: return False if _skip_yieldable_character_check else (False, False)
        if url_variable.count ('.') != 1: return False, False
        left_side, right_side = tuple (url_variable.split ('.'))
        left_side_valid = URLVariableValidator.int_validator (url_variable = left_side, _skip_yieldable_character_check = True)
        if _skip_yieldable_character_check:
            right_side_valid = URLVariableValidator.int_validator (url_variable = right_side, _skip_yieldable_character_check = True)
            return left_side_valid and right_side_valid
        else:
            right_side_valid, right_side_can_yield_character = URLVariableValidator.int_validator (url_variable = right_side)
            return left_side_valid and right_side_valid, left_side_valid and right_side_valid and right_side_can_yield_character
    @staticmethod
    def path_validator (*, url_variable, _skip_yieldable_character_check = False):
        if len (url_variable) == 0: return False if _skip_yieldable_character_check else (False, False)
        is_valid = True
        # From https://flask.palletsprojects.com/en/1.1.x/quickstart/#variable-rules
        # string: "accepts any text without a slash"
        # path: like string but also accepts slashes
        # Because of this, we don't need to check anything except the length
        # and then just return True in the correct format based on whether or not we're skipping the character check
        # (Also, we can't yield a character if there's only one character in the path)
        return True if _skip_yieldable_character_check else (True, len (url_variable) == 1)
    validators = { # These have to be defined using __func__ to access the function part of the static methods: see https://stackoverflow.com/a/41921291/5037905
        "string": string_validator.__func__,
        "int": int_validator.__func__,
        "float": float_validator.__func__,
        "path": path_validator.__func__
    }

class URLMatcher:
    @staticmethod
    def check_url_against_parsed_route_url (*, url, parsed_route_url):
        # TODO: Clean up this function... there are lots of dead debug print statements left over. (Eric will take care of this eventually)

        # Note: parsed_route_url is a friendlier name for a list of route URL segments,
        # referred to with the "segments" variable in the RouteURLParser class.
        # In other words, parsed_route_url is analogous to segments.
        parsing_url = copy.deepcopy (url) # Make sure we don't modify the original url passed

        url_variables = {}
        route_url_segment_number = 0
        selection_start = 0
        while route_url_segment_number < len (parsed_route_url):
            # print ("### START OF SEGMENT ITERATION")
            # print (f"### URL VARIABLES: {url_variables}")
            # print (f"### SELECTION PROGRESS: {selection_start}/{len (parsing_url)}")
            # print (f"### REMAINING SELECTION: {parsing_url [selection_start :]}")
            # print (f"### SEGMENT NUMBER: {route_url_segment_number + 1}/{len (parsed_route_url)}")
            current_segment = parsed_route_url [route_url_segment_number]
            # print (current_segment)
            if current_segment ["type"] == "string":
                if parsing_url [selection_start :].startswith (current_segment ["string"]):
                    # print (f"{current_segment ['string']} matches")
                    selection_start += len (current_segment ["string"])
                else:
                    # print (f"{current_segment ['string']} doesn't match")
                    # Get the last segment and check if it's a variable that can yield a character to attempt to make this string match
                    if route_url_segment_number == 0:
                        # This is the first segment and it doesn't match, so the URL doesn't match.
                        return False, None
                    last_segment = parsed_route_url [route_url_segment_number - 1]
                    if last_segment ["type"] != "variable_specifier":
                        # This variable doesn't match and the last segment isn't a variable, so the URL doesn't match.
                        return False, None
                    last_variable = url_variables [last_segment ["variable_name"]]
                    # Check if the last variable contains this string
                    last_variable_index_of_string = last_variable ["value"].find (current_segment ["string"])
                    if last_variable_index_of_string < 0:
                        # The last variable doesn't contain this string. Parsing has failed.
                        return False, None
                    # print ("IT CONTAINS US")
                    # Check the validity of the last variable without this string (and everything after it)
                    sliced_last_variable_value = last_variable ["value"] [: last_variable_index_of_string]
                    # print (sliced_last_variable_value)
                    sliced_last_variable_is_valid = URLVariableValidator.validate_url_variable (
                        _type = last_variable ["type"],
                        url_variable = sliced_last_variable_value
                    ) [0]
                    if not sliced_last_variable_is_valid:
                        # print ("ok we dont got this -- sliced last variable isn't valid")
                        return False, None
                    # print ("THE SLICE IS VALID WE DID IT???")
                    backtrack_amount = len (last_variable ["value"]) - last_variable_index_of_string # The amount we have to move back to line up with the end of the sliced part of the last variable
                    # print (f"Backtracking by {backtrack_amount}")
                    forward_amount = len (current_segment ["string"]) # The amount we have to move forward after finding the current string
                    # print (f"Forward tracking by {forward_amount}")
                    last_variable ["value"] = sliced_last_variable_value # Patch the value of the last variable
                    selection_start -= backtrack_amount
                    selection_start += forward_amount
            elif current_segment ["type"] == "variable_specifier":
                selection_size = 0
                current_selection_matches = True
                finished = False
                while current_selection_matches and not finished:
                    selection_size += 1
                    # print (f"selection size is now {selection_size}")
                    selection = parsing_url [selection_start : (selection_start + selection_size)]
                    # print (f"current selection is {selection}")
                    if selection_size > 1: last_selection_can_yield_character = copy.deepcopy (selection_can_yield_character)
                    current_selection_matches, selection_can_yield_character = URLVariableValidator.validate_url_variable (
                        _type = current_segment ["variable_type"],
                        url_variable = selection
                    )
                    if current_selection_matches:
                        # print (f"iteration: {selection} matches variable {current_segment ['variable_name']} (length: {len (selection)})")
                        # Check if the next iteration will reach the end of the parsing URL
                        if (selection_start + selection_size + 1) > len (parsing_url):
                            # print ("breaking now")
                            url_variables [current_segment ["variable_name"]] = {"type": current_segment ['variable_type'], "value": selection, "can_yield_character": selection_can_yield_character}
                            finished = True
                            selection_start += len (selection)
                    else:
                        selection_size -= 1
                        # print ("Subtracting from selection size")
                        if selection_size > 0:
                            # The attempt to add another character to the selection failed, but the current selection constitutes as a variable,
                            # so just save this selection as a match for the current variable,
                            # and move onto parsing the next segment.
                            selection = parsing_url [selection_start : selection_start + selection_size]
                            # print (f"finished: {selection} matches variable {current_segment ['variable_name']}")
                            url_variables [current_segment ["variable_name"]] = {"type": current_segment ["variable_type"], "value": selection, "can_yield_character": last_selection_can_yield_character}
                            finished = True
                            selection_start += len (selection)
                        else:
                            # The current selection is empty, so see if the last segment is a variable and can yield a character.
                            # print ("got here")
                            if route_url_segment_number == 0:
                                # This is the first segment and it doesn't match, so the URL doesn't match.
                                return False, None
                            last_segment = parsed_route_url [route_url_segment_number - 1]
                            if last_segment ["type"] != "variable_specifier":
                                # This variable doesn't match and the last segment isn't a variable, so the URL doesn't match.
                                return False, None
                            last_variable = url_variables [last_segment ["variable_name"]]
                            last_variable_can_yield_character = last_variable ["can_yield_character"]
                            # TODO: Add functionality to backtrack multiple variables ("iterative backtracking"), e.g. ["test42", "0", (int)] --> ["test4", "2", "0"]
                            if not last_variable_can_yield_character:
                                # print ("ok we dont got this -- last variable cant yield a character")
                                return False, None
                            # print ("WE GOT THIS")
                            last_variable ["value"] = last_variable ["value"] [:-1] # Slice off the last character, since it can be yielded
                            selection_start -= 1 # Move the selection back by one character
                            current_selection_matches = True # Allow another iteration
                            #
#                             if
#
                            # and then check if the result
                            # return False, None
            # print (f"{parsing_url [selection_start:]} left to parse")
            # print (f"(selection_start is now {selection_start})")
            route_url_segment_number += 1
        # print ("We did it???")
        # Make sure there isn't anything left at the end of the original string
        if selection_start < len (parsing_url):
            # print (f"selection_start: {selection_start}, len (parsing_url): {len (parsing_url)}")
            return False, None
        # Post-process URL variables according to their type
        post_processed_url_variables = {}
        for variable_name, variable_info in url_variables.items ():
            variable_value = None
            if variable_info ["type"] == "string":
                variable_value = variable_info ["value"]
            elif variable_info ["type"] == "int":
                variable_value = int (variable_info ["value"])
            elif variable_info ["type"] == "float":
                variable_value = float (variable_info ["value"])
            elif variable_info ["type"] == "path":
                variable_value = variable_info ["value"].split ('/')
            post_processed_url_variables [variable_name] = variable_value
        return True, post_processed_url_variables

if __name__ == "__main__": # Checks if the script was run from the command line
    # Since the script was run from the command line, run a test given a mode provided by the user
    mode = input ("Mode (r --> route URL parser, u --> URL variable validator, m --> URL matcher): ")
    if mode == "r":
        route_url = input ("Type a route URL to parse: ")
        segments = RouteURLParser.parse_route_url (route_url = route_url)
        print (RouteURLParser._generate_pretty_segment_printout (segments = segments))
        variable_specifier_list_string = "; ".join (f"type: {segment ['variable_type']}, name: {segment ['variable_name']}" for segment in segments if segment ["type"] == "variable_specifier")
        print (f"Variable specifiers: {variable_specifier_list_string}")
    elif mode == "u":
        _type = input ("Type (string/int/path/float): ")
        url_variable = input ("URL variable contents: ")
        is_valid, can_yield_character = URLVariableValidator.validate_url_variable (
            _type = _type,
            url_variable = url_variable
        )
        print (f"Is valid: {is_valid}, can yield character: {can_yield_character}")
    elif mode == "m":
        route_url = input ("Type a route URL to parse: ")
        print (f"Parsing route URL {route_url}")
        parsed_route_url = RouteURLParser.parse_route_url (route_url = route_url)
        url = input ("Type a URL to check against the route URL: ")
        print (f"Checking URL {url}")
        parse_success, parsed_variables = URLMatcher.check_url_against_parsed_route_url (url = url, parsed_route_url = parsed_route_url)
        print (f"Parse success: {parse_success}")
        if parse_success: print (f"Parsed variables: {parsed_variables}")
    else:
        print ("Invalid mode!")
