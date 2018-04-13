from Engine.Bases import Sprite, Draw, Base
from Engine.Classes import automatic, Ephemeral, Move
from Engine.Helper import cap,in_range,pack
from Shared import commands , colors
from Weapon import TargetedWeapon

@automatic
class MicrowaveShot(Ephemeral, Base):
    drawable = True

    damage = 1
    cooldown = 20
    range = 110

    def __init__(self,  target,player):
        super().__init__()
        self.player = player
        self.target = target

    def draw(self):
        p = self.player.absolute()
        t = self.target.absolute()
        p_pos = pack(p)
        t_pos = pack(t)
        Draw.lines(colors['red'], p_pos, t_pos)

    def play(self):
        if self.target.hurt(self.damage) or not in_range(self.player, self.target, self.range):
            self.deregister()


class Microwave(TargetedWeapon):
    range = 100
    cooldown_max = 60

    ms=None

    Projectile=MicrowaveShot

    def deregister(self):
        super().deregister()
        if self.ms :
            self.ms.deregister()
            self.ms=None


@automatic
class Bullet(Ephemeral,Move,Sprite):

    damage=5
    range=5
    speed=10
    cooldown=10
    image = Draw.load(r'_bullets_3.bmp', colorkey=(255, 255, 255))

    def __init__(self,target,player):
        super().__init__(player.pos)
        self.target=target
        self.direction = cap( target.pos-player.pos)

    def play(self):
        super().play()

        if self.target and in_range(self.target,self,self.range):
            self.target.hurt(self.damage)
            self.deregister()
            return


    def deregister(self):
        super().deregister()
        self.target=None


class Gun(TargetedWeapon):
    cooldown_max=10
    Projectile=Bullet
    range = 100

class ElectroBullet(Bullet):
    speed = 8
    damage = 2
    range = 20
    cooldown = 150

    image = Draw.load(r'_bullets_2.png', colorkey=(255, 255, 255))

    def play(self):
        if in_range(self.target,self,Bullet.range): # if near the electrobullet
            self.target.hurt(Bullet.damage) # hur
        super().play()

class ElectroGun(Gun):
    cooldown_max=20
    Projectile = ElectroBullet

class Missile(Bullet):
    speed=6
    damage = 15
    cooldown = 40

    image = Draw.load(r'_bullets_1.png', colorkey=(255, 255, 255))

    def play(self):
        self.direction=cap(self.target.pos-self.pos) # change direction
        super().play()  # now move

class MissileLauncher(Gun):
    Projectile = Missile
    cooldown_max = 45


weapons=(Gun,Microwave,ElectroGun,MissileLauncher)
