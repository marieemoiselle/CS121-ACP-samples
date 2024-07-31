# Import the SQLite library
import sqlite3

# Create a connection to the database (if the database does not exist, it will be created)
connection = sqlite3.connect('test.db')

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        degree TEXT NOT NULL
    )
''')

# Commit the changes
connection.commit()

# Function to clear the table
def clear_table():
    cursor.execute('DELETE FROM users')
    connection.commit()

# Insert a new user into the database
def insert_user(name, age, degree):
    cursor.execute('INSERT INTO users (name, age, degree) VALUES (?, ?, ?)', (name, age, degree))
    connection.commit()

# Update a user's information in the database
def update_user(id, name, age, degree):
    cursor.execute('UPDATE users SET name=?, age=?, degree=? WHERE id=?', (name, age, degree, id))
    connection.commit()

# Delete a user from the database
def delete_user(id):
    cursor.execute('DELETE FROM users WHERE id=?', (id,))
    connection.commit()

# Retrieve all users from the database
def get_all_users():
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()

# Execute SQL queries directly
def execute_sql_query(query):
    cursor.execute(query)
    connection.commit()

# Example usage

# Clear the table before inserting new data
clear_table()

# Insert a new user
insert_user('Luna Valeria', 20, 'BS Architecture')

'''
# Fetch all users and print their information
users = get_all_users()
for user in users:
    print(f'User ID: {user[0]}, Name: {user[1]}, Age: {user[2]}, Degree: {user[3]}')
'''

# Update a user's information
update_user(1, 'Luna Martinez', 25, 'BS Architecture')

# Delete a user with ID 1
# delete_user(1)

# Insert users using direct SQL queries
execute_sql_query("INSERT INTO users (name, age, degree) VALUES ('Samantha Vera', 29, 'BA Communication')")
execute_sql_query("INSERT INTO users (name, age, degree) VALUES ('Clyden Ramirez', 32, 'BS Biology')")

# Fetch all users and print their information
users = get_all_users()
for user in users:
    print(f'User ID: {user[0]}, Name: {user[1]}, Age: {user[2]}, Degree: {user[3]}')

# Close the connection
connection.close()
