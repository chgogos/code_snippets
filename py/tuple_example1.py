my_tuple = (1, "apple", 3.14, True)
print(my_tuple)  # (1, 'apple', 3.14, True)

another_tuple = 2, "banana", False
print(another_tuple)  # (2, 'banana', False)

print(1, 2)           # 1 2  => είναι δύο ξεχωριστά ορίσματα
print((1, 2))         # (1, 2) => είναι μία πλειάδα

print(my_tuple[0])    # 1
print(my_tuple[-1])   # True

my_tuple[1] = "orange" # TypeError