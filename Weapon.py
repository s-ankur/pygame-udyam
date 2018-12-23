import pygame
import random
import cmath

from Engine import Drawable, Playable, Absolute, Moveable
import Engine
import sprites
from Helper import dist
from Misc import Ephemeral


def hurt_target(source, stats):  # hurt the ship if it exists
    if source.target is not None:

        if source.target.health > 0:
            source.target.health -= stats.damage * random.random()
            source.target.team.attackedby(source)
        else:
            if random.randrange(0, 3) == 2 and not hasattr(source, 'events'):
                source.target.health = 40
                source.target.target = None
                source.target.boss = source
                source.team.register(source.target)
                source.team.target(None)

            else:

                source.target.delete()
                source.target = None


class DefaultWeapon:
    damage = 10
    cooldown = 15
    range = 80


class Weapon(Playable):

    def __init__(self, source):  # initalize weapon
        self.source = source
        self.cooldown = 0

    def play(self):
        self.cooldown -= 1
        if self.cooldown == 0:
            self.del_playable()

    def fire_weapon(self):
        if self.cooldown == 0 and self.source.target is not None \
                and dist(self.source.pos, self.source.target.pos) < self.stats.range:
            self.init_playable()
            self.cooldown = self.stats.cooldown
            self.fire()

    def fire(self):
        pass


class Phasor(Weapon, Drawable):
    stats = DefaultWeapon

    def fire(self):
        hurt_target(self.source, self.stats)
        self.init_drawable()

    stats = DefaultWeapon

    def draw(self):
        if self.cooldown < 10:
            self.del_drawable()
            return

        if self.source.target is not None:
            pos = self.source.pos + Engine.center - self.source.focus.pos
            target_pos = self.source.target.pos + Engine.center - self.source.focus.pos
            pygame.draw.line(Engine.screen, (255, 0, 0), (pos.real, pos.imag), (target_pos.real, target_pos.imag))


class MissileLauncherStats:
    cooldown = 40
    range = 400


class MissileLauncher(Weapon):
    stats = MissileLauncherStats

    def fire(self):
        Missile(self.source)


class MissileStats:
    damage = 50
    cooldown = 70
    range = 7


class Missile(Ephemeral, Moveable):
    stats = MissileStats
    sprite = sprites.Bullet3
    speed = 6
    impulse = 1
    image = sprite.sprite

    def __init__(self, source):
        if source.target is not None:
            self.source = source
            self.init_ephemeral(self.stats.cooldown, source.pos)

    def ephemeral(self):
        if self.source.target is not None:
            if dist(self.pos, self.source.target.pos) < self.stats.range:
                self.del_ephemeral()
                hurt_target(self.source, self.stats)
            else:
                self.angle = cmath.phase(self.source.target.pos - self.pos)
                self.moveable()


weapons = (Phasor, MissileLauncher)
