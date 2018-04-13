__author__ = 'AnkuR'
import pygame

from Colors import *


class OrangeShip:
    sprite = pygame.image.load('_ship_orange.bmp')
    sprite.set_colorkey(black)


class GreenShip:
    sprite = pygame.image.load('_ship_green.bmp')
    sprite.set_colorkey(black)


class PurpleShip:
    sprite = pygame.image.load('_ship_purple.bmp')
    sprite.set_colorkey(black)


class BlueShip:
    sprite = pygame.image.load('_ship_blue.bmp')
    sprite.set_colorkey(black)

ships=(BlueShip,PurpleShip,GreenShip,OrangeShip)


"""___Planets___"""


class AquaPlanet:
    sprite = pygame.image.load('_planet_aqua.bmp')
    sprite.set_colorkey(black)


class ChlorinePlanet:
    sprite = pygame.image.load('_planet_chlorine.bmp')
    sprite.set_colorkey(black)


class BluePlanet:
    sprite = pygame.image.load('_planet_blue.bmp')
    sprite.set_colorkey(black)


class RedPlanet:
    sprite = pygame.image.load('_planet_red.bmp')
    sprite.set_colorkey(black)

planets=(ChlorinePlanet,BluePlanet,RedPlanet)


"""___Misc___"""


class Bullet1:
    sprite = pygame.image.load('_bullets_1.png')
    sprite.set_colorkey(black)


class Bullet2:
    sprite = pygame.image.load('_bullets_2.png')
    sprite.set_colorkey(black)

class Bullet3:
    sprite = pygame.image.load('_bullets_3.bmp')
    sprite.set_colorkey(black)
