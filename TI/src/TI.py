import libtcodpy as libtcod
import sys
from time import sleep
import os, math, random

sys.path.insert(0, os.path.realpath(__file__).replace("TI.py","World"))
sys.path.insert(0, os.path.realpath(__file__).replace("TI.py","Engine"))
sys.path.insert(0, os.path.realpath(__file__).replace("TI.py","Scripts"))

import GameObject,Tile,DataGrinder,Actor,Prop,Camera,ScriptHandler
import Map

DEBUG = 1

game_iteration = 0

objects = []
 
#actual size of the window
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

DISPLAY_WIDTH = 60
DISPLAY_HEIGHT = 50

FOV_RECOMPUTE = True
 
LIMIT_FPS = 60  #60 frames-per-second maximum

FPS_CONSOLE = libtcod.console_new(10,1)

def dprint(arg):
    global DEBUG
    if DEBUG:
        print(arg) 
 
def handle_keys():
    global player, map, FOV_RECOMPUTE

    key = libtcod.console_check_for_keypress(True)
 
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
 
    elif key.vk == libtcod.KEY_ESCAPE:
        return True  #exit game
    
    #Call a test script
    elif key.vk == libtcod.KEY_KP5:
        args = {}
        args['player'] = player
        ScriptHandler.CallExternalScript(1, args)
        
    #movement keys
    if key.vk == (libtcod.KEY_KP8):
        player.move(0,-1, map)
        FOV_RECOMPUTE = True
 
    elif key.vk == (libtcod.KEY_KP2):
        player.move(0,1, map)
        FOV_RECOMPUTE = True
 
    elif key.vk == (libtcod.KEY_KP4):
        player.move(-1,0, map)
        FOV_RECOMPUTE = True
 
    elif key.vk == (libtcod.KEY_KP6):
        player.move(1,0, map)
        FOV_RECOMPUTE = True
    
    elif key.vk == (libtcod.KEY_KP7):
        player.move(-1,-1, map)
        FOV_RECOMPUTE = True
 
    elif key.vk == (libtcod.KEY_KP9):
        player.move(1,-1, map)
        FOV_RECOMPUTE = True
 
    elif key.vk == (libtcod.KEY_KP1):
        player.move(-1,1, map)
        FOV_RECOMPUTE = True
 
    elif key.vk == (libtcod.KEY_KP3):
        player.move(1,1, map)
        FOV_RECOMPUTE = True

    if key.vk != libtcod.KEY_NONE:
        return False
 
def update():
    pass

def render():
    global map, camera, player, SCREEN_WIDTH, SCREEN_HEIGHT, FOV_RECOMPUTE
    camera.move_camera(player.x, player.y, map.width, map.height)
    libtcod.console_set_default_foreground(0, libtcod.white)

    temp_player_x, temp_player_y = camera.to_camera_coordinates(player.x, player.y)

    if FOV_RECOMPUTE:
        libtcod.console_clear(0)
        libtcod.map_compute_fov(map.fov_map, player.x, player.y, 10, True, 1)
        FOV_RECOMPUTE = False
    
        for x in range(DISPLAY_WIDTH):
            for y in range(DISPLAY_HEIGHT):
                (map_x, map_y) = (camera.x + x, camera.y + y)
                distance = get_distance(player.x, map_x, player.y, map_y)
                map.map[map_x][map_y].draw(camera, map, distance) 
    
    libtcod.console_print(FPS_CONSOLE, 0, 0, 'FPS: ' + str(libtcod.sys_get_fps()))
    libtcod.console_blit(FPS_CONSOLE, 0, 0, 10, 1, 0, 0, 0)
    libtcod.console_flush()

def get_distance(x1, x2, y1, y2):
    dx = x2 - x1
    dy = y2 - y1
    return int(math.sqrt(dx ** 2 + dy ** 2))

    

def input():
    return handle_keys()

#############################################
# Initialization & Main Loop
#############################################
dprint('Initialization started') 

libtcod.console_set_custom_font('assets/arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/libtcod tutorial', False)
libtcod.sys_set_fps(LIMIT_FPS)

map = Map.Map(1)
player = Actor.Actor(map.rooms[0].center.x, map.rooms[0].center.y, 1, map)
map.objects.append(player)
camera = Camera.Camera(player.x, player.y, DISPLAY_WIDTH, DISPLAY_HEIGHT)
dprint('Initialization complete')
 
while not libtcod.console_is_window_closed():
    update()
    render()
    exit = input()
    
    #exit game if needed
    if exit:
        break

