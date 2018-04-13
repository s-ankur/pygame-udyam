__author__ = 'AnkuR'
from Engine.Engine import Engine
from Entities import PlayerShip,AiShip,RockMaker
from Engine.Bases import Sprite

engine=Engine()
RockMaker()
PlayerShip()

engine.run()
