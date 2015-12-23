import AI_BASIC_FUNCTIONS as basic_ai
#args = {self, map}
def call(args):
    target = basic_ai.get_player(args['map'])
    (dx, dy) = basic_ai.get_target_direction(target, args['self'])
    args['self'].move(dx, dy, args['map'])
    print('Enemy Moved!')
    #basic_ai.move(args['self'], dx, dy, args['map'])