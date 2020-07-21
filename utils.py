import os
import base64
import hashlib
import secrets

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

class MissingLibraryError (Exception):
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

def make_aes_iv (): return secrets.token_bytes (16) # 16 byte IV according to https://www.pycryptodome.org/en/latest/src/cipher/aes.html

# thanks https://docs.python.org/3/library/stdtypes.html#int.to_bytes
def int_to_bytes (_int): return _int.to_bytes((_int.bit_length() + 7) // 8, byteorder='little')
def bytes_to_int (_bytes): return int.from_bytes (_bytes, byteorder = "little")
