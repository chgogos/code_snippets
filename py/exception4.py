import math


class NegativeLogError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Logarithm undefined for x = {value}. x must be > 0.")

    def __str__(self):
        return (
            f"[NegativeLogError] Invalid input: {self.value}. Logarithm requires x > 0."
        )


def safe_log(x, base=10):
    if x <= 0:
        raise NegativeLogError(x)
    return math.log(x, base)


try:
    print(safe_log(100))  # log10(100) = 2
    print(safe_log(-5))  # Θα γίνει raise η προσαρμοσμένη εξαίρεση
except NegativeLogError as e:
    print("Εξαίρεση: ", e)  # χρήση του __str__
    print(
        "Η τιμή που προκάλεσε εξαίρεση ήταν: ", e.value
    )  # πρόσβαση στην αποθηκευμένη πληροφορία
