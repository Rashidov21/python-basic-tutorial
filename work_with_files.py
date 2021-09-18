# -*- coding: utf-8 -*-
# import os
# print(os.path)
# file = open("test.txt", "r") # 1 param file path , 2 param bu rejim (r,a,b,w)
# print(file.read())# file ni o'qish
# file.close() # file ni yopish
# print(os.path.abspath("test.txt")) # file ning absolute manzili

# import os , sys
# print(f"Fayl : {os.path.abspath(__file__)}")
# print(f"Katalog : {os.getcwd()}")
# print(f"Import uchun katalog : {sys.path[0]}")
# print(f"TXT Faylga olib boruvchi path : {os.path.abspath('test.txt')}")

# open("fayl yolini", "rejim")
# rejimlar:
# r - oqish
# r+ - oqish + yozish
# w - yozish
# w+ - oqish + yozish
# a - qoshish
# a+ - qoshish + oqish
# x - xosil qilish
# x+ - xosil qilish agar oldindan mavjud bosa FileExistsError kotarish
# num = 11
# print(f"Hello \n {num}")
# print(r"Hello \n \t")
# file =  open(r"test.txt", "r")
# print(file.read())
# file.close()

# with as  file ni as operatori orqali nomlab ochish va avtomatik yopish
# with open(r"test.txt", "r") as file:
#     print(file.read())

# import random as r
# print(r.randint(10,20))

# from bs4 import BeautifulSoup as bs # qayta nomlash
from faker import Faker
fake = Faker()
# for i in range(10):
#     n = fake.name()
#     a = fake.address()
#     print(f"name : {n} - address : {a}")

# with open(r"test.txt", "w+") as names:
#     for i in range(5):
#         name = fake.name()
#         # names.writelines(name) # yangi qator yozish
#         names.write(f"{name} \n")#shunchaki yangi qatordan yozish yozish
# f = open(r"test.txt", "r")
# print(f.readline())
# f.close()

# task 1
# faker orqali 300 ta ismni names.txt fayliga yozing
# va 300 tadan nechtasi John ekanini qaniqlang

# task 2
# Ushbu userlarni user.txt file sidan olib oqísh orqali qarzdorliklarni hisoblang
# Tanya:300
# Susan:123
# Thomas:89
# John:53
# Heather:12
# Michele:23
# Regina:233

# task 3
# 10 ta ism yosh va oylik maoshi berilgan user lardan tashkil topgan
# staffs dictini xosil qiling
# staffs dict:
#     staffs = [
#         {"name":"Michael", "age":23, "salary":15000}
#     ]
    # str:name
    # int:age
    # int:salary
# dictga ushbu malumotlar users.txt faylidan olib yozilsin
    # user.txt : Michael-23-150000