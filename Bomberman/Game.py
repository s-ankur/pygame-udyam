

__author__ = 'AnkuR'

import Engine
from Players import NetPlayerRec, LocalPlayer
from Bomberman.Character import Bomber,Box,Brick
from Helper import coords
from Bases import Sprite
Sprite.center=coords(0,0)
engine = Engine.Engine()

def main():
    spawn_1=60, 60
    spawn_2=350,350


    level=[]
    for i in range(11):
        level.append([])
        for j in range(11):
            tmp=0
            if i%2==0 and j%2==0 or i in(0,10) or j in (0,10):tmp=1
            elif  i%2==0 or j%2==0:tmp=2
            level[i].append(tmp)
    level[2][1]=level[1][2]=level[-2][-3]=level[-3][-2]=0

    for i,row in enumerate(level):
        for j,elem in enumerate(row):
            if elem==1:tmp=Brick
            elif elem == 2:tmp=Box
            else:continue
            tmp().pos=coords(i*37+19,j*37+19) # dark magick


    b = Bomber(pos=complex(*spawn_1))
    LocalPlayer(b,2)

    c = Bomber(pos=complex(*spawn_2))
    LocalPlayer(c,1)

    #NetPlayerRec(c,1)


    # from pprint import pprint
    # pprint(level)

while True:
    main()
    engine.run()
    engine.clear()
    #showscore()
