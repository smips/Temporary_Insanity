import libtcodpy as libtcod

class GameObject(object):
    """The basis for all objects in the game"""
    def __init__(self, x, y, char, fcolor, bcolor):
        self.x = x
        self.y = y
        self.char = char
        self.fcolor = fcolor
        self.bcolor = bcolor

    def draw(self):
        libtcod.console_put_char_ex(0, self.x, self.y, self.char, self.fcolor, self.bcolor)

    def move(self, dx, dy):
        libtcod.console_put_char(0,self.x, self.y, ' ')
        self.x += dx
        self.y += dy

