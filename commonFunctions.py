import os,sys
import queue

def clear_screen():
    try:
        os.system('cls')
    except Exception as e:
        os.system('cls')
    return


def printOSinfo():
    sysInfo = open('sources/info.sysdat').read()
    print(sysInfo)
    return


def print_main_menu_header(internetStatus, returnObject, internetDataDictionary):
    """
    :param internetStatus: True or False
    :param internetDataDictionary: {ping, downloadSpeed, uploadSpeed}
    :return: if no connection returns 'unknown' dictionary
    """
    returnDictionary={
        'ping': 'unknown',
        'downloadSpeed': 'unknown',
        'uploadSpeed': 'unknown'
                }
    if not internetStatus:
        returnObject.put(returnDictionary)
        print('Internet connection: ', internetStatus)
        print('ping: '+returnDictionary.get('ping'))
        return
    for i, j in zip(internetDataDictionary.values(), returnDictionary.keys()):
        returnDictionary[j] = i
    returnObject.put(returnDictionary)
    print('Internet connection: ', internetStatus)
    print('ping:', returnDictionary.get('ping'), '| Download speed: ', returnDictionary.get('downloadSpeed'))


def menu_initialization(coreObject, quequeObject, menuFunction):
    """
    :param coreObject: mainCore object to add thread
    :param quequeObject: object to return value
    :param menuFunction: function from MainMenu class
    :return: menuChoice, menuSize(exit menu value)
    """
    coreObject.addThread(menuFunction, quequeObject)
    menuChoice, menuSize = quequeObject.get()
    return int(menuChoice), menuSize


def check_input_no_enter_button(inputedChar):
    """
    :param inputedChar: char to check for no EnterBtn
    :return: not inputedChar == ''
    """
    return not inputedChar == ''
