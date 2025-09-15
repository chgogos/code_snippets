from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

# map: υπολογισμός τετραγώνου κάθε τιμής
squared = list(map(lambda x: x**2, nums))
print("Τετράγωνα:", squared)  # [1, 4, 9, 16, 25, 36]

# filter: διατήρηση μόνο των περιττών τιμών
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Άρτιοι αριθμοί:", evens)  # [2, 4, 6]

# reduce: άθροιση των τιμών
total = reduce(lambda x, y: x + y, evens)
print("Σύνολο:", total)  # 12

