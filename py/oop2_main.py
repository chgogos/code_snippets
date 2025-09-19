from oop2 import DigitalCounter

counter = DigitalCounter()
counter.set_max(5)
for _ in range(7):
    counter.increment()
    print(counter.count)  # Εκτυπώνει: 1, 2, 3, 4, 5, 0, 1
counter.clear()
print(counter.count)  # Εκτυπώνει: 0
