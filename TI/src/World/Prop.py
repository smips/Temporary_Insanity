import GameObject
import DataGrinder

class Prop(GameObject.GameObject):
    """Game objects which do not act(unless perhaps acted upon). Only 1 per Tile."""
    def __init__(self, x, y, ID, map):
        self.x = x
        self.y = y

        prop_data = DataGrinder.get_prop_data(ID)

        self.char = prop_data['Char']
        self.fcolor = prop_data['Fcolor']
        self.bcolor = map[x][y].bcolor
        self.solid = prop_data['Solid']
        self.block_sight = prop_data['Block_sight']

        map[x][y].prop = self


