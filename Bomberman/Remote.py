__author__ = 'AnkuR'
from Engine import Engine
from time import sleep
from Bases import Sprite,Draw
engine=Engine()

conn=Sprite()
conn.pos=complex(0,0)
i1=Draw.load(r'C:\Users\AnkuR\PycharmProjects\Engine\Bomberman\copen.bmp')
i2=Draw.load(r'C:\Users\AnkuR\PycharmProjects\Engine\Bomberman\cclos.bmp')

conn.image=i2

from Players import LocalPlayer,NetPlayerSen
running=True
while running:
    try:
        played=NetPlayerSen()
        conn.image=i1
        LocalPlayer(played)
        running=engine.run()
    except Exception as e:
        if e in (ConnectionResetError,ConnectionRefusedError):
            conn.image=i2
            sleep(1)
            continue