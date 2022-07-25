import requests
from bs4 import BeautifulSoup

# r = requests.get("http://api.mp3quran.net/api/surah?surah=1&language=ru")
# r = requests.get("http://api.mp3quran.net/radios/radio_.json")

page = requests.get("https://namaz.today/city/andizhan")
data = BeautifulSoup(page.text, 'html.parser')
print(data)
