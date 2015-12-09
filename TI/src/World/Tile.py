import GameObject

class Tile(GameObject.GameObject):
    """Tiles for a game map. May contain 1 prop, 1 actor, 1 item"""
    def __init__(self, x, y, char, fcolor, bcolor, prop=None, actor=None,item=None):
        self.x = x
        self.y = y
        self.char = char
        self.fcolor = fcolor
        self.bcolor = bcolor
        self.prop = prop
        self.actor = actor
        self.item = item

    def draw(self):
        super(Tile, self).draw()
        if self.actor != None:
            self.actor.draw(self)
            return
        elif self.item != None:
            self.item.draw(self)
            return
        elif self.prop != None:
            self.prop.draw(self)
            return
