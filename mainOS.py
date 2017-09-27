from mainCore import PersonalOS
from menu import Menu
from about import About
from network import Network
import queue
from commonFunctions import *
from notes import Notes

if __name__ == '__main__':
    clearScreen()
    printOSinfo()
    input()
    clearScreen()
    sysInfo = open('sources/info.sysdat').read()
    coreObject = PersonalOS(None, None)
    mainMenu = Menu()
    network = Network()
    networkData = queue.Queue()
    networkStatus = queue.Queue()
    networkStatus = network.connectionStatus
    network.checkSpeed(networkData)
    emptyRetunObject = queue.Queue()
    exitSignal = True
    while exitSignal:
        clearScreen()
        coreObject.addThread(clearScreen())
        menuChoice = queue.Queue()
        coreObject.addThread(printMainMenuHeader(networkStatus, networkData, networkData.get()))
        coreObject.addThread(mainMenu.mainMenu(menuChoice))
        menuChoice, menuSize = menuChoice.get()
        menuChoice = int(menuChoice)
        if menuChoice == menuSize:      #   exit
            exitSignal = False
            clearScreen()
            printOSinfo()
                # About
        if menuChoice == 1:
            clearScreen()
            aboutMenuChoice = queue.Queue()
            coreObject.addThread(mainMenu.aboutMenu(aboutMenuChoice))
            aboutMenuChoice, exitChoice = aboutMenuChoice.get()
            if aboutMenuChoice == exitChoice:
                pass
            osInfo = About()
            aboutMenuChoice = int(aboutMenuChoice)
            if aboutMenuChoice == 2:
                clearScreen()
                contactsInfo = queue.Queue()
                coreObject.addThread(osInfo.getDeveloperContacts(contactsInfo))
                contactsInfo = contactsInfo.get()
                print(contactsInfo)
                input()
            if aboutMenuChoice == 3:
                clearScreen()
                featuresInfo = queue.Queue()
                coreObject.addThread(osInfo.getComingFeatures(featuresInfo))
                featuresInfo = featuresInfo.get()
                print(featuresInfo)
                input()
            if aboutMenuChoice == 1:
                clearScreen()
                patchInfo = queue.Queue()
                coreObject.addThread(osInfo.getPatchInfo(patchInfo))
                patchInfo = patchInfo.get()
                print(patchInfo)
                input()

            # Organiser
                # Organiser
        if menuChoice == 2:
            organiserExit = False
            while not organiserExit:
                clearScreen()
                organiserMenuChoice = queue.Queue()
                coreObject.addThread(mainMenu.organiserMenu(organiserMenuChoice))
                organiserMenuChoice, exitChoice = organiserMenuChoice.get()
                if organiserMenuChoice == exitChoice:   # Exit
                    organiserExit = True
                if organiserMenuChoice == 1:     # calendar
                    pass
                if organiserMenuChoice == 2:      # Notes
                    clearScreen()
                    notesExit = False
                    while not notesExit:
                        notesMenuChoice = queue.Queue()
                        coreObject.addThread(mainMenu.notesMenu(notesMenuChoice))
                        notes = Notes()
                        notesMenuChoice, notesExitChoice = notesMenuChoice.get()
                        if notesMenuChoice == notesExitChoice:
                            notesExit = True
                        if notesMenuChoice == 1:    # notesList
                            clearScreen()
                            iter = 1
                            notesTitles = notes.getNotesTitle()
                            for i in notesTitles:
                                print(iter, i)
                                iter += 1
                            noteNumber = int(input('Input note number'))
                            clearScreen()
                            print(notes.getNoteTextByTitle(notesTitles[noteNumber-1]))
                            input()
                            clearScreen()
                        if notesMenuChoice == 2:    # addNote
                            clearScreen()
                            noteTitle = input('Input note Title: ')
                            noteText = input('Input note text: ')
                            try:
                                notes.addNote(noteTitle, noteText)
                                print('Added!')
                                input()
                                clearScreen()
                            except Exception as e:
                                print('Error')
                                print('Try again later')
                                input()
                                clearScreen()
                # Mail Client
        if menuChoice == 3:
            pass










