import sys
from math import sqrt

while True:
    x = input("Εισάγετε έναν αριθμό (-99 για έξοδο): ")
    if x == "-99":
        break
    try:
        r = sqrt(float(x))
        print(f"Η τετραγωνική ρίζα του {x} είναι {r}")
    except ValueError as e:
        sys.stderr.write(f"Σφάλμα: {e} - είσοδος: {x}\n")
        print("Παρακαλώ εισάγετε έναν μη αρνητικό αριθμό.")
    except TypeError as e:
        sys.stderr.write(f"Σφάλμα: {e} - είσοδος: {x}\n")
        print("Παρακαλώ εισάγετε έναν έγκυρο αριθμό.")
