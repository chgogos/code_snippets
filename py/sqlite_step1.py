import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()
print("Η Βάση Δεδομένων δημιουργήθηκε και συνδέθηκε.")
conn.close()
