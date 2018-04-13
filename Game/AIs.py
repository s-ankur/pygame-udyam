__author__ = 'AnkuR'
import random,cmath
from status import *





class EasyAI:
    def __init__(self,source):
        self.source=source
        self.status=self.patrol
        self.patrol_count=0

    def think(self):


        self.status()

    def patrol(self):
        if self.source.target is not None:
            self.status=self.attack
            return

        if self.source.boss is None or self.source.boss.health<0: #no point in patrolling
            self.status= self.standby
            self.source.boss=None
            self.source.impulse=0
            return

        (boss_dist, boss_angle) = cmath.polar(self.source.boss.pos - self.source.pos)
        if boss_dist > patrol_dist:#out of boss_range
            self.source.impulse=.6 #come back qickly
            self.source.angle = boss_angle
        else:#within boss range
            self.source.impulse=.1  #now slow down
            if self.patrol_count < 0:
                self.patrol_count = random.randrange(40, 150)#reset counter
                self.source.angle += random.random()*1.5 - .75 #patrol angle randomized
            else:
                self.patrol_count -= 1

    def standby(self):
        pass

    def attack(self):
        if self.source.target is None:
            self.status = self.patrol
            return

        if self.source.health<min_health:
            self.status = self.flee
            return

        (target_dist, target_angle) = cmath.polar(self.source.target.pos - self.source.pos)
        #self.source.missile.fire(self.source.target)

        if target_dist > self.source.weapon.stats.range:
            self.status=self.chase
        else:
            self.source.angle = target_angle + 1.51  #spiral!! face to target
            self.source.impulse = .46
            self.source.weapon.fire_weapon()


    def chase(self):
        if self.source.target is None:
            self.status = self.patrol
            return

        self.source.impulse=.66
        (target_dist, target_angle) = cmath.polar(self.source.target.pos - self.source.pos)
        if target_dist< self.source.weapon.stats.range/1.3:
            self.status = self.attack
        else:
            self.source.angle=target_angle





    def flee(self):
        if self.source.target is None:
            self.status = self.patrol
            return

        (target_dist, target_angle) = cmath.polar(self.source.pos-self.source.target.pos)
        if target_dist < flee_dist:
            self.source.impulse = .4
            self.source.angle =  target_angle
        else:
            self.status = self.patrol
            self.source.target = None