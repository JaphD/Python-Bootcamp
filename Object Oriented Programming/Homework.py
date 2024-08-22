# Problem 1
class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1, x2, y2 = 0, 0, 0, 0
        for i, coordinate in enumerate(self.coor1):
            if i == 0:
                x1 = coordinate
            else:
                y1 = coordinate
        for i, coordinate in enumerate(self.coor2):
            if i == 0:
                x2 = coordinate
            else:
                y2 = coordinate

        print(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)

    def slope(self):
        x1, y1, x2, y2 = 0, 0, 0, 0
        for i, coordinate in enumerate(self.coor1):
            if i == 0:
                x1 = coordinate
            else:
                y1 = coordinate
        for i, coordinate in enumerate(self.coor2):
            if i == 0:
                x2 = coordinate
            else:
                y2 = coordinate
        print((y2 - y1) / (x2 - x1))


coor1 = (3, 2)
coor2 = (8, 10)

li = Line(coor1, coor2)

li.distance()

li.slope()

'''
A better alternative would be the following for problem one
    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        
        print(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)

    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        
        print((y2 - y1) / (x2 - x1))   
'''
print("\n")


# Problem 2
class Cylinder:
    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        print(Cylinder.pi * self.radius ** 2 * self.height)

    def surface_area(self):
        print((2 * Cylinder.pi * self.radius ** 2) + 2 * Cylinder.pi * self.radius * self.height)


c = Cylinder(2, 3)

c.volume()

c.surface_area()
