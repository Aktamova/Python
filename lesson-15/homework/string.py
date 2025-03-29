import sqlite3

values = (
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
)

with sqlite3.connect("hw15.db") as connection:
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE Roster(
        Name TEXT,
        Species TEXT,
        Age INT
        );"""
    )
cursor.executemany("INSERT INTO Roster VALUES(?, ?, ?);", values)

result = cursor.execute("Select * from Roster")
result.fetchall()


import sqlite3

with sqlite3.connect("hw15.db") as connection:
    cursor = connection.cursor()
    cursor.execute("""
    UPDATE Roster 
    SET Name = 'Ezri Dax' 
    WHERE Name = 'Jadzia Dax'
""")

result = cursor.execute("Select * from Roster")
result.fetchall()
import sqlite3

# Connect to the database
conn = sqlite3.connect("hw15.db")
cursor = conn.cursor()

# Select Name and Age of Bajorans
cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
rows = cursor.fetchall()

# Display results
result = cursor.execute("Select * from Roster")
result.fetchall()

# Close connection
conn.close()
