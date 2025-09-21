import csv

fn = "Google_Stock_Train (2010-2022).csv"
with open(fn, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    max_diff, max_row = -1, None
    for row in reader:
        low = float(row["Low"])
        high = float(row["High"])
        diff = high - low
        if diff > max_diff:
            max_diff = diff
            max_row = row
print(f"Μέγιστη διακύμανση: {max_diff:.2f}")
print(f"Ημερομηνία:  {max_row['Date']}")
