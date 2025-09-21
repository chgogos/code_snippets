def read_numbers_and_divide():
    while True:
        try:
            user_input = input("Εισάγετε 2 τιμές χωρισμένες με κενό: ").split()
            if len(user_input) != 2:
                raise ValueError("Παρακαλώ εισάγετε ακριβώς 2 τιμές.")
            a, b = map(float, user_input)  # μετατροπή σε float σε 1 εντολή
            return a / b

        except ValueError as e:
            print("Σφάλμα: ", e)
        except ZeroDivisionError:
            print("Σφάλμα: Η δεύτερη είσοδος δεν μπορεί να είναι μηδέν.")


quotient = read_numbers_and_divide()
print("Αποτέλεσμα: ", quotient)
