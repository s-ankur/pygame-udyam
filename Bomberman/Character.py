

__author__ = 'AnkuR'
from Classes import automatic, HealthBar,Selector
from Bases import Draw, Sound,Solid, Mortal
from Shared import commands
from Bomberman.Weapons import BombDrop
from Managers import Event

class Character(Mortal, Solid):
    playable = True

    target = None
    player = None

    health = 100
    speed = 5

    def register(self):
        super().register()
        self.weapon = self.Weapon(self)  # \\
        self.healthbar=HealthBar(self)


    def deregister(self):
        super().deregister()
        if self.player:
            self.player.deregister()
        self.weapon.deregister()  # whatever  I create , i must destroy
        self.weapon=None
        self.healthbar.deregister()  # whatever  I create , i must destroy
        self.healthbar=None  # whatever  I create , i must destroy

    def shift(self):
        pass


    def kill(self):
        super().kill()
        self.kill_sound.play() # meow
        s=lambda :Event.handler.remove(s) and False
        Event.handler.append(s)

    def primary_fire(self):
        self.weapon.fire_weapon()

    def secondary_fire(self):
        self.weapon.fire()


class Bomber(Character):
    image = Draw.load('3.bmp',colorkey=(255,0,0))
    kill_sound = Sound('meow.ogg')
    Weapon = BombDrop

class Box(Mortal,Solid):
    show_log = False
    image=Draw.load('5.bmp')
    health=20


class Brick (Solid):
    show_log = False
    image=Draw.load('5.bmp')


commands['bomber']=Bomber
