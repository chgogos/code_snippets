def average_positive(numbers):
    """Υπολογίζει το μέσο όρο των θετικών αριθμών στη λίστα."""
    positives = [num for num in numbers if num > 0]
    return sum(positives) / len(positives)


alist = []
while True:
    try:
        x = input("Εισήγαγε έναν αριθμό (κενό για τερματισμό): ")
        if x == "":
            break
        x = float(x)
        alist.append(x)
    except ValueError:
        print("Εισήχθει μη αριθμητική τιμή, προσπαθήστε ξανά")

try:
    avg = average_positive(alist)
    print(f"Μέσος όρος θετικών αριθμών: {avg}")
except ZeroDivisionError:
    print("Δεν εισήχθησαν θετικοί αριθμοί.")
