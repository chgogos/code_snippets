s = '12345'
print("Break")
for c in s:
    if c == '3':
        break
    print(c)

print("Continue")
for c in s:
    if c == '3':
        continue
    print(c)
