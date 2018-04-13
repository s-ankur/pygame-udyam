import random
import cmath

from Bases import Sprite, Draw,none
from Classes import Mortal,Selector, Explosion
from Space.Weapons import Microwave
from Space.Ai import EasyAI
import Space.sprites as sprites
from Shared import commands
from Managers import Event



class Planet(Mortal,Sprite):
    health =100
    target=none

class Ship(Mortal,Sprite):
    playable = True
    target=none
    player=None

    impulse = 0
    angle = 0

    speed = 4
    health=100

    def register(self):
        super().register()
        self.weapon=self.Weapon(self)

    def deregister(self):
        super().deregister()
        self.weapon.deregister()


    def kill(self):
        super().kill()
        Explosion(self.pos)


    def play(self):
        self.image = Draw.transform.rotate(self.sprite, -self.angle * 180 / 3.14)
        self.pos += cmath.rect(self.speed, self.angle) * self.impulse

    def fire(self):
        if self.target and self.target.alive:  # has target and its alive
            self.weapon.fire_weapon()
        else:
            self.target = none

class AiShip(Ship):
    AI=EasyAI


    def __init__(self, boss,Weapon):
        self.Weapon=Weapon
        self.ai=self.AI(self)
        self.boss=boss
        x=self.AI.patrol_dist
        r1 = random.randrange(-x, x)
        r2 = random.randrange(-x, x)
        pos = boss.pos + complex(r1, r2)
        super().__init__(pos)

    def play(self):
        self.ai.think()
        super().play()

class PlayerShip(Ship):
    sprite= sprites.ships[1]
    Weapon=Microwave

    def register(self):
        super().register()
        Sprite.focus=self
        self.selector=Selector(self)
        Event.handler.append(self.process_keys)


    def deregister(self):
        super().deregister()
        self.selector.deregister()
        Event.handler.remove(self.process_keys)

    def kill(self):
        super().kill()
        Event.handler.append(lambda :False)
        Event.resume=True

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

        if keys['tab']:
            self.selector.shift()

        if keys['down']:
            self.target=self.selector.selection
            self.fire()
        return True


class Team:
    def __init__(self,*args):
        self.team=list(args)

    def add(self,x):
        self.team.append(x)

    def register(self):
        for a in self.team:
            a.register()

commands['expl']=Explosion