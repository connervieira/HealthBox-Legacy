import utils, metrics # utils.py, metrics.py

class HealthKitAPIKeyManagerTerminalWrapper:
    def __init__ (self, db):
        self.db = db
        self._manager = HealthKitAPIKeyManager (self.db)
    def api_key_management_menu (self):
        while True: # Loop until a valid command has been entered
            utils.clear ()
            # List all API keys
            print ("API keys: ")
            api_key_number = 1
            for api_key in self.db ["api_keys"]:
                print (f"#{api_key_number}:")
                print (f"Friendly name: {api_key ['friendly_name']}")
                print (f"Key: {api_key ['key']}")
                api_key_number += 1
                print ("")

            # Show a menu with actions to perform on the key list
            print ("Commands:")
            print ("c|create <friendly name>: Create a new API key with the specified friendly name")
            print ("e|edit <number>: Edit the friendly name or permissions for the key with the specified number")
            print ("d|delete <number>: Delete the key with the specified number")
            print ("l|log <number>: List usage details for the key with the specified number")
            print ("cl|clear-log <number>: Erase all log entries for the key with the specified number")
            print ("q: quit")

            command = input ("Enter your command with argument(s): ")
            command_name, command_argument = utils.parse_command (command)
            command_name_resolution_success, command_name = utils.resolve_aliases (command_name, [["create", "c"], ["edit", "e"], ["delete", "d"], ["log", "l"], ["clear-log", "cl"], ["quit", "q"]])
            if not command_name_resolution_success:
                utils.pause_with_message ("Invalid command!")
                continue

            if command_name in ["edit", "delete", "log", "clear-log"]: # These commands need an API key number as the argument.
                # To avoid duplicate code, the API key number is parsed here.
                api_key_number_parse_success, api_key = self._manager._parse_key_number_string (command_argument)
                if not api_key_number_parse_success:
                    utils.pause_with_message ("Invalid API key number!")
                    continue

            if command_name == "create":
                self._manager.create (friendly_name = command_argument)
            elif command_name == "edit":
                self.edit_api_key_menu (api_key)
            elif command_name == "delete":
                self._manager.delete (api_key = api_key)
            elif command_name == "log":
                for log_entry in self._manager.get_log_entries (api_key = api_key):
                    print (log_entry) # TODO: Improve this by adding parsing of the log entry dictionary
            elif command_name == "clear-log":
                self._manager.clear_log (api_key = api_key)
            elif command_name == "quit":
                break
    def edit_api_key_menu (self, api_key):
        while True:
            utils.clear ()
            print (f"Editing {api_key ['friendly_name']}")
            print (f"Key: {api_key ['key']}")
            print (f"Type: {api_key ['type']}")
            print (f"Security: {api_key ['security']}")
            print (f"Filter: {', '.join (api_key ['filter'])}")
            print ("")
            print ("Commands:")
            print ("n|name <friendly name>: Set the name of this API key")
            print ("t|type <s|source / a|app>: Set the type of the API key, where:")
            print ("  a|app: The key can be used to retrieve fitness data from HealthBox (default)")
            print ("  s|source: The key can be used to send fitness data to HealthBox")
            print ("  (You can customize the exact data that can be set and retrieved with the security)")
            print ("s|security <a|all / n|none / w|whitelist / b|blacklist>: Set the security mode of the API key, where:")
            print ("  a|all: Allow all requests to the API (default)")
            print ("  n|none: Allow no requests to the API")
            print ("  w|whitelist: Allow no requests to the API, except those that match a list of metric categories")
            print ("  b|blacklist: Allow all requests to the API, except those that match a list of metric categories")
            print ("f|filter: Open a menu to specify metrics and metric categories for the whitelist and blacklist security options (has no effect with security set to all or none)")
            print ("q|quit: quit")
            print ("")
            command = input ("Enter your command with argument(s): ")
            command_name, command_argument = utils.parse_command (command)
            command_name_resolution_success, command_name = utils.resolve_aliases (command_name, [["name", "n"], ["type", "t"], ["security", "s"], ["filter", "f"], ["quit", "q"]])
            if not command_name_resolution_success:
                utils.pause_with_message ("Invalid command!")
                continue
            if command_name == "name":
                self._manager.edit_friendly_name (api_key = api_key, friendly_name = command_argument)
            elif command_name == "type":
                resolution_success, resolved_type = utils.resolve_aliases (command_argument, [["app", "a"], ["source", "s"]])
                if not resolution_success:
                    utils.pause_with_message ("Invalid type!")
                    continue
                self._manager.set_type (api_key = api_key, type = resolved_type)
            elif command_name == "security":
                resolution_success, resolved_security = utils.resolve_aliases (command_argument, [["all", "a"], ["none", "n"], ["whitelist", "w"], ["blacklist", "b"]])
                if not resolution_success:
                    utils.pause_with_message ("Invalid security!")
                    continue
                self._manager.set_security (api_key = api_key, security = resolved_security)
            elif command_name == "filter":
                old_filter = self._manager.get_filter (api_key = api_key)
                new_filter = utils.open_list_editor (
                    metrics.generate_metric_printout (), # The text shown for the choices to add to the filter
                    old_filter, # The list prior to undergoing any edits by the user
                    metrics.verify_metric_id, # The function that gets called with user input to verify it's valid
                    input_transform = lambda _input: _input.upper () # The function that gets called on user input no matter what, used here to make sure 'A1' and 'a1' collide
                )
                if old_filter != new_filter: self._manager.set_filter (api_key = api_key, filter = new_filter)
            elif command_name == "quit":
                break

class InvalidIDError (Exception): pass

class HealthKitAPIKeyManager: # This object provides a simplistic API for creating and managing API keys.
    def __init__ (self, db):
        self.db = db
    def _get_key_from_actual_key (self, *, actual_key, allow_none = False): # Returns an api_key dictionary from the actual key, e.g. "8cfe6451b2204b7ea814857b1b0ce36a"
        for api_key in self.db ["api_keys"]:
            if api_key ["key"] == actual_key:
                return api_key
        if allow_none:
            return None
        else:
            raise InvalidIDError (id)
    def _get_list_of_actual_keys (self): return list (api_key ["key"] for api_key in self.db ["api_keys"])
    def _parse_key_number_string (self, key_number_string):
        # Returns success (bool), key (dict) or None
        try:
            api_key = self.db ["api_keys"] [int (key_number_string) - 1]
            return True, api_key
        except (ValueError, IndexError):
            return False, None
    def create (self, *, friendly_name):
        api_key = { # See the edit menu for a description of each of these key settings.
            "friendly_name": friendly_name,
            "key": utils.generate_id (existing_ids = self._get_list_of_actual_keys ()),
            "type": "app",
            "security": "all",
            "filter": [],
            "log_entries": []
        }
        self.db ["api_keys"].append (api_key)
        self.db.save ()
    def edit_friendly_name (self, *, api_key, friendly_name):
        api_key ["friendly_name"] = friendly_name
        self.db.save ()
    def set_type (self, *, api_key, type):
        api_key ["type"] = type
        self.db.save ()
    def set_security (self, *, api_key, security):
        api_key ["security"] = security
        self.db.save ()
    def delete (self, *, api_key):
        self.db ["api_keys"].remove (api_key)
        self.db.save ()
    def get_log_entries (self, *, api_key):
        return api_key ["log_entries"]
    def clear_log (self, *, api_key):
        api_key ["log_entries"] = []
        self.db.save ()
    def get_filter (self, *, api_key):
        return api_key ["filter"]
    def set_filter (self, *, api_key, filter):
        api_key ["filter"] = filter
        self.db.save ()
