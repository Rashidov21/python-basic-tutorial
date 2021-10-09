#-*- coding: utf-8 -*-
import sqlite3
con = sqlite3.connect("users.db")
cur = con.cursor()
sql = """\
    CREATE TABLE users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        password TEXT
        );
    """
try:
    cur.execute(sql)
except sqlite3.DatabaseError as err:
    print("Error", err)
else:
    print("Congrats! user.db created and created users TABLE.")
try:
    sql = """\
        INSERT INTO users (email, password)
        VALUES ("yoki@meme.ru","qwerty")
    """
    cur.execute(sql)
except sqlite3.DatabaseError as err:
    print(err)
else:
    print("Created a new user data into users.db TABLE users")
cur.close()
con.close()
input()
