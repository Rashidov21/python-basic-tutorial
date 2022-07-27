import sqlite3
conn = sqlite3.connect('main.db')
cur = conn.cursor()

sql = """CREATE TABLE puzzels(
    puzzle_id INT PRIMARY KEY,
    text TEXT,
    answer TEXT);"""

try:
    cur.execute(sql)
except sqlite3.DatabaseError as e:
    print(e)
else:
    print("DB has ben created !")
