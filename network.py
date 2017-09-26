import urllib3, socket, pyspeedtest, queue, math

class Network:
    def __init__(self):
        try:
            host = socket.gethostbyname('ya.ru')
            socket.create_connection((host, 80), 2)
            self.connectionStatus = True
        except:
            self.connectionStatus = False

    def checkSpeed(self, returnObject):
        """
        :param returnObject: queue object
        :return: returnList{ping, downloadSpeed, uploadSpeed}
        """
        if not self.connectionStatus:
            returnObject.put('no connection')
            return
        speedCheck=pyspeedtest.SpeedTest()
        ping = speedCheck.ping(server='ya.ru')
        downloadSpeed = speedCheck.download()
        uploadSpeed = speedCheck.upload()
        returnList = {
            'ping': math.ceil(ping),
            'downloadSpeed': math.ceil(downloadSpeed),
            'uploadSpeed': math.ceil(uploadSpeed)
        }
        returnObject.put(returnList)


