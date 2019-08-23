from Tile import Tile
from SpellEffect import SpellEffect
from pprint import pprint


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class TheWorld(metaclass=Singleton):
    def __init__(self):
        """
        Only speaks in WorldEffect
        """
        print("Starting The world.....")
        self.tiles = [[]]
        self.prepare_tiles()

    def prepare_tiles(self):
        self.tiles = [[Tile([x, y]) for x in range(10)] for y in range(10)]
        return

    def add_world_element(self, world_element):
        """
            edits the world grid of tiles based on world element shape and position
        :param world_element:
        :return:
        """
        for tile_co_ords in world_element.shape.get_relative_affected_tiles():
            x = world_element.position[0] + tile_co_ords[0]
            y = world_element.position[1] + tile_co_ords[1]
            self.tiles[x][y].add_object(world_element)

    def resolve_tiles(self):
        for i in self.tiles:
            for j in i:
                j.resolve_tile()

    def print_grid(self):
        pprint([[len(j.objects) for j in i] for i in self.tiles])

    def get_total_objects(self):
        objects = 0
        for i in self.tiles:
            for j in i:
                if len(j.objects) > 0:
                    objects += 1
        return objects