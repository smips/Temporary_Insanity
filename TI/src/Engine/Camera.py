class Camera(object):
    """description of class"""
    def __init__(self,x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move_camera(self, target_x, target_y, MAP_WIDTH, MAP_HEIGHT): 
        #new camera coordinates (top-left corner of the screen relative to the map)
        new_x = target_x - self.width / 2  #coordinates so that the target is at the center of the screen
        new_y = target_y - self.height / 2
 
        #make sure the camera doesn't see outside the map
        if new_x < 0: new_x = 0
        if new_y < 0: new_y = 0
        if new_x > MAP_WIDTH - self.width - 1: new_x = MAP_WIDTH - self.width
        if new_y > MAP_HEIGHT - self.height - 1: new_y = MAP_HEIGHT - self.height
 
        #if new_x != self.x or new_y != self.y: fov_recompute = True
 
        (self.x, self.y) = (new_x, new_y)

    def to_camera_coordinates(self, n_x, n_y):
        #convert coordinates on the map to coordinates on the screen
        (n_x, n_y) = (n_x - self.x, n_y - self.y)
 
        if (n_x < 0 or n_y < 0 or n_x >= self.width or n_y >= self.height):
            return (None, None)  #if it's outside the view, return nothing
 
        return (n_x, n_y)

