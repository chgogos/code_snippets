numbers = [3, 1, 4, 2]
numbers.sort() # ταξινομεί την ίδια την λίστα
print(numbers)  # [1, 2, 3, 4]

numbers = [3, 1, 4, 2]
print(sorted(numbers))  # [1, 2, 3, 4] 
print(numbers) # [3, 1, 4, 2]

words = ["apple", "banana", "kiwi"]
print(sorted(words, key=len))  # ['kiwi', 'apple', 'banana']
print(sorted(words, key=len, reverse=True))  # ['banana', 'apple', 'kiwi']
