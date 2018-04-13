__author__ = 'AnkuR'

import pygame,cmath
from Colors import *
from Helper import coords


class Playable:
    playables = []

    def __init__(self):
        self.init_playable()

    def init_playable(self):
        Playable.playables.append(self)

    def del_playable(self):
        if self in Playable.playables:
            Playable.playables.remove(self)

    @classmethod
    def play_all(cls):
        for played in cls.playables:
            played.play()

    def play(self):
        pass


class Drawable:
    drawables = []

    def __init__(self):
        self.init_drawable()

    def init_drawable(self):
        Drawable.drawables.append(self)

    def del_drawable(self):
        if self in Drawable.drawables:
            Drawable.drawables.remove(self)

    @classmethod
    def draw_all(cls):
        for i in cls.drawables:
            i.draw()
        pygame.display.update()  # updating the display for any changes on the screen
        screen.fill(black)

    def draw(self):
        pass


class Absolute(Drawable):
    focus = Drawable()
    focus.pos=coords((0,0))

    def __init__(self, pos):
        self.init_absolute(coords(pos))

    def init_absolute(self, pos):
        self.init_drawable()
        self.pos = pos

    def draw(self):
        sprite_center=coords(self.image.get_rect().center)
        pos = center + self.pos - self.focus.pos - sprite_center
        screen.blit(self.image, (pos.real, pos.imag))


class Moveable:
    def moveable(self):
        self.image = pygame.transform.rotate(self.sprite.sprite, -self.angle * 180 / 3.14)
        self.pos += cmath.rect(self.speed, self.angle) * self.impulse


class DefaultManager:
    @staticmethod
    def events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if close button(X) is pressed, then quit the program
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                        Playable.playables=[]
                        Drawable.drawables=[]
                        selectables=[]
                        return False
        return True


class Event:
    manager = DefaultManager


def init():
    global screen, clock, FPS, scr_size, center, manager
    pygame.init()
    FPS = 20
    scr_size = (width, height) = (800, 400)  # setting a sceen size
    center = coords(scr_size)/2
    screen = pygame.display.set_mode(scr_size)  # creating a screen object using pygame.display class
    clock = pygame.time.Clock()  # creating a clock object, used to provide delay to the objects



def gameloop():
    while Event.manager.events():
        Playable.play_all()
        Drawable.draw_all()
        clock.tick(FPS)
