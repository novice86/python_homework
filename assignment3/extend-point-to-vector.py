from math import sqrt
# Task5

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if float(self.x) == float(other.x) and float(self.y) == float(other.y):
            return True
        
        return False
    
    def distance(self, another_point):
        return sqrt((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2)
    
    def __repr__(self):
        return f"Point({self.x!r}, {self.y!r})"


class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def __repr__(self):
        return f"Vector({self.x!r}, {self.y!r})"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y

        return Vector(x, y)


point1 = Point(1, 1)
print(point1)
point2 = Point(1, 1)
print(point2)
print(f"distance between point1 and point2: {point1.distance(point2)}")
print(point1 == point2)

v1 = Vector(1, 1)
v2 = Vector(1, 1)
print(v1)
print(v2)
v3 = v1 + v2
print(v3)

        