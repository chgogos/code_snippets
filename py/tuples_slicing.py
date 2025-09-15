nested = (1, (2, 3), (4, 5, 6), 7)

print(nested[0])        # 1
print(nested[1])        # (2, 3)
print(nested[1][0])     # 2  => πρόσβαση σε στοιχείο του nested tuple

print(nested[1:3])      # ((2, 3), (4, 5, 6))
print(nested[:2])       # (1, (2, 3))
print(nested[::2])      # (1, (4, 5, 6)) => κάθε δεύτερο στοιχείο

# Slicing μέσα σε nested tuple
print(nested[2][1:])    # (5, 6)
