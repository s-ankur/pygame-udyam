import pygame

__author__ = 'AnkuR'
from Engine import Playable, Absolute
import sprites


class Ephemeral(Playable,Absolute):
    def init_ephemeral(self,cooldown,pos):
        self.cooldown=cooldown
        self.init_absolute(pos)
        self.init_playable()

    def play(self):
        if self.cooldown==0:
            self.delete()
            self.del_ephemeral()
            return
        self.ephemeral()
        self.cooldown-=1

    def del_ephemeral(self):
        self.del_drawable()
        self.del_playable()

    def delete(self):
        pass

    def ephemeral(self):
        pass


class Explosion(Ephemeral):
    ex1 = pygame.image.load('_exp_1.bmp')
    ex1.set_colorkey((0,0,0))
    ex2 = pygame.image.load('_exp_2.bmp')
    ex2.set_colorkey((0,0,0))
    ex3= pygame.image.load('_exp_3.bmp')
    ex3.set_colorkey((0,0,0))

    def __init__(self,pos):
        self.image=self.ex1
        self.init_ephemeral(9,pos)

    def ephemeral(self):
        if self.cooldown==3:
            self.image=self.ex3
        elif self.cooldown ==5:
            self.image=self.ex2


