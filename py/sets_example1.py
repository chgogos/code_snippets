s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(f"{s1=}")
print(f"{s2=}")
print("Ένωση:", s1.union(s2)) # {1, 2, 3, 4, 5, 6}
print("Τομή:", s1.intersection(s2)) # {3, 4}
print("Διαφορά s1 - s2:", s1.difference(s2)) # {1, 2}
print("Διαφορά s2 - s1:", s2.difference(s1)) # {5, 6}
print("Συμμετρική διαφορά:", s1.symmetric_difference(s2)) # {1, 2, 5, 6}
