import sqlite3
import time
import random

conn = sqlite3.connect("temperature.db")
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS Measurements")
c.execute("""
CREATE TABLE Measurements (
    id INTEGER PRIMARY KEY,
    timestamp TEXT,
    temperature REAL
)
""")
conn.commit()
for _ in range(20):
    temp = round(random.uniform(20, 30), 2)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO Measurements (timestamp, temperature) VALUES (?, ?)", (timestamp, temp))
    print(f"Εισαγωγή μέτρησης: {timestamp}, {temp} °C")
    conn.commit()
    time.sleep(0.2)  # μικρή καθυστέρηση για προσομοίωση
c.execute("SELECT AVG(temperature) FROM Measurements")
avg_temp = c.fetchone()[0]
print(f"Μέση θερμοκρασία: {avg_temp:.2f} °C")
conn.close()
