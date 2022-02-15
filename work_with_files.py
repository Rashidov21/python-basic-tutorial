# -*- coding: utf-8 -*-
import os

# print(os.path) # python install directory
# file = open("test.txt", "a")
# 1 param file path , 2 param bu rejim (r,a,b,w)
# print(dir(file))
# file.write("\npython or ruby")
# print(file.read())  # file ni o'qish
# file.close()  # file ni yopish
# print(os.path.abspath("tasks.py"))  # file ning absolute manzili

# import os , sys
# print(f"Fayl : {os.path.abspath(__file__)}")
# print(f"Katalog : {os.getcwd()}")
# print(f"Import uchun katalog : {sys.path[0]}")
# print(f"Faylga olib boruvchi path : {os.path.abspath(__file__)}")

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
# file = open("test.txt", "r+")
# print(file.read())
# print(file.readlines())
# file.write("str")
# file.writelines("str")
# fr = file.read()
# print(fr)
# file.close()

# f = open("test.txt", "r")
# # print(f.readlines()) # list lines
# s = 0
# for i in f.readlines():
#     # John - 30
#     s += int(i.split("-")[1])
# print(s)

# from math import pi as pi_soni
# print(pi_soni)

# with as : file ni as operatori orqali nomlab ochish va avtomatik yopish
# with open(r"test.txt", "r") as file:
#     print(file.read())

# task 1
# 1 , 100 >> 30 to nums.txt file write
# from random import randint
# for i in range(30):
#     rn = randint(1,100)
#     with open("test.txt", "a") as file:
#         file.writelines(f"{rn}\n")


# import random as r
# print(r.randint(10,20))

# from bs4 import BeautifulSoup as bs # qayta nomlash

# pip install faker
# from faker import Faker
# fake = Faker()
# # print(dir(fake))
#
# with open("menifaylim.txt", "r+") as file:
#     for i in range(10):
#         n = fake.name()
#         a = fake.address()
#         file.writelines(f"name : {n} - address : {a} \n")
# with open("menifaylim.txt", "r") as f:
#     print(f.read())


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
