__author__ = 'AnkuR'
from Bases import Draw
warpimg=Draw.load('_warpimg.bmp')
menus=(Draw.load('_menu.bmp'),Draw.load('_instr.bmp'),Draw.load('_credits.bmp'))

ships=[]
planets=[]
for i in range(4):
    planets.append(Draw.load('_planet_'+str(i)+'.bmp'))
    ships.append(Draw.load('_ship_'+str(i)+'.bmp'))

