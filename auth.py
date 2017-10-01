import crypto
from commonFunctions import *

class Authorisation ():
    def __init__(self, user_data):
        self.user_data = user_data
        self.logged_in = False
        self.username = None

    def authorisate(self):
        while not self.logged_in:
            self.login()

    def login(self):
        self.user_info = None
        self.username = input ("Enter username:")
        if self.username == "reg" or self.username == "New user":
            self.newUser()
            return
        with open(self.user_data, 'r') as file:
            for line in file:
                if line[:len(self.username)] == self.username:
                    self.user_info = line
                    break
            if self.user_info is None:
                print("Wrong or unregistred username.",
                      "Type \"reg\" as username to register")
                return
            self.user_data = line.split()
            #structure: ||username salt hashed-password [master-key-salt]|| #TODO rework
            salt = self.user_data[1]
            hashed_password = self.user_data[2]
        while not self.logged_in:
            password = input("Enter password for ", self.username, ": ", sep='')
            if password.len() == 0:
                clearScreen()
                return
            elif crypto.sha256_hash(password, salt) == hashed_password:
                self.logged_in = True
                clearScreen()
                return
            else:
                print ("Wrong password. Try again. (Or leave it empty to return)")
        print ("Welcome, ", self.username, sep='')

    def newUser(self):
        self.username = None
        while self.username is None:
            self.username = input("Enter username to register (or empty to return): ")
            allowed = self.nameApprovment()
            if self.username.len() == 0:
                clearScreen()
                return
            elif not allowed:
                self.username = None
        self.salt = crypto.generate_salt(8)
        password = self.setPassword(self.salt)
        if password is None:
            clearScreen()
            return
        with open(self.user_data, 'a') as file:
            file.write(self.username + ' ' + self.salt + ' ' + password)
        clearScreen()

    def nameApprovment (self):
        if self.username is None or self.username.len() == 0:
            return False
        reserved = ["reg", "new_user"]
        if self.username in reserved:
            print ("Sorry, this name is reserved.")
            return False
        self.username = self.username.lower()
        for char in self.username:
            """_ PASSWORD RESTRICTIONS _"""
            if char.isspace() or not char.isprintable():
                print ("Sorry, the name contains characters that are not allowed.")
                return False
        return True

    def setPassword(self, salt):
        password = None
        while password is None:
            password = input("Enter password (up to 32 chars len). Or leave it empty to return.")
            if password.len() == 0:
                return
            elif password.len() > 32:
                print("Password is too long.")
                password = None
            else:
                password = crypto.sha256_hash(password, salt)
                return password

    def setMasterPassword(self):
        master_key_salt = crypto.generate_salt(8)
        self.user_data.append (master_key_salt)

    def setMasterKey(self, password):
        self.master_key = crypto.sha256_hash(password, self.user_data[3])
        return self.master_key

    def encryptWithKey (self, text):
        return crypto.aes_decrypt(text, self.master_key)

    def decryptWithKey(self, text):
        return crypto.aes_decrypt(text, self.master_key)