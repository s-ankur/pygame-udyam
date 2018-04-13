from Bases import Mortal, Solid, Draw
from Classes import automatic, Ephemeral, Explosion
from Helper import in_range
from Shared import log,commands
from Weapon import UntargetedWeapon

__author__ = 'AnkuR'


@automatic
class Bomb(Mortal, Ephemeral, Solid):
    show_log = False

    image = Draw.load('1.bmp', colorkey=(255, 255, 255))
    range = 60
    damage = 80
    cooldown = 70
    speed = 2
    health = 30

    def __init__(self,pos):
        super().__init__(pos+complex(1,0))


    def onCollide(self,pos):
        self.play=lambda:self.move(self.speed*pos)  # hurl bomb
        self.onCollide=lambda x:self.kill() # now bomb is armed and will explode if touched


    def kill(self):
        super().kill()
        for player in Mortal.mortals[:]:
            if in_range(self, player, self.range):
                player.hurt(self.damage)
        Explosion(self.pos)



class BombDrop(UntargetedWeapon):
    cooldown_max=80
    range=100

    Projectile = Bomb

    @classmethod
    def bombs_away(cls):
        log('Aerial Bombardment Initiated')
        for i in range(10):
            Bomb(Draw.randpos())


commands['bomb'] = Bomb
commands['bombsaway'] = BombDrop.bombs_away