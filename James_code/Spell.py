from Targeting import *
from SpellShapes import *


class Spell:
    def __init__(self, incantation):
        self.incantation = incantation
        self.element = None
        self.action = None
        self.shape = None
        self.target = None
        self.affix = None

    def decode_incantation(self, position):
        components = self.incantation.split()
        if components[0] == 'Fire':
            self.element = SpellEffectFire(int(components[1]))
            self.action = components[2]
        elif components[0] == 'Cold':
            self.element = SpellEffectCold(int(components[1]))
            self.action = components[2]
        if components[3] == 'Cone':
            self.shape = Square
        if components[4] == 'Point':
            self.target = Point(int(components[5]), position)

    def cast(self):
        if self.action == 'Create':
            position, velocity = self.target.properties()
            return self.element.create(position, velocity, self.shape)
        elif self.action == 'Absorb':
            self.element.absorb()
        elif self.action == 'Displace':
            self.element.displace()

    def cost(self):
        return

