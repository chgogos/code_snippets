pairs = [(1, 3), (2, 2), (0, 5), (4, 1)]

# Ταξινόμηση με βάση το άθροισμα των στοιχείων κάθε ζεύγους
pairs_sorted = sorted(pairs, key=lambda pair: pair[0] + pair[1])

print(pairs_sorted) # [(1, 3), (2, 2), (0, 5), (4, 1)]
