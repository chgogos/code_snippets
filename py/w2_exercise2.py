def evens_max(*args):
    """Επιστρέφει τη μέγιστη τιμή από τα άρτια ορίσματα ή -1 αν δεν υπάρχει."""
    max_even = None  
    for x in args:
        if x % 2 == 0:           
            if max_even is None: 
                max_even = x
            elif x > max_even:   
                max_even = x

    if max_even is None:
        return -1
    else:
        return max_even


print(evens_max(1, 2, 3, 4, 5))        # 4
print(evens_max(-10, -20, -30, -40))   # -10
print(evens_max(1, 3, 5, 7, 9))        # -1
