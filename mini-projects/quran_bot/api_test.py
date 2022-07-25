import requests
from bs4 import BeautifulSoup

# r = requests.get("http://api.mp3quran.net/api/surah?surah=1&language=ru")
# r = requests.get("http://api.mp3quran.net/radios/radio_.json")
headers = {
    "User Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}
page = requests.get("https://namaz.today/city/andizhan", headers=headers)
data = BeautifulSoup(page.text, 'html.parser')
print(data)
