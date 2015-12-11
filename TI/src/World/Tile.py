import GameObject
import DataGrinder

class Tile(GameObject.GameObject):
    """Tiles for a game map. May contain 1 prop, 1 actor, 1 item"""
    def __init__(self, x, y, ID, prop=None, actor=None,item=None):
        self.x = x
        self.y = y
        self.prop = prop
        self.actor = actor
        self.item = item

        tile_data = DataGrinder.get_tile_data(ID)
        self.char = tile_data['Char']
        self.fcolor = tile_data['Fcolor']
        self.bcolor = tile_data['Bcolor']
        self.solid = tile_data['Solid']
        self.block_sight = tile_data['Block_sight']

    def draw(self, camera):
        super(Tile, self).draw(camera)
        if self.actor != None:
            self.actor.draw(camera)
            return
        elif self.item != None:
            self.item.draw(camera)
            return
        elif self.prop != None:
            self.prop.draw(camera)
            return
