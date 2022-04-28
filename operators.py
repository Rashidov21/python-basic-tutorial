import requests
from bs4 import BeautifulSoup
url = "https://www.pexels.com/ru-ru/search/python/"
headers = {
    "Accept-Language":"ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6,pt;q=0.5,uz;q=0.4",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"
}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, "html.parser")
print(soup.findAll("article", class_="photo-item"))
images = "sss"
for x in images:
    print(x)

#int , str , float, bool
# < , > , == , != , in ,not in, is,is not, and ,or ,
#print(10 > 5) # True
#print(10 >= 10) # True
#print(10 < 5) # False
#print(10 <= 5) # False
#print(10 == 10) # True
#print(10 != 10) # False
# s = 'salom'
# print('b' in s) # False
# print('s' in s) # True
# print('s' not in s) # False
# print('b' not in s) # True
# x = y = [1,2]
# print(x)
# print(y)
# print(x is y) #True aks holda False
# print(x is not y) # False
# x = 10
# y = [1,2]
# print(x and y) birinchi true ni ushedi
# print(x or y) birinchi false ni ushedi
# <, > ,<=, >= , == , != , is ,is not , in , not in, and , or
# Mantiqiy operatorlar >> not , and , or
