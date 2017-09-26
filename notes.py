import calendar, datetime, time, random
class Notes:

    def __init__(self, username='test'):
        self.filePath = 'sources/users/'+username+'/'+'notes.dat'
        self.notesFile = open(self.filePath)
        self.fileData = self.notesFile.read()
        notes = self.fileData.split(';')
        self.notes = {}
        for i in notes:
            key, text = i.split(':')
            self.notes[key] = text
        sorted(self.notes.keys())

    def getNotesTitle(self):
        return list(self.notes.keys())

    def getNoteTextByTitle(self, title):
        for i in self.notes.keys():
            if i == title:
                return self.notes[i]

    def addNote(self, title, text):
        self.notesFile = open(self.filePath, 'a')
        self.notesFile.write(';'+title+':'+text)
        self.notesFile = open(self.filePath)
        self.fileData = self.notesFile.read()
        notes = self.fileData.split(';')
        self.notes = {}
        for i in notes:
            key, text = i.split(':')
            self.notes[key] = text





