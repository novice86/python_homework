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
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"


class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y

        return Vector(x, y)


print("--- Demonstrating Point ---")
point1 = Point(1, 2)
point2 = Point(4, 6)
point3 = Point(1, 2)

print(f"Point 1: {point1}")
print(f"Point 2: {point2}")
print(f"Point 3: {point3}")

print(f"\nDistance between Point 1 and Point 2: {point1.distance(point2)}")
print(f"Equality (Point 1 == Point 2): {point1 == point2}")
print(f"Equality (Point 1 == Point 3): {point1 == point3}") 

print("\n--- Demonstrating Vector ---")
v1 = Vector(2, 3)
v2 = Vector(4, 1)

print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")
print(f"Vector Addition (v1 + v2): {v1 + v2}")

        