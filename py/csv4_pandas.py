import pandas as pd

fn = "Google_Stock_Train (2010-2022).csv"
df = pd.read_csv(fn)
df["Range"] = df["High"] - df["Low"]
max_row = df.loc[df["Range"].idxmax()]

print(f"Μέγιστη διακύμανση: {max_row['Range']:.2f}")
print(f"Ημερομηνία: {max_row['Date']}")
