# Παραδοσιακή συνάρτηση
def square(x):
    return x**2


print(square(5))  # Έξοδος: 25
a = (lambda x: x**2)(5)
print(a)  # Έξοδος: 25
f = lambda x: x**2
print(f(5))  # Έξοδος: 25
