from commonFunctions import *
import queue

class Authentication:
    def __init__(self):
        self.login = ''
        self.password = ''
        clear_screen()

    def login(self, returnObject):
        printOSinfo()
        self.login = input('Input login: ')
        self.password = input('Input password for '+self.login)

    def reg(self, returnObject):
