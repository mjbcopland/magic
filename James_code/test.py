from TheWorld import *
from People import Wizard

theworld = TheWorld()

tile_1 = Tile((0, 0))
Bob = Wizard((5, 3), 0)
WorldElement = Bob.shout('Lightning 10 Create Square Point 5')

Carl = Wizard((5, 5), 0)
WorldElement2 = Carl.shout('Cold 8 Create Square Point 5')

theworld.add_world_element(WorldElement)
theworld.add_world_element(WorldElement2)
theworld.resolve_tiles()
theworld.print_grid()
print(theworld.get_total_objects())

