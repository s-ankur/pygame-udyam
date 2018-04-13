__author__ = 'AnkuR'
import Engine
Engine.init()
from Ships import firsttime
from Engine import gameloop
from Menu import menuloop


while True:
    menuloop()
    firsttime()
    gameloop()