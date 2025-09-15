import random			
lucky_number = random.randint(1,100) 
print("The lucky number was generated!")

winner = False
c = 0
for i in range(6):
    c += 1
    x = int(input(f"Guess the number (try {c}): "))
    if x == lucky_number:
        winner = True
        break
    elif x < lucky_number:
        print("Too low")
    else:
        print("Too high")

if winner:
    print(f"Winner at try {c}!")
else: 
    print(f"Looser, the lucky number was {lucky_number}!")
