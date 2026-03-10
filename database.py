import sqlite3
from auth import hash_func

def create_db():
    con = sqlite3.connect("jwt.db")

    cursor = con.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                password TEXT NOT NULL
                )
            ''')
            
    con.close()

def create_user(username, password):

    npassword = hash_func(password)

    con = sqlite3.connect("jwt.db")

    cursor = con.cursor()

    cursor.execute('''INSERT INTO users (name, password)
                    VALUES (?, ?)''', (username, npassword))

    con.commit()
    con.close()

def get_user(username):

    con = sqlite3.connect("jwt.db")

    cursor = con.cursor()

    cursor.execute('''SELECT * FROM users WHERE name = ?''', (username,))
    result = cursor.fetchall()

    con.close()

    return result
