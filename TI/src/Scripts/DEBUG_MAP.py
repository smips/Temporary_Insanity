import Tile
import Prop
import random

def call(args):
    objects = []
    map = [[0 for x in range(args['Height'])] for x in range(args['Width'])]

    for x in range(args['Width']):
        for y in range(args['Height']):
            map[x][y] = Tile.Tile(x, y, args['Tile_IDs'][0])
            #if random.randint(0,1):
            #    map[x][y].prop = Prop.Prop(x,y,1,map)
            #    objects.append(map[x][y].prop)
            objects.append(map[x][y])

    return (map, objects)