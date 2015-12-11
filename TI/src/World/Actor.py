import GameObject
import DataGrinder
import libtcodpy as libtcod

class Actor(GameObject.GameObject):
    """All GameObjects which take turns"""
    def __init__(self, x, y, ID, map):
        self.x = x
        self.y = y

        actor_data = DataGrinder.get_actor_data(ID)
        self.char = actor_data['Char']
        self.bcolor = map[self.x][self.y].bcolor
        self.fcolor = actor_data['Fcolor']

        map[x][y].actor = self

    def move(self, dx, dy, map):
        new_x = self.x + dx
        new_y = self.y + dy
        blocked = map[new_x][new_y].solid
        if map[new_x][new_y].prop != None:
            blocked += map[new_x][new_y].prop.solid
        if map[new_x][new_y].actor != None:
            blocked += 1
        if not blocked:
            libtcod.console_put_char(0,self.x, self.y, ' ')
            map[self.x][self.y].actor = None
            super(Actor, self).move(dx, dy)
            map[self.x][self.y].actor = self
            self.bcolor = map[self.x][self.y].bcolor
            print(str(self.x))
