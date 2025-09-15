my_set = {1, 2, 3}
print("Αρχικό σύνολο:", my_set)  # {1, 2, 3}

my_set.add(4)
my_set.add(2)  # ήδη υπάρχει, δεν αλλάζει τίποτα
print("Με add:", my_set)        # {1, 2, 3, 4}

# update(): προσθήκη πολλαπλών στοιχείων από λίστα/tuple/set
my_set.update([5, 6], (7, 8), {1, 9})
print("Με update:", my_set)     # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# discard(): διαγραφή στοιχείου, χωρίς σφάλμα αν δεν υπάρχει
my_set.discard(3)
my_set.discard(100)             # δεν υπάρχει, δεν προκαλεί σφάλμα
print("Με discard:", my_set)    # {1, 2, 4, 5, 6, 7, 8, 9}

# remove(): διαγραφή στοιχείου, σφάλμα αν δεν υπάρχει
my_set.remove(2)
print("Με remove:", my_set)     # {1, 4, 5, 6, 7, 8, 9}
my_set.remove(100)  # KeyError
