import libtcodpy as libtcod
import sys
from time import sleep
import os, math, random

sys.path.insert(0, os.path.realpath(__file__).replace("TI.py","World"))
sys.path.insert(0, os.path.realpath(__file__).replace("TI.py","Engine"))
sys.path.insert(0, os.path.realpath(__file__).replace("TI.py","Scripts"))

import GameObject
import Tile
import DataGrinder
import Actor
import Prop
import Camera
import ScriptHandler

DEBUG = 1

game_iteration = 0

objects = []
 
#actual size of the window
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

DISPLAY_WIDTH = 60
DISPLAY_HEIGHT = 50

MAP_WIDTH = 80
MAP_HEIGHT = 80

map = [[0 for x in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]
 
LIMIT_FPS = 60  #60 frames-per-second maximum

def dprint(arg):
    global DEBUG
    if DEBUG:
        print(arg) 
 
def handle_keys():
    global player, map

    key = libtcod.console_check_for_keypress(True)
 
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
 
    elif key.vk == libtcod.KEY_ESCAPE:
        return True  #exit game
    
    #Call a test script
    elif key.vk == libtcod.KEY_KP5:
        ScriptHandler.CallExternalScript(1)
        
    #movement keys
    if key.vk == (libtcod.KEY_KP8):
        player.move(0,-1, map)
 
    elif key.vk == (libtcod.KEY_KP2):
        player.move(0,1, map)
 
    elif key.vk == (libtcod.KEY_KP4):
        player.move(-1,0, map)
 
    elif key.vk == (libtcod.KEY_KP6):
        player.move(1,0, map)
    
    elif key.vk == (libtcod.KEY_KP7):
        player.move(-1,-1, map)
 
    elif key.vk == (libtcod.KEY_KP9):
        player.move(1,-1, map)
 
    elif key.vk == (libtcod.KEY_KP1):
        player.move(-1,1, map)
 
    elif key.vk == (libtcod.KEY_KP3):
        player.move(1,1, map)
    if key.vk != libtcod.KEY_NONE:
        return False
 
def update():
    #ScriptHandler.CallExternalScript(1)
    pass

def render():
    global map, camera, player, SCREEN_WIDTH, SCREEN_HEIGHT
    camera.move_camera(player.x, player.y, MAP_WIDTH, MAP_HEIGHT)
    libtcod.console_clear(0)
    libtcod.console_set_default_foreground(0, libtcod.white)
    i = 1
    for x in range(DISPLAY_WIDTH):
        for y in range(DISPLAY_HEIGHT):
            (map_x, map_y) = (camera.x + x, camera.y + y)
            map[map_x][map_y].draw(camera) 

    libtcod.console_print(0, 0, 0, 'FPS: ' + str(libtcod.sys_get_fps()))
    libtcod.console_flush()

def input():
    return handle_keys()

def make_map():
    global map, objects,MAP_HEIGHT,MAP_WIDTH
    for x in range(MAP_WIDTH):
        for y in range(MAP_HEIGHT):
            map[x][y] = Tile.Tile(x, y, 1)
            #if random.randint(0,0):
                #map[x][y].prop = Prop.Prop(x,y,1,map)
                #objects.append(map[x][y].prop)
            objects.append(map[x][y])

#############################################
# Initialization & Main Loop
#############################################
dprint('Initialization started') 

libtcod.console_set_custom_font('assets/arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/libtcod tutorial', False)
libtcod.sys_set_fps(LIMIT_FPS)

make_map()
player = Actor.Actor(MAP_WIDTH/2, MAP_HEIGHT/2, 1, map)
objects.append(player)
camera = Camera.Camera(player.x, player.y, DISPLAY_WIDTH, DISPLAY_HEIGHT)
dprint('Initialization complete')
 
while not libtcod.console_is_window_closed():
    update()
    render()
    exit = input()
    
    #exit game if needed
    if exit:
        break

