import requests

r = requests.get("https://api.mp3quran.net/api/translations?languages=ru")
print(r.json())
