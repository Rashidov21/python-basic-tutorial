import math
import random
# Numbers 
# int , float, complex 

# round() # yaxlitlash 
# n = 12.923163 
# print(round(n,3)) # 12.923

# print(round(5.6)) # 6
# print(round(5.5)) # 6
# print(round(5.4)) # 5

# print(pow(2,2)) #4
# print(pow(2,3)) #8

# # -1 moduli 1
# print(abs(-1)) # 1
# print(min(1,2,3)) #1
# print(max(1,2,3)) #3

# print(sum([1,2,3,4,5,6])) # 6

# n = 10.0
# print(n.is_integer()) # True

# print(math.pi) # 3.14....

# print(random.random()) # 0 bilan 1 orasida son

# print(random.randint(1,10))
# s = 'python'
# a = [1,2,3,4,5]
# random.shuffle(a) # massiv elementlarini aralashtirish
# print(a)
# print(random.choice(s)) #tasodifiy element tanlash

# s = "lorem ipsum dolor"
# print(random.sample(s,5)) # alohida tasodifiy elementlar massivi

# task 1 
# user kiritgan son miqdorida har hil harf,son va maxsus belgilardan iborat parol generatsiya qiluvchi dastur tuzing

# letters = "qwertyuiopasdfghjklzxcvbnm"
# numbers = "0123456789"
# symbols = "!@#$%^&*()_"

# from_data = letters + numbers + symbols

# password = ""

# pass_len = int(input("Password length ?"))

# for i in range(pass_len):
#     password += random.choice(from_data)
# print(password)