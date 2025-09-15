temp_sum, temp_count, temp_max = 0, 0, None

def add_temperature(temp):
    """Προσθέτει θερμοκρασία και ενημερώνει τις καθολικές μεταβλητές."""
    global temp_sum, temp_count, temp_max
    assert -30 <= temp <= 60, "Η θερμοκρασία πρέπει να είναι μεταξύ -30 και 60"
    temp_sum += temp
    temp_count += 1
    if temp_max is None or temp > temp_max:
        temp_max = temp

def average_temperature():
    """Επιστρέφει το μέσο όρο θερμοκρασιών."""
    assert temp_count > 0, "Δεν έχει καταγραφεί καμία θερμοκρασία"
    return temp_sum / temp_count

def max_temperature():
    """Επιστρέφει τη μέγιστη θερμοκρασία."""
    assert temp_count > 0, "Δεν έχει καταγραφεί καμία θερμοκρασία"
    return temp_max

# Προσθήκη θερμοκρασιών (έγκυρες)
add_temperature(20); add_temperature(25); add_temperature(18); add_temperature(30)
print("Μέσος όρος θερμοκρασιών:", average_temperature()) # 23.25
print("Μέγιστη θερμοκρασία:", max_temperature()) # 30
add_temperature(100)  # AssertionError
