from mainCore import PersonalOS
from menu import Menu
from about import About
from network import Network
import queue
from commonFunctions import *
from notes import Notes


apiKey = "8f972ee3-83d3-4611-a888-9250825d0c90"

if __name__ == '__main__':
    clear_screen()
    printOSinfo()
    input()
    clear_screen()
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
        clear_screen()
        coreObject.addThread(clear_screen())
        queueObject = queue.Queue()
        coreObject.addThread(print_main_menu_header(networkStatus, networkData, networkData.get()))
        menuChoice, menuSize = menu_initialization(coreObject, queueObject, mainMenu.mainMenu(queueObject))
        if menuChoice == menuSize:      #   exit
            exitSignal = False
            clear_screen()
            printOSinfo()
            input()
                # About
        if menuChoice == 1:
            clear_screen()
            aboutMenuChoice = queue.Queue()
            aboutMenuChoice, exitChoice = menu_initialization(coreObject, aboutMenuChoice, mainMenu.aboutMenu(aboutMenuChoice))
            if aboutMenuChoice == exitChoice:
                pass
            osInfo = About()
            aboutMenuChoice = int(aboutMenuChoice)
            if aboutMenuChoice == 2:
                clear_screen()
                contactsInfo = queue.Queue()
                coreObject.addThread(osInfo.getDeveloperContacts(contactsInfo))
                contactsInfo = contactsInfo.get()
                print(contactsInfo)
                input()
            if aboutMenuChoice == 3:
                clear_screen()
                featuresInfo = queue.Queue()
                coreObject.addThread(osInfo.getComingFeatures(featuresInfo))
                featuresInfo = featuresInfo.get()
                print(featuresInfo)
                input()
            if aboutMenuChoice == 1:
                clear_screen()
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
                clear_screen()
                organiserMenuChoice = queue.Queue()
                organiserMenuChoice, exitChoice = menu_initialization(coreObject, organiserMenuChoice, mainMenu.organiserMenu(organiserMenuChoice   ))
                if organiserMenuChoice == exitChoice:   # Exit
                    organiserExit = True
                if organiserMenuChoice == 1:     # calendar
                    pass
                if organiserMenuChoice == 2:      # Notes
                    clear_screen()
                    notesExit = False
                    while not notesExit:
                        notesMenuChoice = queue.Queue()
                        coreObject.addThread(mainMenu.notesMenu(notesMenuChoice))
                        notes = Notes()
                        notesMenuChoice, notesExitChoice = notesMenuChoice.get()
                        if notesMenuChoice == notesExitChoice:
                            notesExit = True
                        if notesMenuChoice == 1:    # notesList
                            clear_screen()
                            iter = 1
                            notesTitles = notes.getNotesTitle()
                            for i in notesTitles:
                                print(iter, i)
                                iter += 1
                            noteNumber = int(input('Input note number'))
                            clear_screen()
                            print(notes.getNoteTextByTitle(notesTitles[noteNumber-1]))
                            input()
                            clear_screen()
                        if notesMenuChoice == 2:    # addNote
                            clear_screen()
                            noteTitle = input('Input note Title: ')
                            noteText = input('Input note text: ')
                            try:
                                notes.addNote(noteTitle, noteText)
                                print('Added!')
                                input()
                                clear_screen()
                            except Exception as e:
                                print('Error')
                                print('Try again later')
                                input()
                                clear_screen()
                # Mail Client
        if menuChoice == 3:
            pass










