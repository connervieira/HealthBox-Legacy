import os
import base64
import hashlib
import secrets
import uuid

def clear (): # Function to clear the screen
	if os.name == "nt": # Use 'cls' command if host is Windows
		os.system ("cls")
	else: # Use 'clear' command if host is Mac os Linux
		os.system ("clear")

class color: # Define various text styling elements
    WHITE = '\033[37m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

class MissingLibraryError (Exception): # An error to be raised when a library isn't installed
	# functionality should be a short description of what the library is used for
	# library should be the name of the library as installed through pip
	def __init__ (self, functionality, library):
		self.functionality = functionality
		self.library = library
		super ().__init__ (f"Missing library {library} for {functionality}, try 'pip install {library}'")

def base64_encode (*args, text_encoding = "utf-8"): # base64-encodes all byte arguments and returns the result as a tuple of strings
    return tuple (map (lambda byte_data: base64.b64encode (byte_data).decode (text_encoding), args))

def base64_decode (*args, text_encoding = "utf-8"): # base64-decodes all string arguments and returns the result as a tuple of bytes
    return tuple (map (lambda string_data: base64.b64decode (string_data.encode (text_encoding)), args))

# Hashes a string with a given hash method and encoding and returns the result and salt as bytes
# If a salt is passed, the salt is appended to the end of the string;
# otherwise, a new salt is generated
def hash_string (string, salt = None, hash_method = "sha256", text_encoding = "utf-8"):
	if salt is None: salt = secrets.token_bytes ()
	string_data = string.encode (text_encoding) + salt
	return getattr (hashlib, hash_method) (string_data).digest (), salt

def make_aes_iv (): return secrets.token_bytes (16) # Generates an IV for AES-CBC, which should be 16 bytes long, according to https://www.pycryptodome.org/en/latest/src/cipher/aes.html

# thanks https://docs.python.org/3/library/stdtypes.html#int.to_bytes
def int_to_bytes (_int): return _int.to_bytes((_int.bit_length() + 7) // 8, byteorder='little')
def bytes_to_int (_bytes): return int.from_bytes (_bytes, byteorder = "little")

def _generate_id (): return uuid.uuid4 ().hex # A simple method to generate an identifier like "1b081f8468fd45deb8fa63e98de2481e"

def generate_id (*, existing_ids = []): # A more complicated method that generates an ID and makes sure it isn't present in the passed list of existing IDs
	first = True
	id = uuid.uuid4 ().hex
	while first or id in existing_ids:
		id = uuid.uuid4 ().hex
		first = False
	return id

def parse_command (command):
	split_command = command.split (" ")
	command_name, command_argument = split_command [0].lower (), " ".join (split_command [1:])
	return command_name, command_argument

def pause_with_message (message):
	print (message)
	input ("Press enter to continue")

def print_red_if_false (message, condition, **kwargs): # Prints the given message in red if the given condition is false, preserving any keyword arguments in the call to print
	if condition:
		print (message, **kwargs)
	else:
		print (f"{color.RED}{message}{color.END}", **kwargs)

# Resolves a string to its actual value if it's an alias based on the targets_with_aliases argument
# The argument source is the string to be resolved
# The argument targets_with_aliases is a list of lists, where the first entry in each list is the preferred value of the string and each other entry is an alias
# The argument lower is a bool indicating whether or not the source should be set to lower case before it's processed.
# The return values are success (bool), resolved_str (str or None)
def resolve_aliases (source, targets_with_aliases, lower = True):
	if lower: source = source.lower ()
	for target_with_aliases in targets_with_aliases:
		if source in target_with_aliases:
			return True, target_with_aliases [0]
	return False, None

# Opens a menu, allowing the user to edit a list of items.
# The argument top_printout is a string that's shown at the top of the menu, intended to show options for the list of items.
# The argument source_list is the original contents of the list to be edited.
# The argument validator_func is a function that's called on each item to make sure it fits the intended format of the list.
# The keyword argument list_to_string_func is a function that's called on the list of items to transform it into a printable string.
# The argument input_transform is a function that gets called on typed items prior to being processed.
# The return value is edited_list (list).
def open_list_editor (top_printout, source_list, validator_func, list_to_string_func = lambda _list: ", ".join (_list), input_transform = lambda _input: _input.lower ()):
	edited_list = source_list.copy () # Avoid editing the source list in place.
	while True:
		clear ()
		print (top_printout)
		print ("")
		print (f"List contents: {list_to_string_func (edited_list)}")
		print ("Enter a list item to add or remove it, or type 'q' to quit.")
		target_item = input ("Enter the item: ")
		if target_item.lower () == "q": break
		target_item = input_transform (target_item)
		if not validator_func (target_item):
			pause_with_message ("Invalid item!")
			continue
		if target_item in edited_list:
			edited_list.remove (target_item)
		else:
			edited_list.append (target_item)
	return edited_list
