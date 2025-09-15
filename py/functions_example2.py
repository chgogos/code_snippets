# Ορισμός συνάρτησης με 1 παράμετρο
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Κλήσεις συνάρτησης  
temp1 = celsius_to_fahrenheit(0)      # Όρισμα: 0
temp2 = celsius_to_fahrenheit(100)    # Όρισμα: 100

print(f"0°C = {temp1}°F")
print(f"100°C = {temp2}°F")
