import queue

class About:
    def __init__(self):
        file = open('sources/about.txt')
        self.sysInfo = file.read()
        self.sysInfo = self.sysInfo.split('\/')

    def getPatchInfo(self, returnObject):
        returnObject.put(self.sysInfo[0])

    def getDeveloperContacts(self, returnObject):
        returnObject.put(self.sysInfo[1])

    def getComingFeatures(self, returnObject):
        returnObject.put(self.sysInfo[2])





