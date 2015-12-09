import libtcodpy as libtcod
import sys
from time import sleep

sys.path.insert(0, 'I:\\TI\\TI\\src\\World\\')

import GameObject
import Tile

DEBUG = 1

game_iteration = 0

objects = []
 
#actual size of the window
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
 
LIMIT_FPS = 60  #20 frames-per-second maximum

def dprint(arg):
    global DEBUG
    if DEBUG:
        print(arg) 
 
def handle_keys():
    global player
 
    #key = libtcod.console_check_for_keypress()  #real-time
    key = libtcod.console_wait_for_keypress(True)  #turn-based
 
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
 
    elif key.vk == libtcod.KEY_ESCAPE:
        return True  #exit game
 
    #movement keys
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        player.move(0,-1)
 
    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        player.move(0,1)
 
    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        player.move(-1,0)
 
    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        player.move(1,0)
 
 
#############################################
# Initialization & Main Loop
#############################################
dprint('Initialization started') 

libtcod.console_set_custom_font('assets/arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'python/libtcod tutorial', False)
libtcod.sys_set_fps(LIMIT_FPS)

player = GameObject.GameObject(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, '@', libtcod.white, libtcod.BKGND_NONE)
tile1 = Tile.Tile(SCREEN_WIDTH/2,SCREEN_HEIGHT/3,'#',libtcod.red, libtcod.BKGND_NONE)
tile2 = Tile.Tile(SCREEN_WIDTH/2,SCREEN_HEIGHT/4,'#',libtcod.blue, libtcod.white)
objects.append(player)
objects.append(tile1)
objects.append(tile2)

dprint('Initialization complete')
 
while not libtcod.console_is_window_closed():
    dprint('Game loop iteration ' + str(game_iteration) + ' started.') 
    libtcod.console_set_default_foreground(0, libtcod.white)
    for object in objects:
        object.draw()
 
    libtcod.console_flush()
 
    #handle keys and exit game if needed
    exit = handle_keys()
    if exit:
        break
    game_iteration = game_iteration + 1
    sleep(0.01)