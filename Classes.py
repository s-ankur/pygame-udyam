__author__ = 'AnkuR'

from random import choice
from Helper import coords, pack
from Shared import commands, colors
from Bases import  Base, Mortal, Sprite, Owned
from Engine import Draw


class HealthBar(Owned, Base):
    drawable = True

    def draw(self):
        x = self.owner
        pos = x.absolute() - coords(*x.image.get_rect().center) - coords(0, 3)
        Draw.rectangle(colors['red'], pack(pos) + (x.health / 2, 3))


class Selector(Owned, Base):
    drawable = True

    selection=None

    def shift(self):
        ms = Mortal.mortals[:]
        ms.remove(self.owner)
        if self.selection in ms:
            ms.remove(self.selection)
        if ms:
            self.selection = choice(ms)
        else:
            self.selection = None


    def draw(self):
        if self.selection is not None and self.selection.alive:
            p = self.selection.absolute()
            c = coords(50, 50)
            Draw.rectangle(colors['red'], pack(p - c / 2) + (50, 50), 1)


class Explosion(Sprite):
    show_log = False

    ex1 = Draw.load('_exp_1.bmp',dir='./')
    ex1.set_colorkey((0,0,0))
    ex2 = Draw.load('_exp_2.bmp',dir='./')
    ex2.set_colorkey((0,0,0))
    ex3= Draw.load('_exp_3.bmp',dir='./')
    ex3.set_colorkey((0,0,0))

    image=ex1
    cooldown=10

    def draw(self):
        if self.cooldown == 0:
            self.deregister()
            return
        elif self.cooldown==3:
            self.image=self.ex3
        elif self.cooldown ==5:
            self.image=self.ex2
        self.cooldown-=1
        super().draw()