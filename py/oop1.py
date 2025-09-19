class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


r1 = Rectangle(4, 5)
print(f"Rectangle 1: {r1.width}x{r1.height}, area = {r1.area()}")
r2 = Rectangle(2, 7)
print(f"Rectangle 2: {r2.width}x{r2.height}, area = {r2.area()}")
