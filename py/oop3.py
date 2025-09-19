class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    
p1 = Point(2, 3)
p2 = Point(2, 3)
print(p1)        # Point(2, 3)
print(p1 == p2)  # True 