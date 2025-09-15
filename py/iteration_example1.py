numbers = [10, 20, 30, 40]

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

print("-" * 20)

for num in numbers:
    print(num)

print("-" * 20)

for index, num in enumerate(numbers):
    print(f"Index {index}: {num}")
