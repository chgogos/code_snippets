def evens_max(*args):
    """Επιστρέφει τη μέγιστη τιμή από τα άρτια ορίσματα ή -1 αν δεν υπάρχει."""
    try:
        return max(x for x in args if x % 2 == 0)
    except ValueError:
        return -1


print(evens_max(1, 2, 3, 4, 5))        # 4
print(evens_max(-10, -20, -30, -40))   # -10
print(evens_max(1, 3, 5, 7, 9))        # -1
