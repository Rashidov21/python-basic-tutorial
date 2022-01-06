from bs4 import BeautifulSoup
import requests

HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}


url = "https://tproger.ru/"
page = requests.get(url,headers=HEADER)
soup = BeautifulSoup(page.text, "html.parser")
content = soup.findAll("div", class_="article__container-text")
obj = []
for x in content:
    title = x.find("a",class_='article__link')
    desc = x.find("p", class_='article__excerpt article__excerpt--icon')
    obj.append({"title":title.text, "desc":desc.text})
# for x in obj:
#     con = connect_to_db()
#     cur = con.cursor()
#     sql = f"""\
#             INSERT INTO articles(title, desc)
#              VALUES('{x["title"]}','{x["desc"]}');
#         """
#     try:
#         cur.execute(sql)
#     except sqlite3.DatabaseError as e:
#         print("ERROR", e)
#     else:
#         con.commit()
#         print("OK\n" * 5)

# titles = soup.findAll("a", class_='article__link')
# for i in titles:
#     print(i)
# print(len(titles))