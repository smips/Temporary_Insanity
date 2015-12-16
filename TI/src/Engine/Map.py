import DataGrinder
import ScriptHandler
import libtcodpy as libtcod

class Map(object):
    """description of class"""
    def __init__(self, ID):
        map_data = DataGrinder.get_map_data(ID)

        self.width = map_data['Width']
        self.height = map_data['Height']
        self.size_variance = map_data['Size_Variance']
        self.name = map_data['Name']
        self.num_rooms = map_data['Num_Rooms']
        self.script_id = map_data['Script_ID']
        self.tile_ids = map_data['Tile_IDs']
        (self.map, self.objects) = ScriptHandler.CallExternalScript(self.script_id, map_data)

        self.fov_map  = libtcod.map_new(self.width, self.height)
        for x in range(self.width):
            for y in range(self.height):
                libtcod.map_set_properties(self.fov_map, x, y, not self.map[x][y].block_sight, not self.map[x][y].solid)
