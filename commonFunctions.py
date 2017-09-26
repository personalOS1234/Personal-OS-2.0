import os,sys
import queue

def clearScreen():
    try:
        os.system('clear')
    except Exception as e:
        os.system('cls')
    return


def printOSinfo():
    sysInfo = open('sources/info.sysdat').read()
    print(sysInfo)
    return


def printMainMenuHeader(internetStatus, returnObject, internetDataDictionary):
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

