import Tile
import Prop
import random
import Cartographer

#args = Width, Height, Tile_IDs, Size_Variance, Name, Num_Rooms, Script_ID
def call(args):
    objects = []
    map = [[0 for x in range(args['Height'])] for x in range(args['Width'])]

    for x in range(args['Width']):
        for y in range(args['Height']):
            #Populate entire map with walls
            map[x][y] = Tile.Tile(x, y, args['Tile_IDs'][1])
            objects.append(map[x][y])

    rooms = []
    num_rooms = args['Num_Rooms']
    for x in range(num_rooms):    
        success = True    
        rand_x = args['Size_Variance'] + random.randint(-4,4)
        rand_y = args['Size_Variance'] + random.randint(-4,4)
        rect = Cartographer.Rectangle(Cartographer.get_random_point(1,args['Width'] - rand_x,1,args['Height'] - rand_y), rand_x, rand_y)
        for room in rooms:
            if rect.intersects(room):
                if num_rooms < args['Num_Rooms'] + 3:
                    num_rooms = num_rooms + 1
                    success = False
        if success:
            rooms.append(rect)
    for room in rooms:
        pts = room.get_points()
        for pt in pts:
            map[pt.x][pt.y] = Tile.Tile(pt.x, pt.y, args['Tile_IDs'][0])

    for x in range(len(rooms) - 1):
        pt1 = Cartographer.Point(rooms[x].center.x, rooms[x].center.y)
        pt2 = Cartographer.Point(rooms[x + 1].center.x, rooms[x + 1].center.y)
        line1 = Cartographer.create_h_tunnel(pt1.x, pt2.x, pt1.y)
        line2 = Cartographer.create_v_tunnel(pt1.y, pt2.y, pt2.x)
        for pt in line1:
            map[pt.x][pt.y] = Tile.Tile(pt.x, pt.y, args['Tile_IDs'][0])
        for pt in line2:
            map[pt.x][pt.y] = Tile.Tile(pt.x, pt.y, args['Tile_IDs'][0])

    return (map, objects, rooms)