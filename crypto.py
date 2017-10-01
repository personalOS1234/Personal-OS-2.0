from hashlib import sha256
from random import randint
from external import pyaes


def sha256_hash(text, salt=''):
        text += salt
        text = text.encode()
        text = sha256(text).digest()
        return text


def aes_encrypt(text, sha256_key):
        aes = pyaes.AESModeOfOperationCTR(sha256_key)  #setting key
        text = aes.encrypt(text)
        return text


def aes_decrypt(ciphertext, sha256_key):
        aes = pyaes.AESModeOfOperationCTR(sha256_key)  #setting key
        decrypted = aes.decrypt(ciphertext)
        return decrypted[:len(decrypted)]


def generate_salt (length):
        salt = []
        for i in range (length):
            salt.append(randint(255))
        return str(chr(salt[i]) for i in length)


'''
Authentication system concept:  
After creating new OS user, OS generates random salt.
OS stores hash(pass+salt) to check that password is correct.
Mail client generates its own salt for current user.
When attaching new mailbox, its password is encrypted with aes, 
using hash(OSUserPassword + CurrentUserMailSalt) as key.
When password is needed it decrypts with AES and same key.
'''