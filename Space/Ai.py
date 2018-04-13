__author__ = 'AnkuR'
import random,cmath
from Bases import none




class EasyAI:
    patrol_dist=70
    min_health=40
    flee_dist=150

    def __init__(self,source):
        self.source=source
        self.think=self.patrol
        self.patrol_count=0

    def patrol(self):
        if self.source.target.alive:
            self.think=self.attack
            return

        if not self.source.boss.alive: #no point in patrolling
            if self.source.boss.target.alive: # capture
                self.source.boss=self.source.boss.target
            else:
                self.think= self.standby
                self.source.boss=none
                self.source.impulse=0
            return

        if self.source.boss.target.alive:
            self.source.target=self.source.boss.target
            return


        (boss_dist, boss_angle) = cmath.polar(self.source.boss.pos - self.source.pos)
        if boss_dist > self.patrol_dist:#out of boss_range
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
        if not self.source.target.alive:
            self.think = self.patrol
            self.source.target = none
            return

        if self.source.health<self.min_health:
            self.think = self.flee
            return

        (target_dist, target_angle) = cmath.polar(self.source.target.pos - self.source.pos)
        if target_dist > self.source.weapon.range:
            self.think=self.chase
        else:
            self.source.angle = target_angle + 1.51  #spiral!! face to target
            self.source.impulse = .46
            self.source.fire()


    def chase(self):
        if not self.source.target.alive:
            self.think = self.patrol
            self.source.target=none
            return

        self.source.impulse=.66
        (target_dist, target_angle) = cmath.polar(self.source.target.pos - self.source.pos)
        if target_dist< self.source.weapon.range/1.3:
            self.think = self.attack
        else:
            self.source.angle=target_angle





    def flee(self):
        if not self.source.target.alive:
            self.think = self.patrol
            self.source.target=none
            return

        (target_dist, target_angle) = cmath.polar(self.source.pos-self.source.target.pos)
        if target_dist < self.flee_dist:
            self.source.impulse = .4
            self.source.angle =  target_angle
        else:
            self.think = self.patrol
            self.source.target = none

