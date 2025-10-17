class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor


double = Multiplier(2)
triple = Multiplier(3)

print(double(5))  # 10
print(double(100))  # 200
print(triple(5))  # 15
print(triple(100))  # 300
