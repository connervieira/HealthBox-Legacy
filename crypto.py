import traceback
# base64 used in test script at bottom
import secrets
import hashlib

import utils # utils.py

try:
    import Cryptodome.Cipher.AES as PyCryptodomeAESModule
except ModuleNotFoundError as error:
    if traceback.format_exception_only (ModuleNotFoundError, error) != ["ModuleNotFoundError: No module named 'Cryptodome'\n"]: # Make sure the error we're catching is the right one
        raise # If not, raise the error
    raise utils.MissingLibraryError ("decrypting and encrypting databases", "pycryptodomex")

# --- DEFINITION OF TERMS USED ---
# String key: the string used to create the encryption key (see encryption hash)
# Hash: a hash of the string key plus a salt (see encryption hash + storage hash)
# Hash method: the method used to hash the string key. The encryption hash method should return a 128-, 192-, or 256-bit hash for encryption usage. The storage hash method doesn't matter unless the serialized format length must be consistent.
# Encryption hash: a hash of the string key using a salt separate from the storage hash salt, used to encrypt data
# Storage hash: a hash of the string key using a salt separate from the encryption hash salt, serialized and used to check a string key against the originally used one
# IV: the "initialization vector" of the cryptographic function; should be saved next to the hash for future decryption operations
# Serialized format: a combination of the storage hash and IV, formatted as a string to be saved to a file or elsewhere, for future decryption operations
# Delimiter: the separator of the hash and IV in the serialized format, should not be part of the hex or base64 character sets
# Text encoding: the encoding format used to encode and decode the string key and base64 IV when hashing, serializing, or deserializing
# HashBasedCryptoData: a container for the encryption hash and its salt, the storage hash and its salt, and the IV
# HashBasedCryptoProvider: a static class that contains methods that use PyCryptodome and a HashBasedCryptoData instance to decrypt and encrypt data
# --- END TERM DEFINITIONS ---

class HashBasedCryptoDataBidirSerializer:
    @staticmethod
    def deserialize (serialized_format, delimiter = ':', text_encoding = "utf-8"):
        crypto_data = HashBasedCryptoData (from_code = True)
        crypto_data.apply_deserialized_data (*utils.base64_decode (
            *serialized_format.split (delimiter), \
            text_encoding = text_encoding
        ))
        return crypto_data
    @staticmethod
    def serialize (data, delimiter = ':', text_encoding = "utf-8"):
        return delimiter.join (utils.base64_encode (
            data.encryption_hash_salt, data.storage_hash, data.storage_hash_salt, data.iv, data.data_length, \
            text_encoding = text_encoding
        ))

class InvalidConstructorCall (Exception): pass
class InvalidKeyError (Exception): pass

class HashBasedCryptoData:
    def __init__ (self, from_code = False):
        if not from_code:
            raise InvalidConstructorCall ("Use HashBasedCryptoData.make_new or HashBasedCryptoData.use_existing")
    def serialize (*args, **kwargs): return HashBasedCryptoDataBidirSerializer.serialize (*args, **kwargs)
    @staticmethod
    def make_new (string_key, hash_method = "sha256", text_encoding = "utf-8"):
        encryption_hash, encryption_hash_salt = utils.hash_string (string_key, hash_method = hash_method, text_encoding = "utf-8")
        storage_hash, storage_hash_salt = utils.hash_string (string_key, hash_method = hash_method, text_encoding = "utf-8")
        iv = None
        data_length = -1
        crypto_data = HashBasedCryptoData (from_code = True)
        for data_part_name in ["encryption_hash", "encryption_hash_salt", "storage_hash", "storage_hash_salt", "iv", "data_length"]:
            setattr (crypto_data, data_part_name, locals () [data_part_name])
        crypto_data.iv_is_from_deserializer = False
        return crypto_data
    @staticmethod
    def use_existing (string_key, serialized_format, hash_method = "sha256", delimiter = ':', text_encoding = "utf-8"):
        crypto_data = HashBasedCryptoDataBidirSerializer.deserialize (serialized_format, delimiter = delimiter, text_encoding = text_encoding)
        crypto_data.check_string_key (string_key, hash_method = hash_method, text_encoding = text_encoding)
        # we now know that the given key is valid! generate the encryption hash using the given key and stored salt
        crypto_data.encryption_hash, _salt = utils.hash_string (string_key, salt = crypto_data.encryption_hash_salt, hash_method = hash_method, text_encoding = text_encoding)
        crypto_data.iv_is_from_deserializer = True # helps keep the programmer from accidentally overwriting the IV by deserializing and then calling encrypt before decrypt
        return crypto_data
    def check_string_key (self, string_key, hash_method = "sha256", text_encoding = "utf-8"):
        storage_hash_with_given_key, _storage_hash_salt = utils.hash_string (string_key, salt = self.storage_hash_salt, hash_method = hash_method, text_encoding = text_encoding)
        if storage_hash_with_given_key != self.storage_hash:
            raise InvalidKeyError (string_key)
    def apply_deserialized_data (self, encryption_hash_salt, storage_hash, storage_hash_salt, iv, data_length): # to be used by deserializer
        # the equivalent of doing self.encryption_hash_salt = encryption_hash_salt for all four arguments
        for data_part_name in ["encryption_hash_salt", "storage_hash", "storage_hash_salt", "iv", "data_length"]:
            setattr (self, data_part_name, locals () [data_part_name])

class HashBasedCryptoDataFileInteropProvider:
    @staticmethod
    def dump (crypto_data, file, *args, **kwargs):
        return file.write (crypto_data.serialize (*args, **kwargs))
    @staticmethod
    def load (file, string_key, **kwargs):
        return HashBasedCryptoData.use_existing (string_key, file.read (), **kwargs)
    @staticmethod
    def dumps (crypto_data, *args, **kwargs):
        return crypto_data.serialize (*args, **kwargs)
    @staticmethod
    def loads (crypto_data_string, string_key, **kwargs):
        return HashBasedCryptoData.use_existing (string_key, crypto_data_string, **kwargs)

class IVOverwriteAttemptError (Exception): pass

class HashBasedCryptoProvider:
    @staticmethod
    def encrypt (crypto_data, data_to_encrypt, force_new_iv = False):
        if crypto_data.iv_is_from_deserializer and not force_new_iv:
            raise IVOverwriteAttemptError ("This HashBasedCryptoData instance was initialized from the serialized format, but decrypt wasn't called before encrypt!\nSet force_new_iv to overwrite the IV if this is on purpose")
        crypto_data.iv = utils.make_aes_iv ()
        crypto_data.iv_is_from_deserializer = False
        crypto_data.data_length = utils.int_to_bytes (len (data_to_encrypt)) # data length must be a multiple of 16, so we store the true length of the data
        padded_data_to_encrypt = data_to_encrypt + (b"\x00" * (16 - (len (data_to_encrypt) % 16))) # and then pad it with zeroes before encrypting
        return PyCryptodomeAESModule.new (crypto_data.encryption_hash, PyCryptodomeAESModule.MODE_CBC, iv = crypto_data.iv).encrypt (padded_data_to_encrypt)
    @staticmethod
    def decrypt (crypto_data, data_to_decrypt):
        decrypted_data = PyCryptodomeAESModule.new (crypto_data.encryption_hash, PyCryptodomeAESModule.MODE_CBC, iv = crypto_data.iv).decrypt (data_to_decrypt)
        crypto_data.iv_is_from_deserializer = False # not exactly true... it's a bad variable name. but basically we assume that since the IV has been used once, it can be overwritten
        return decrypted_data [0:utils.bytes_to_int (crypto_data.data_length)] # remove the padding using the stored data length

if __name__ == "__main__": # Checking if this file was directly called from the command line
    # Testing crypto.py functionality:
    key = input ("Enter an initial key: ")
    original_data = input ("Enter the data to encrypt: ").encode ("utf-8")
    print (f"Key: {key}, original data: {original_data}")
    crypto_data = HashBasedCryptoData.make_new (key)
    encrypted_data = HashBasedCryptoProvider.encrypt (crypto_data, original_data)
    import base64
    print (f"Encrypted data: {base64.b64encode (encrypted_data).decode ('utf-8')}")
    serialized_format = crypto_data.serialize ()

    key = input ("Enter the original key: ")
    try:
        crypto_data = HashBasedCryptoData.use_existing (key, serialized_format)
    except InvalidKeyError:
        print ("Bad key detected")
        raise
    try:
        HashBasedCryptoProvider.encrypt (crypto_data, b"")
    except IVOverwriteAttemptError:
        print ("IV overwrite attempt detected successfully")
    decrypted_data = HashBasedCryptoProvider.decrypt (crypto_data, encrypted_data)
    print (f"Decrypted data: {decrypted_data}")
    try:
        assert decrypted_data == original_data, "Decrypted data doesn't match original data"
    except:
        print ("Something went wrong")
        raise
    print ("Tests succeeded")
