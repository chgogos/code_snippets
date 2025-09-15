def calculate_rectangle_area(length, width):
    return length * width


r1 = calculate_rectangle_area(10, 20) # positional ορίσματα
r2 = calculate_rectangle_area(length=10, width=20) # named ορίσματα
r3 = calculate_rectangle_area(width=20, length=10) # named ορίσματα
print(f"{r1=}, {r2=}, {r3=}")
