
import random

from Engine import Engine,Resources,Menu,Setables
Setables.scr_size=(800,400)
Setables.background_color=(0,0,0)
engine=Engine()
from Shared import commands
from Managers import Event
from Bases import Draw
from Space.Entities import AiShip, PlayerShip,Planet,Team
import Space.sprites as sprites
import Space.music as music
from Space.Weapons import weapons



player_spawn=complex(40,40)

def first_time():
    global player_team
    create_planets()

    player=PlayerShip(player_spawn)
    player.sprite=sprites.ships[1]

    guardian=AiShip(player,weapons[0])
    guardian.sprite=sprites.ships[1]

    player_team=Team(player,guardian)
    commands['warp']=warp


def warp():
    engine.clear() # deregister everyone
    Resources.screen.fill((0,0,0))
    Resources.screen.blit(sprites.warpimg, (600,350))
    Resources.update() # update screen
    create_planets() # create new system
    player_team.register() # reregister  only  the player's team
    Resources.clock.tick(2) #pause for effect



def warp_mangager():
    if Event.keys['w']:warp()
    return True


def create_planets():
    n_planets = int(1.1 * (random.random() + 1))
    for i in range(n_planets):
        planet=Planet(Draw.randpos())
        planet.image=random.choice(sprites.planets)
        create_ships(planet)


def create_ships(planet):
    n_ships = random.randrange(1,6)
    planetteam=Team()
    for i in range(1, n_ships):
        ship=AiShip(planet,Weapon=random.choice(weapons))
        ship.sprite=random.choice(sprites.ships)
        planetteam.add(ship)

class Load_menu:
    n=0

    @classmethod
    def init(cls):
        Event.handler.append(cls.change)
        Menu.menu=cls.load


    @classmethod
    def load(cls):
        Resources.screen.fill(Setables.background_color)
        Resources.mixer.stop()
        music.menus[cls.n].play(-1)
        Resources.screen.blit(sprites.menus[cls.n],(0,0))
        Resources.update()

    @classmethod
    def change(cls):
        keys=Event.keys
        if keys['right']:
            first_time()
            Resources.mixer.stop()
            music.menus[3].play(-1)
            Event.handler.remove(cls.change)
            Event.handler.append(warp_mangager)
            return False
        elif keys['m']:cls.n=0
        elif keys['n']:cls.n=1
        elif keys['w']:cls.n=2
        else:
            return True
        cls.load()
        return True

Resources.init()
Load_menu.init()

while Menu.run() and engine.run():
    pass





