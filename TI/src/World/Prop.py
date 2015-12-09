import GameObject

class Prop(GameObject.GameObject):
    """Game objects which do not act(unless perhaps acted upon). Only 1 per Tile."""
    def __init__(self, x, y, char, bcolor):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

