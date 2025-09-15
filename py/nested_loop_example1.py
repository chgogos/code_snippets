for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:2}", end=" ")
    print()
print("-" * 20)
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print(f"{i * j:2}", end=" ")
        j += 1
    print()
    i += 1
