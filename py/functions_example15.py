def divide(a, b):
    """
    Διαίρεση δύο αριθμών, διασφαλίζοντας ότι ο διαιρέτης δεν είναι μηδέν.
    """
    assert b != 0, "Denominator must not be zero!"
    return a / b


print(divide(10, 2))
print(divide(5, 0))
