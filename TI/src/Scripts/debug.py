#Test script
#All scripts should follow this format!
#Every script needs a call(DBarg1, DBarg2, DBarg3..., args)
#DBargs are any arguments from the GameData DB
#args is a dictionary of arguements passed from the game engine(the player, the map, etc)
def call(COMMENT, args):
    print(str(COMMENT))
    print('(' + str(args['player'].x) + ',' + str(args['player'].y) + ')')
