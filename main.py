__author__ = 'AnkuR'
from Menu import menuloop
from Engine import gameloop
from Ships import firsttime
import Engine
Engine.init()


while True:
    menuloop()
    firsttime()
    gameloop()
