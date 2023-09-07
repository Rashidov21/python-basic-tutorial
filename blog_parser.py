import sqlite3
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

url = "https://www.transfermarkt.com/sommertransfers/saisontransfers/statistik?transferfenster=sommertransfers&saison_id=2023"
soup = BeautifulSoup(requests.get(url, headers=HEADERS).text, "html.parser")
print(soup)
print(soup.find("table", class_="items"))



# url = "https://pyblog.uz/"
# pagination = "?page="

# conn = sqlite3.connect("some_data.db", check_same_thread=False)
# cur = conn.cursor()

# query = """SELECT * FROM titles WHERE title LIKE '%Python%' OR title LIKE '%python%'"""
# data = cur.execute(query)
# print(data.fetchall())

# soup = BeautifulSoup(requests.get(url).text, "html.parser")
# for i in range(1,18):
#     soup = BeautifulSoup(requests.get(url + pagination + str(i)).text, "html.parser")
#     for div in soup.findAll("div", class_="is-size-4"):
#         title = div.find("a").text.strip()
                
#         sql = f"""INSERT INTO titles
#             VALUES("{title}");"""
#         try:
#             cur.execute(sql)
#         except sqlite3.DatabaseError as e:
#             print(e)
#         else:
#             conn.commit() 


