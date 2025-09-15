def factorial(n):
    if n == 0:
        return 1  # Βασική περίπτωση
    else:
        return n * factorial(n - 1)  # Αναδρομική περίπτωση


print(factorial(5))
print(factorial(10))
print(factorial(20))
