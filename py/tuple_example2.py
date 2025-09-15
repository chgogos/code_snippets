my_list = [1, 2, 3]
my_tuple = tuple(my_list) # Μετατροπή λίστας σε πλειάδα
print(my_tuple)  # (1, 2, 3)

new_list = list(my_tuple) # Μετατροπή πλειάδας σε λίστα
print(new_list)  # [1, 2, 3]

single_value = (5)      # απλή τιμή, δεν είναι πλειάδα
single_tuple = (5,)     # πλειάδα ενός στοιχείου
print(single_value)     # 5
print(single_tuple)     # (5,)
print(type(single_value))  # <class 'int'>
print(type(single_tuple))  # <class 'tuple'>
