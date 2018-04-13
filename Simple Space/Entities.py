__author__ = 'AnkuR'
import cmath

from Engine.Shared import commands,Setables


Setables.scr_size=(400,200)
Setables.background_color=(0,0,0)

from Engine.Classes import Explosion,Owned
from Engine.Managers import Event
from Engine.Weapon import Weapon
from Engine.Helper import *
from Engine.Bases import Sprite,Draw ,Mortal

class Bullet( Sprite):
    playable = True
    show_log = False
    damage=50
    range=10
    cooldown=10
    speed=10
    image = Draw.load(r'_bullets_3.bmp', colorkey=(255, 255, 255))

    def __init__(self,pos,angle):
        super().__init__(pos)
        self.angle=angle

    def play(self):
        super().play()
        self.pos += cmath.rect(self.speed, self.angle)
        for ship in Ship.ships:
            if in_range(self,ship,self.range):
                ship.hurt(self.damage)
                self.deregister()
                return
        if self.cooldown==0:
            self.deregister()
        else:
            self.cooldown-=1

class Gun(Weapon):
    cooldown_max=10
    def fire(self):
        if self.cooldown<=0:
            Bullet(self.owner.pos+cmath.rect(10, self.owner.angle), self.owner.angle)
            self.cooldown=self.cooldown_max

class EasyAI(Owned):
     def think(self):
         pass

class Ship(Mortal,Sprite):

    playable = True

    ships=[]
    impulse = 0
    angle = 0

    speed =8
    health=100

    sprite=Draw.load('_ship_1.bmp')

    Weapon=Gun
    def register(self):
        super().register()
        Ship.ships.append(self)
        self.weapon=self.Weapon(self)

    def deregister(self):
        super().deregister()
        Ship.ships.remove(self)
        self.weapon.deregister()

    def kill(self):
        super().kill()
        Explosion(self.pos)

    def play(self):
        self.image = Draw.transform.rotate(self.sprite, -self.angle * 180 / 3.14)
        self.pos += cmath.rect(self.speed, self.angle) * self.impulse

    def fire(self):
        self.weapon.fire()

class AiShip(Ship):
    AI=EasyAI

    def register(self):
        super().register()
        self.ai=self.AI(self)

    def play(self):
        self.ai.think()
        super().play()

class PlayerShip(Ship):
    Weapon=Gun

    def register(self):
        super().register()
        Event.handler.append(self.process_keys)

    def deregister(self):
        Event.handler.remove(self.process_keys)
        super().deregister()
        Event.handler.append(lambda :False)


    def process_keys(self):
        keys = Event.keys
        self.angle += (keys['right']-keys['left'])*.2
        if keys['up']:
            self.impulse += .2
        else:
            self.impulse -= .01

        if self.impulse > .7:
            self.impulse = .7
        elif self.impulse < 0:
            self.impulse = 0

        if keys['m']:
            self.fire()
        return True
from random import randint

class Rock(Sprite):
    playable = True
    show_log = False
    range=35
    image=Draw.load('_exp_1.bmp',colorkey=(0,0,0))
    def register(self):
        self.timer=0
        super().register()
        self.speed=randint(4,8)

    def play(self):
        self.pos-= complex(self.speed,0)
        for ship in Ship.ships:
            if in_range(self,ship,self.range):
                ship.kill()
                self.deregister()
                return
        if self.timer*self.speed>600:
            self.deregister()
        self.timer+=1


class RockMaker:
    max_time=30
    def __init__(self):
        self.time=0
        Event.handler.append(self.make_rock)

    def make_rock(self):
        if self.time==0:
            Rock(pos=complex(300,randint(-100,100)))
            self.time=self.max_time
        self.time-=1
        return True



commands['aiship']=AiShip
commands['playership']=PlayerShip
commands['rock']=Rock