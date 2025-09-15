def sum_numbers(n):
    total = 0
    i = 1
    while i < n:  
        total += i
        i += 1
    return total

n = 5
result = sum_numbers(n)
print(f"Το άθροισμα των αριθμών από το 1 μέχρι και το {n} είναι: {result}")
