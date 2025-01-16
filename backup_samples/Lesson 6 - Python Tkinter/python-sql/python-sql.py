import sqlite3

# establish a connection to the database
conn = sqlite3.connect('sample.db')

# create a cursor object
cursor = conn.cursor()

#execute SQL commands to create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS people (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                degree TEXT NOT NULL
                )''')

# commit the changes and close the connection
conn.commit()
conn.close()