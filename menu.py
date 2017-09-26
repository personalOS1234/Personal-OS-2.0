import queue , threading


class Menu():
    def __init__(self):
        sourceFile = open('sources/menu.dat')
        self.mainMenuData = sourceFile.read()
        self.mainMenuData = self.mainMenuData.split()
        self.sysInfo = open('sources/info.sysdat').read()
        self.aboutMenuData = None
        self.iter = 1
        self.organiserMenuData = None
        self.notesMenuData = None

    def mainMenu(self, returnObject):
        self.iter = 1
        print(self.sysInfo)
        for i in self.mainMenuData:
            print(self.iter, i)
            self.iter += 1
        choice = input('\n--------------------------------\nInput your choice: ')
        returnObject.put([choice, len(self.mainMenuData)])
        return

    def aboutMenu(self, returnObject):
        self.aboutMenuData = ['Patches', 'Contacts', 'Features', 'Exit']
        self.iter = 1
        for i in self.aboutMenuData:
            print(self.iter, i)
            self.iter += 1
        choice = input('\n--------------------------------\nInput your choice: ')
        returnObject.put([choice, len(self.aboutMenuData)])

    def organiserMenu(self, returnObject):
        self.organiserMenuData = ['Calendar', 'Notes', 'Exit']
        self.iter = 1
        for i in self.organiserMenuData:
            print(self.iter, i)
            self.iter += 1
        choice = input('\n--------------------------------\nInput your choice: ')
        choice = int(choice)
        returnObject.put([choice, len(self.organiserMenuData)])

    def notesMenu(self, returnObject):
        self.notesMenuData = ['Notes', 'Add note', 'Exit']
        self.iter = 1
        for i in self.notesMenuData:
            print(self.iter, i)
            self.iter += 1
        choice = input('\n--------------------------------\nInput your choice: ')
        returnObject.put([int(choice), len(self.notesMenuData)])
