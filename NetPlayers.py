__author__ = 'AnkuR'

from Players import Player
from socket import *
import pickle
from Daemon import Daemon


class NetPlayerRec(Player):
    def __init__(self, playable,num):
        super().__init__(playable,num)
        self.out_queue,self.in_queue=NetPlayerRecDaemon().start()

    def __call__(self):
        if not self.in_queue.empty():
            data = self.in_queue.get()
            if type(data)==complex:
                self.played.move(data)
            elif data==bytes(1) :
                self.played.primary_fire()
            else :
                self.played.shift()
        return True

    def deregister(self):
        super().deregister()
        self.out_queue.put(None)


class NetPlayerRecDaemon(Daemon):

    def run(self):
        myHost = ''                             # '' = all available interfaces on host
        myPort = 50007                          # listen on a non-reserved port number
        sockobj = socket(AF_INET, SOCK_STREAM)
        sockobj.bind((myHost, myPort))     # make a TCP socket object
        sockobj.listen(1)

        connection, _ = sockobj.accept()
        while True:
            try:
                data = connection.recv(1024)
                data= pickle.loads(data)
                self.out_queue.put(data)
            except Exception:
                connection.kill()
                return


class NetPlayerSen:
    speed=4
    def __init__(self):
        myHost = 'localhost'
        myPort = 50007
        sockobj = socket(AF_INET, SOCK_STREAM)
        sockobj.connect((myHost, myPort))
        self.soc=sockobj

    def move(self,data):
        data=pickle.dumps(data)
        self.soc.send(data)

    def shift(self):
        self.move(bytes(1))

    def primary_fire(self):
        self.move(bytes(2))
