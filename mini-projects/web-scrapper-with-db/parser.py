from bs4 import BeautifulSoup
import requests
import json
HEADER = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}


url = "https://socratify.net/quotes/best"
page = requests.get(url,headers=HEADER)
soup = BeautifulSoup(page.text, "html.parser")
content = soup.findAll("div", class_="b-list-quote2__item")
# quotes = content.findAll("div", class_="b-list-quote2__item ")
obj = []

for x in content:
    title = x.find("a",class_='b-list-quote2__item-text js-quote-text').text
    author = x.find("div", class_="b-list-quote2__item-category").a.text
    item = {
        "title":title.strip(),
        "author": author.strip()
    }
    obj.append(item)

