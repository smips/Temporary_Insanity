import random

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle(object):

    def __init__(self, pt1, width, height):
        self.pt1 = pt1
        self.pt2 = Point(pt1.x + width, pt1.y + height)
        self.center = Point(pt1.x + (width/2), pt1.y + (height/2))
        self.width = width
        self.height = height

    def get_points(self):
        #returns a list of XY coordinates in the rectangle
        pts = []
        for x in range(self.width):
            for y in range(self.height):
                pts.append(Point(self.pt1.x + x, self.pt1.y + y))
        return pts

    def intersects(self, rect):
        return (self.pt1.x <= rect.pt2.x and self.pt2.x >= rect.pt1.x and
                self.pt1.y <= rect.pt2.y and self.pt2.y >= rect.pt1.y)


class Line(object):

    def __init__(self, pt1, pt2):
        self.pt1 = pt1
        self.pt2 = pt2


def get_random_point(min_x, max_x, min_y, max_y):
    return Point(random.randint(min_x, max_x), random.randint(min_y, max_y))

def create_h_tunnel(x1, x2, y):
    pts = []
    #horizontal tunnel. min() and max() are used in case x1>x2
    for x in range(min(x1, x2), max(x1, x2) + 1):
        pts.append(Point(x, y))
    return pts
 
def create_v_tunnel(y1, y2, x):
    pts = []
    #vertical tunnel
    for y in range(min(y1, y2), max(y1, y2) + 1):
        pts.append(Point(x, y))
    return pts