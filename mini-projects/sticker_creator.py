import requests
from bs4 import BeautifulSoup
import urllib.request

url = 'https://demonpress.ecwid.com/%D0%9F%D0%BB%D0%B0%D0%BA%D0%B0%D1%82%D1%8B-c26701164'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
text = requests.get(url, headers=headers)
soup = BeautifulSoup(text.content, 'html.parser')
urls = []

# get links to high res pics from the first page
for i in soup.find_all('a', attrs = {"class": "grid-product__image"}):
	urls += [i['href']]

# parse links from other pages
for i in ['15','30','45']:
	url_next = url + '?offset=' + i
	text = requests.get(url_next, headers=headers)
	soup = BeautifulSoup(text.content, 'html.parser')
	for i in soup.find_all('a', attrs = {"class": "grid-product__image"}):
		urls += [i['href']]

# download pics to the cwd
for url in urls:
	text = requests.get(url, headers=headers)
	soup = BeautifulSoup(text.content, 'html.parser')
	if len(soup.find_all('img', {'class':'details-gallery__picture details-gallery__photoswipe-index-0'})) == 0:
		print(url)
	for j in soup.find_all('img', {'class':'details-gallery__picture details-gallery__photoswipe-index-0'}):
		urllib.request.urlretrieve(j['src'], j['title'].replace('/','').replace('*','').replace('?','')+'.jpg')