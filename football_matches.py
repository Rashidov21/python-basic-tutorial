# pip install requests
# pip install bs4
import sqlite3
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
url = "https://qalampir.uz/"
page = requests.get(url, headers=HEADERS)
# print(page.status_code)
soup = BeautifulSoup(page.text, "html.parser")

matches = [match for match in soup.findAll("div", class_="news-card")]
news = []
for i in matches:
    i = i.find("a", class_="news-card-content-text")
    print(type(i.text))
    print(url + i["href"])
    # news.append(
    #     {
    #         "title":i.text,
    #         "url":url + i["href"]
    #     }
    # )
# print(news)

# for x in news:
#     print(x)
