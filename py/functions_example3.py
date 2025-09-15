import math


def circle_properties(radius):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    diameter = 2 * radius
    return area, circumference, diameter


area, circum, diam = circle_properties(5)
print(f"Εμβαδόν: {area:.2f}, περίμετρος: {circum:.2f}, διάμετρος: {diam}")
