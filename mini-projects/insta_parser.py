import requests

url = 'https://www.instagram.com/rashidov_21/'
data = requests.get(url)
print(data.content)