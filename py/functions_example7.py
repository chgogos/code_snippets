def calculate_interest(principal, rate=0.05, time=1, compound_frequency=1):
    amount = principal * (1 + rate / compound_frequency) ** (compound_frequency * time)
    interest = amount - principal
    return round(interest, 2)


# default τιμές: επιτόκιο 5%, 1 έτος, ετήσια εφαρμογή επιτοκίου
interest1 = calculate_interest(1000)
print(f"Τόκοι: {interest1}€")

# Προσαρμοσμένες τιμές: επιτόκιο 8%, 2 έτη, ετήσια εφαρμογή επιτοκίου
interest2 = calculate_interest(1000, rate=0.08, time=2)
print(f"Τόκοι: {interest2}€")

# Προσαρμοσμένες τιμές: επιτόκιο 6%, 5 έτη, μηνιαίος ανατοκισμός
interest3 = calculate_interest(1000, rate=0.06, time=5, compound_frequency=12)
print(f"Τόκοι: {interest3}€")
