import AI_BASIC_FUNCTIONS as basic_ai
import libtcodpy as libtcod
#args = {self, map}
def call(args):
    #global self, map, FOV_RECOMPUTE, enemy
    self = args['self']
    map = args['map']
    FOV_RECOMPUTE = False

    key = libtcod.console_check_for_keypress(True)
 
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        #Alt+Enter: toggle fullscreen
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
 
    elif key.vk == libtcod.KEY_ESCAPE:
        return True  #exit game
    
    #Call a test script
    elif key.vk == libtcod.KEY_KP5:
        #enemy.tick(map)
        FOV_RECOMPUTE = True
        
    #movement keys
    if key.vk == (libtcod.KEY_KP8):
        self.move(0,-1, map)
        FOV_RECOMPUTE = True
 
    elif key.vk == (libtcod.KEY_KP2):
        self.move(0,1, map)
        FOV_RECOMPUTE = True
 
    elif key.vk == (libtcod.KEY_KP4):
        self.move(-1,0, map)
        FOV_RECOMPUTE = True
 
    elif key.vk == (libtcod.KEY_KP6):
        self.move(1,0, map)
        FOV_RECOMPUTE = True
    
    elif key.vk == (libtcod.KEY_KP7):
        self.move(-1,-1, map)
        FOV_RECOMPUTE = True
 
    elif key.vk == (libtcod.KEY_KP9):
        self.move(1,-1, map)
        FOV_RECOMPUTE = True
 
    elif key.vk == (libtcod.KEY_KP1):
        self.move(-1,1, map)
        FOV_RECOMPUTE = True
 
    elif key.vk == (libtcod.KEY_KP3):
        self.move(1,1, map)
        FOV_RECOMPUTE = True

    #if key.vk != libtcod.KEY_NONE:
    #    return False

    return FOV_RECOMPUTE