import requests

url = "https://forecast9.p.rapidapi.com/"

headers = {
    'x-rapidapi-host': "forecast9.p.rapidapi.com",
    'x-rapidapi-key': "0202709d4emshbe87778ed9b4962p1f76cdjsn4a200e532763"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)

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
