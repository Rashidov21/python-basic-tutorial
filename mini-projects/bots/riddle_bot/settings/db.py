import sqlite3
import os


def connect_db():
    print(os.getcwd())
    conn = sqlite3.connect('./settings/users.db')
    return conn


# sql = """CREATE TABLE users(
#     user_id INT PRIMARY KEY,
#     phone TEXT,
#     location TEXT);"""

# try:
#     conn = connect_db()
#     cur = conn.cursor()
#     cur.execute(sql)
# except sqlite3.DatabaseError as e:
#     print(e)
# else:
#     print("TABLE has ben created !")
