import sqlite3
from send_articles import sender
import time
def connect_to_db():
    con = sqlite3.connect("articles.db")
    return con
def send():
    con = connect_to_db()
    cur = con.cursor()
    sql = """\
        SELECT * FROM articles
    """
    try:
        data = cur.execute(sql)
        for x in data:
            t = f"{x[1]}"
            d = f"{x[2]}"
            sender(t,d)
            time.sleep(10)
    except sqlite3.DatabaseError as e:
        print(e)
    else:
        con.commit()
        cur.close()
        con.close()
send()
    # sender()
# con = sqlite3.connect("articles.db")
# cur = con.cursor()
# sql = """\
#     CREATE TABLE articles(
#          id INTEGER PRIMARY KEY AUTOINCREMENT,
#          title TEXT,
#          desc TEXT);
#     """
# cur.execute(sql)
# con.commit()
# cur.close()
# con.close()


