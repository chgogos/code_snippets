import re

text = """
Στο μάθημα αριθμητικής κάναμε τις παρακάτω πράξεις: 
5+7, 123-45, 9+15, 250-100, 12+88, 99-50, 7+8, 
300-150, 45+55, 200-75. Μετά κάναμε τις πράξεις 
101+21, 15+85 και κάναμε μια τελευταία αφαίρεση 
400-123 για επανάληψη.
"""

pattern = r"\b(\d{1,3})([+-])(\d{1,3})\b"

matches = re.findall(pattern, text)
for a, op, b in matches:
    a, b = int(a), int(b)
    result = a + b if op == "+" else a - b
    print(f"{a}{op}{b} = {result}")
