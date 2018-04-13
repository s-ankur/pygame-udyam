from Engine import Absolute
import sprites
from Helper import coords


class Planet(Absolute):

    def __init__(self, pos,sprite):
        self.health= 500
        self.sprite = sprite
        self.image=sprite.sprite
        self.pos=pos
        self.start()

    def start(self):
        self.init_absolute(self.pos)
