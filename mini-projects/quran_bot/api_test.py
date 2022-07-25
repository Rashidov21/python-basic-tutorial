import requests
from bs4 import BeautifulSoup
import locale
locale.setlocale(locale.LC_ALL, "RU_ru")
# r = requests.get("http://api.mp3quran.net/api/surah?surah=1&language=ru")
# r = requests.get("http://api.mp3quran.net/radios/radio_.json")
headers = {
    "User Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
page = requests.get("https://shosh.uz/uz/namoz-vaqtlari-toshkent/")
data = BeautifulSoup(page.text, 'html.parser')
table = data.find(
    "table", {'class': 'tablepress tablepress-id-161'})

# l = [x for x in table.findAll("tr")]
body = table.find("tbody")
print([x.text for x in body.findAll("tr")])
# for i in l:
#     print(i)
# namaz_names = [x.text for x in l[0].findAll("th")]
