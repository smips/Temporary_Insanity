﻿import libtcodpy as libtcod

class GameObject(object):
    """The basis for all objects in the game"""
    def __init__(self, x, y, char, fcolor, bcolor):
        self.x = x
        self.y = y
        self.char = char
        self.fcolor = fcolor
        self.bcolor = bcolor

    def draw(self, camera, map, distance):
        fov_damping = 20
        if not libtcod.map_is_in_fov(map.fov_map, self.x, self.y):
            f_color = self.fcolor * libtcod.dark_gray
            b_color = self.bcolor * libtcod.dark_gray
        else:
            f_color = self.fcolor
            b_color = self.bcolor * libtcod.Color(255 - (distance * fov_damping), 255 - (distance * fov_damping),255 - (distance * fov_damping))
        (t_x, t_y) = camera.to_camera_coordinates(self.x, self.y)
        libtcod.console_put_char_ex(0, t_x, t_y, str(self.char), f_color, b_color)

    def move(self, dx, dy):
        libtcod.console_put_char(0,self.x, self.y, ' ')
        self.x += dx
        self.y += dy


