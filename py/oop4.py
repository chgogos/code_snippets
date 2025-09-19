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
s = set()

s.add(p1)
s.add(p2)  # δεν προστίθεται, γιατί p1 == p2
print(s)  # {Point(2, 3)}
