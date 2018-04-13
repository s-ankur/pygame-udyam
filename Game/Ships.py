from Misc import Explosion

__author__ = 'AnkuR'

import cmath,random, pygame
from Engine import Absolute, Playable, Event, DefaultManager,scr_size,clock,Drawable,screen ,Moveable
import sprites
from Weapon import weapons
import AIs
from status import *
from Planets import Planet
from Teams import Team
from Helper import coords
selectables=[]


class Ship(Playable, Absolute,Moveable):
    speed = 4

    def delete(self):
        self.del_ship()

    def del_ship(self):
        self.del_playable()
        self.del_drawable()
        if self in selectables:
            selectables.remove(self)
        Explosion(self.pos)

    def init_ship(self, pos):
        self.pos=pos
        self.health = 100


    def start_ship(self):
        self.init_playable()
        self.init_drawable()
        selectables.append(self)
        self.angle = 0
        self.impulse = 0
        self.target = None

    def start(self):
        self.start_ship()



class AiShip(Ship):
    AI=AIs.EasyAI


    def __init__(self, boss,sprite):
        self.boss=boss
        self.boss_pos = boss.pos
        self.sprite=sprite
        self.init_aiship()


    def init_aiship(self):
        r1 = random.randrange(-patrol_dist, patrol_dist)
        r2 = random.randrange(-patrol_dist, patrol_dist)
        pos = self.boss_pos + complex(r1, r2)
        self.ai=self.AI(self)
        self.init_ship(pos)
        self.start()

    
    def play(self):
        self.ai.think()
        self.moveable()


class PlayerShip(Ship):
    sprite= sprites.OrangeShip

    def __init__(self, pos):
        self.init_ship(pos)
        self.start()

    def start(self):
        Event.manager=self
        Absolute.focus=self
        self.move = [0, 0]
        self.start_ship()
        selectables.remove(self)
        Selector(self)

    def delete(self):
        self.del_ship()
        Event.manager=DefaultManager

    def events(self):
        global selectables
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if close button(X) is pressed, then quit the program
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move[0] = -.1
                if event.key == pygame.K_RIGHT:
                    self.move[0] = .1
                if event.key == pygame.K_UP:
                    self.move[1] = 1
                if event.key == pygame.K_DOWN:
                    self.weapon.fire_weapon()
                if event.key == pygame.K_TAB:
                    length=len(selectables)
                    if length==0:
                        self.target=None
                    else:
                        self.target=selectables[random.randrange(0,length)]

                if event.key == pygame.K_w:
                    warp()
                if event.key == pygame.K_m:
                    Playable.playables=[]
                    Drawable.drawables=[]
                    selectables=[]
                    return False

            if event.type == pygame.KEYUP:  # if a key is unpressed
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.move[1] = 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.move[0] = 0
        return True


    def play(self):
        self.process_keys()
        self.moveable()

    def process_keys(self):
        self.angle += self.move[0]
        if self.move[1] == 1:
            self.impulse += .2
        else:
            self.impulse -= .01
        if self.impulse > .7:
            self.impulse = .7
        elif self.impulse < 0:
            self.impulse = 0


class Selector(Absolute,Playable):

    image= pygame.image.load('_selector.bmp')
    image.set_colorkey((0,0,0))

    def __init__(self,player):
        self.player=player
        self.init_playable()


    def play(self):
        target=self.player.target
        if target is None:
            self.del_drawable()
        else:
            if self not in Drawable.drawables:
                self.init_drawable()
            self.pos=target.pos


size=(scr_size[0]/2-30,scr_size[1]/2-30)
player_team=None


def pos():
    return complex(random.randrange(-size[0], size[0]), random.randrange(-size[1], size[1]))


def firsttime():
    global player_team

    planet=Planet(complex(0,0),sprites.AquaPlanet)
    planetteam=Team()
    for i in range(random.randrange(1,5)):
        ship=AiShip(planet,sprites.GreenShip)
        ship.weapon=weapons[0](ship)
        planetteam.register(ship)

    player=PlayerShip(coords((40,40)))
    player.weapon=weapons[1](player)
    guardian=AiShip(player,sprites.OrangeShip)
    guardian.weapon=weapons[0](guardian)
    player_team=Team(player,guardian)


def warp():
        global selectables
        Playable.playables=[]
        Drawable.drawables=[]
        selectables=[]
        screen.fill((0,0,0))
        warpimg=pygame.image.load('_warpimg.bmp')
        screen.blit(warpimg, (600,350))
        pygame.display.update()
        clock.tick(2)
        create_planets()
        player_team.start()


def create_planets():
    n_planets = int(1.1 * (random.random() + 1))

    for i in range(n_planets):
        index = random.randrange(0, len(sprites.planets))
        planet_pos=pos()
        planet=Planet(planet_pos,sprites.planets[index])
        create_ships(planet)


def create_ships(planet):
        n_ships = random.randrange(1,6)
        index_sprite = random.randrange(0, len(sprites.ships))

        planetteam=Team()
        for i in range(1, n_ships):
            weapon_index = random.randrange(0, len(weapons))
            ship=AiShip(planet,sprites.ships[index_sprite])
            ship.weapon=weapons[weapon_index](ship)
            planetteam.register(ship)









