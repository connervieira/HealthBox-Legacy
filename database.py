import os.path
import copy
import json

import crypto # crypto.py

class JSONDatabaseBackend:
    def __init__ (self, *, db_file_name, default = None, encryption = False, crypto_data_file_name = None, string_key = None, encryption_text_encoding = "utf-8"):
        # move arguments into object scope
        # so we can access them from function calls
        self.db_file_name = db_file_name # path to the database file (.json)
        self.default = default # default value for the database if it doesn't exist, only used if create_if_nonexistent is True when calling load ()
        self.loaded = False # set to True after load () succeeds
        self._db = None # internal dictionary with the database contents. since the outer object passes most function calls to this inner object, it shouldn't need to be accessed directly
        self.encryption = encryption # boolean indicating whether or not encryption is enabled. shouldn't be modified after __init__
        # these three only matter if encryption is set to True
        self.crypto_data_file_name = crypto_data_file_name # path to the crypto data file associated with the database (.cryptodata)
        self.string_key = string_key # the string key used for encrypting and decrypting the database, can be changed between calls to load () and save ()
        self.encryption_text_encoding = encryption_text_encoding # text encoding used for calls to encryption functions and for encoding/decoding the JSON dictionary as a string
    def load (self, create_if_nonexistent = True):
        if not os.path.exists (self.db_file_name): # checks if db file exists
            if not create_if_nonexistent: # checks if were supposed to create it if not
                raise Exception ("Database file doesn't exist") # if not, throw error
            self._db = copy.deepcopy (self.default) # makes sure modifying self.default doesn't modify the database
            self.loaded = True
            self.save (_new = True)
        else:
            if not os.path.isfile (self.db_file_name):
                raise Exception ("Database file isn't a file?")
            if not self.encryption:
                with open (self.db_file_name, "r") as database_file:
                    self._db = json.load (database_file)
            else:
                with open (self.crypto_data_file_name, "r") as crypto_data_file:
                    self.crypto_data = crypto.HashBasedCryptoDataFileInteropProvider.load (crypto_data_file, self.string_key, text_encoding = self.encryption_text_encoding)
                with open (self.db_file_name, "rb") as database_file:
                    encrypted_db_dump = database_file.read ()
                binary_db_dump = crypto.HashBasedCryptoProvider.decrypt (self.crypto_data, encrypted_db_dump)
                self._db = json.loads (binary_db_dump.decode (self.encryption_text_encoding))
                self.save ()
            self.loaded = True
    def save (self, _new = False):
        assert self._db is not None, "Load the database first!"
        if self.encryption:
            string_key_has_changed = False
            if not _new:
                # Check if the string_key attribute has changed since the last time we saved
                try:
                    self.crypto_data.check_string_key (self.string_key, text_encoding = self.encryption_text_encoding)
                except crypto.InvalidKeyError:
                    # the string_key attribute has changed! regenerate crypto_data with the new key before saving
                    string_key_has_changed = True
            if _new or string_key_has_changed:
                self.crypto_data = crypto.HashBasedCryptoData.make_new (self.string_key, text_encoding = self.encryption_text_encoding)
        if not self.encryption:
            with open (self.db_file_name, f"w{'+' if _new else ''}") as database_file:
                json.dump (self._db, database_file)
        else:
            binary_db_dump = json.dumps (self._db).encode (self.encryption_text_encoding)
            encrypted_db_dump = crypto.HashBasedCryptoProvider.encrypt (self.crypto_data, binary_db_dump)
            with open (self.db_file_name, f"wb{'+' if _new else ''}") as database_file:
                database_file.write (encrypted_db_dump)
            with open (self.crypto_data_file_name, f"w{'+' if _new else ''}") as crypto_data_file:
                crypto.HashBasedCryptoDataFileInteropProvider.dump (self.crypto_data, crypto_data_file)

# these make it so you can call functions on this object
# and the function actually called is the one on the database object
# this also applies to "bruh" in object, object ["bruh"], object ["bruh"] = "lmao", and del object ["bruh"] expressions
# (thats what the __contains__, __getitem__, __setitem__, and __delitem__ functions get called for)
# I would assign these in a class function but the __ functions have to be set on the object prototype to work properly
# and it'd be a waste of resources to assign to the prototype in each instance

# Given the name of a function, this function creates a function that can be assigned to the object prototype
# to proxy the function with that name to the function with the same name on self._db
# jeez that's a long sentence... text me if this is unclear 4403840834
proxy_function_creator = lambda function_name: lambda self, *args, **kwargs: getattr (self._db, function_name) (*args, **kwargs)
# now we just iterate over each property
for func_name in ["__contains__", "__getitem__", "__setitem__", "__delitem__", "clear", "copy", "fromkeys", "get", "items", "keys", "pop", "popitem", "setdefault", "update", "values"]:
    setattr (JSONDatabaseBackend, func_name, proxy_function_creator (func_name))
