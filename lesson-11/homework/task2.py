import sqlite3
with sqlite3.connect("library.db") as connection:
    cursor = connection.cursor()
    query1 = (''' CREATE TABLE IF NOT EXISTS Books
              (
              Title TEXT,
              Author TEXT,
              Year_published INTEGER,
              Genre TEXT
              )
                ''')
    cursor.execute(query1)

with sqlite3.connect("library.db") as con:
    data = [
        ("To Kill a Mockingbird", "Harper Lee",	1960, "Fiction"),
        ("1984", "George Orwell", 1949, "Dystopian"),
        ("The Great Gatsby", "F. Scott Fitzgerald",	1925, "Classic")
    ]
    cursor = con.cursor()
    query2 = ('''INSERT INTO Books (Title, Author, Year_published, Genre) VALUES(?,?,?,?)''')
    #cursor.executemany(query2, data)
    connection.commit()

with sqlite3.connect("library.db") as con:
    cursor = con.cursor()
    query3 = ('''UPDATE Books SET Year_published = ? WHERE Title = ?''')
    #cursor.execute(query3, (1950, "1984"))

with sqlite3.connect("library.db") as con:
    cursor = con.cursor()
    query4 = ('''SELECT Title, Author FROM Books WHERE Genre = ?''')
    cursor.execute(query4, ("Dystopian",))
    results = cursor.fetchall()
    for row in results:
        #print(row)
        pass

with sqlite3.connect("library.db") as con:
    cursor = con.cursor()
    query5 = ('''DELETE FROM Books WHERE Year_published < ?''')
    #cursor.execute(query5, ("1950",))
    con.commit()

with sqlite3.connect("library.db") as con:
    cursor = con.cursor()
    query6 = ('''ALTER TABLE Books ADD COLUMN RATING FLOAT DEFAULT Null''')
    #cursor.execute(query6)

with sqlite3.connect("library.db") as con:
    cursor = con.cursor()
    query7 = ('''INSERT INTO Books (Title, Author, Year_published, Genre, Rating) VALUES(?,?,?,?,?)''')
    #cursor.execute(query7, ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic", "Null"))
    connection.commit()
 
with sqlite3.connect("library.db") as con:
    updt_data = [
        (4.8, "To Kill a Mockingbird"),
        (4.7, "1984"),
        (4.5, "The Great Gatsby")
    ]
    cursor = con.cursor()
    query8 = ('''UPDATE Books SET Rating = ? WHERE Title = ?''')
    #cursor.executemany(query8, updt_data)
    con.commit()

with sqlite3.connect("library.db") as con:
    cursor = con.cursor()
    query9 = ('''SELECT * FROM Books ORDER BY Rating ASC''')
    cursor.execute(query9)
    sorted_results = cursor.fetchall()
    for row in sorted_results:
        print(row)