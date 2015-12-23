import math
import libtcodpy as libtcod
#Basic utilities for AI to use, like moving

def move(self, dx, dy, map_object):
    map = map_object.map
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
        super(type(self), self).move(dx, dy)
        map[self.x][self.y].actor = self
        self.bcolor = map[self.x][self.y].bcolor

def get_player(map):
    for object in map.objects:
        if object.name == 'Player':
            return object

def get_target_direction(target, self):
    dx = target.x - self.x
    dy = target.y - self.y
    distance = math.sqrt(dx**2 + dy**2)
    dx = int(round(dx / distance))
    dy = int(round(dy / distance))
    return (dx,dy)