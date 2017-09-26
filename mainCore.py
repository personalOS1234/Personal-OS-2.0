import threading
import queue


class PersonalOS:
    threads = []

    def __init__(self, mainThread, threadName = 'unknown'):
        mainThread=threading.Thread(target=mainThread, name=threadName)
        self.threads.append(mainThread)
        mainThread.start()

    def addThread(self, threadFunction, threadName = 'unknown'):
        threadFunction = threading.Thread(target=threadFunction, name=threadName)
        self.threads.append(threadFunction)
        threadFunction.start()

    def printThreads(self):
        for i in self.threads:
            print(i.name)

    def clearThred(self):
        while True:
            for i in self.threads:
                pass
