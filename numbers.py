import math  # matematik amallar uchun kerak
import random  # tasodifiy son, qiymat, element uchun kerak

# Numbers
# int
# float
# complex
# n = 1
# f = 1.2
# c = 2n

# print(round(1.3))#1
# print(round(1.8))#2

# print(math.pi)
# print(dir(math))


# round() , sum() , abs(),bin(), max(), min()
# print(bin(20)) # binar songa aylantirish
# print(max(2,5,6,8)) # 8
# print(min(2,5,6,8)) # 2
# print(round(2.3)) # 2
# print(sum([1,2,3])) # 6
# print(sum(range(1, 11))) # 55
# print(abs(-2)) # 2

# n = 10 * 2 - (sum(range(1, 5)) / abs(-2))
# print(int(n))

# print(random)
# print(math)

# PI = math.pi  # 3.14 ...
# print(math.ceil(PI))  # 4 - tepaga qarab yaxlitlash
# print(math.floor(PI))  # 3 - pastga qarab yaxlitlash
# print(math.sqrt(100)) # 10.0
# print(math.pow(2,2)) # 4
# print(math.pow(2,10)) # 1024
# print(math.factorial(10)) # 3628800

# RANDOM
# print(random.random())  # ~ 0.464341140569114
# print(random.randint(10, 50)) # diapazondagi bitta tasodify butun son
# print(random.randrange(10, 50, 2)) # range() ni anlogi (bir xil)
# l = [1, 2, 3, 4, 5]
# print(random.choice(l))  # tasodifiy bitta elem tanlash
# random.shuffle(l) # massiv elementlarini index larini tasodify almashtiradi
# print(l)
# s = "python"
# siz korsatgan ketmaketlikdan siz korsatgan miqdorda elem tasodify elem qaytaradi
# print(random.sample(s, 2))

# letters = "qwertyuiopasdfghjklzxcvbnm!@#$%^&*()"

# password_length = int(input("Password lenght ? "))
# password = ""
# for i in range(password_length):
#     if i % 2 == 0:
#         letter = random.choice(letters).upper()
#     else:
#         letter = random.choice(letters).lower()
#     password += letter

# print(password)
