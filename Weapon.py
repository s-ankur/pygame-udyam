
from Engine.Helper import in_range
from Engine.Bases import Base
from Engine.Classes import Owned


__author__ = 'AnkuR'


class Weapon(Owned,Base):
    playable = True
    show_log = False


    Projectile=NotImplemented

    cooldown = 0
    range = 100

    def play(self):
        if self.cooldown <= 0:
            return
        self.cooldown -= 1


class UntargetedWeapon(Weapon):

    def fire_weapon(self):
        if self.cooldown == 0 :
            self.Projectile(self.owner.pos)
            self.cooldown=self.cooldown_max


class TargetedWeapon(Weapon):

    def fire_weapon(self, target=None):
        player=self.owner
        target=self.owner.target
        if self.cooldown == 0 and in_range(player,target, self.range):
            self.Projectile(target,player)
            target.target=player
            self.cooldown=self.cooldown_max