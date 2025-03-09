import sqlite3
with sqlite3.connect("roster.db") as connection:
    cursor = connection.cursor()
    query1 = ('''CREATE TABLE IF NOT EXISTS Roster
            (
                Name TEXT,
                Species TEXT,
                Age INTEGER
            )
            ''')
    cursor.execute(query1)
    data = [
        ("Benjamin Sisko", "Human",	40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29)
    ]
    query2 = ('''INSERT INTO Roster (Name, Species, Age) VALUES (?,?,?)''')
    cursor.executemany(query2, data)
    connection.commit()

with sqlite3.connect("roster.db") as database:
    cursor = database.cursor()
    query3 = ('''UPDATE Roster SET Name = ? WHERE Name=?''')
    cursor.execute(query3, ("Ezri Dax", "Jadzia Dax"))
    connection.commit()

with sqlite3.connect("roster.db") as con:
    cursor = con.cursor()
    query4 = ('''SELECT Name, Age FROM Roster WHERE Species = ?''')
    cursor.execute(query4, ("Bajoran",))
    results = cursor.fetchall()
    for row in results:
        print(row)

with sqlite3.connect("roster.db") as con:
    cursor = con.cursor()
    query5 = ('''DELETE FROM Roster WHERE Age > 100''')
    cursor.execute(query5)
    connection.commit()

with sqlite3.connect("roster.db") as con:
    cursor = con.cursor()
    query6 = ('''ALTER TABLE Roster ADD COLUMN Rank TEXT DEFAULT "Unknown" ''')
    cursor.execute(query6)
    connection.commit()

with sqlite3.connect("roster.db") as con:
    cursor = con.cursor()
    query7 = ('''INSERT INTO Roster (Name, Species, Age, Rank) VALUES (?,?,?,?)''')
    query8 = ('''UPDATE Roster SET Rank = ? WHERE Name = ?''')
    cursor.execute(query7, ("Ezri Dax", "Trill", 300, "Lieutenant"))
    cursor.executemany(query8, [("Captain", "Benjamin Sisko"), ("Major","Kira Nerys")])

with sqlite3.connect("roster.db") as con:
    cursor = con.cursor()
    query10 = ('''SELECT * FROM Roster ORDER BY Age DESC''')
    cursor.execute(query10)
    results = cursor.fetchall()
    for row in results:
        print(row)
        