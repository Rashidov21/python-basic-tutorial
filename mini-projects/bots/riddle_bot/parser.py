# pip install bs4
import requests
import sqlite3
from bs4 import BeautifulSoup as bs


url = "http://ertak.uz/puzz/68"
page = requests.get(url)

data = None

if page.status_code == 200:
    data = bs(page.text, "html.parser")
else:
    raise Exception("Conntection failed ...")


def get_puzzels_and_save():
    puzzles = data.findAll("p")
    to_render = []
    for i in puzzles:
        to_render.append(i.text)
    to_render.pop()
    conn = sqlite3.connect('./settings/main.db')
    cur = conn.cursor()
    i = 82
    for puzzle in to_render:
        i += 1
        sql = f"""INSERT INTO puzzels(puzzle_id,text,answer)
            VALUES({i},'{puzzle.split('.')[0]}','{puzzle.split('.')[1].lower()}');"""
        try:
            cur.execute(sql)
        except Exception as e:
            print(e)
        else:
            conn.commit()
    conn.close()
    print("OK")


# print(len(to_render))
get_puzzels_and_save()

# conn = sqlite3.connect('./settings/main.db')
# cur = conn.cursor()
# d = cur.execute("SELECT * FROM puzzels")
# print(d.fetchall())
