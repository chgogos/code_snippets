import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_area(cls, area):
        radius = math.sqrt(area / math.pi)
        return cls(radius)

    def area(self) -> float:
        return math.pi * (self.radius**2)


c1 = Circle(5)
c2 = Circle.from_area(78.54)

print(f"c1: {c1.radius:.2f}, area: {c1.area():.2f}")
print(f"c2: {c2.radius:.2f}, area: {c2.area():.2f}")
