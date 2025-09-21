def repeat_text(text, times):
    if not isinstance(times, int):
        raise TypeError("times must be an integer.")
    if times < 0:
        raise ValueError("times must be non-negative.")
    return text * times


try:
    text, times = input("Δώσε κείμενο και επαναλήψεις: ").split()
    times = int(times)
    result = repeat_text(text, times)
    print("Αποτέλεσμα: ", result)
except TypeError as e:
    print("TypeError:", e)
except ValueError as e:
    print("ValueError:", e)
