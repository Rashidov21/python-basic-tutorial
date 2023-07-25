import math 
import random

# Data type - ma'lumot turi
# str - String , qator - matn
# int - Integer , butun son 
# float - Float , qoldiqli son
# complex - qiyin , katta sonlar
# bool - Boolean , rost yoki yolgon qiymatlari
# None - None , mavjud emas qiymati


# name = "John"
# name = 'Mike'
# name = """David"""
# print(name) #David

# print('Men bugun olma "yedim".') # Men bugun olma "yedim".
# print("Hello\nWorld") # yangi qatordan
# print("Hello\tWorld") # Tab 4 ta bosh joy tashash
# print("Men bugun olma \"yedim\".") # Men bugun olma "yedim".

# a,b,c = 1,2,3
# print(a+b+c) #6 
# x = False
# print(type(x)) # <class 'bool'>
# x = 1
# print(type(x)) # <class 'int'>

# user = input("Son kirit") # userdan ma'lumot qabul qilish
# user = int(user) # stringni int qilish
# print(user + 2)
# # print(type(user))

# user = int(input("Son kiriting \n:"))
# print(user + 2)

# # Arifmetika 
# print(2 + 2) # 4
# print(2 - 2) # 0
# print(2 * 2) # 4
# print(4 / 2) # 2.0
# print(4 // 2) # 2
# print(2 ** 4) # 16
# print(7 % 3) # 1

# i = int("12")
# print(i + 12) # 24

# f = float(10)
# print(10 + f) # 20.0

# pow() , abs() , max(), min(), sum()
# print(pow(2,2)) # 4
# print(pow(2,10)) # 1024
# print(abs(-1)) # 1
# print(abs(-5)) # 5
# print(max(1,4,6,8)) # 8
# print(min(1,4,6,8)) # 1
# print(sum(range(4))) # 6

# module math 
# print(dir(math))  # dir barcha attr va methodlarini ro'yhati
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
# print(math.pi) # 3.141592653589793
# round() # qoldigi 5 dan katta bosa tepaga qarab aks holda pastga qarab yaxlitlash
# print(round(math.pi * 5)) # 16
# print(round(3.5)) # 4
# print(round(3.4)) # 3

# print(math.ceil(3.4)) # 4 - tepaga qarab yaxlitlash
# print(math.floor(3.6)) # 3 - pastga qarab yaxlitlash

# print(random.random()) # 0.3398516329302407

# r = random.randint(1,11) # random ineteger
# print(r)

# print(random.choice("python"))
# arr = [1,2,3,4,5]
# print(random.choice(arr)) # tasodify 1 ta elementni qaytaradi 

# print(random.sample(arr, 2)) # tasodify siz korsatgancha elementlarni qaytaradi

# task 1 
# userdan son qabul qiling (0 < n < 100) while orqali 100 ta takrorlanishda 0 dan 100 gacha bolgan sonlar tasodify olinadi va user kiritgan songa takrorlanishda kelgan sonlar necha marta mos kelganini hisoblaydigan dastur tuzing 

# n = int(input("N ?"))
# count = 0
# i = 0
# while i < 100:
#     i += 1 
#     r_num = random.randint(0,100)
#     # print(r_num)
#     if n == r_num:
#         count += 1
# print("Match : " , count)

# task 2 
# userdan paroldagi belgilar soni nechta bolishini sorang , shu miqdorqa katta harflar  sonlar va maxsus belgilardan iborat parol hosil qiling 
# input: 6
# output: A3n4&4
pass_length = int(input("Password length :\n"))
password = ""
letters = "asdfghjklllllzxcvbnmqwertyuiop123456789!@#$%^&*()"
upper_letters = "asdfghjklllllzxcvbnmqwertyuiop".upper()
for i in range(pass_length):
    password += random.choice(letters + upper_letters)
print(password)

# task 3 
# 0 dan 50 gacha bolgan sonlar orasidan tasodify 10 tasini oling agar  son toq bo'lsa ularni yigindisini agar just bo'lsa kopaytmasini ekranga chiqaring (yigindilar alohida kopaytma alohida chiqadi )
# juft=1
# toq=0
# for i in range(10):
#     r_num=random.randint(0,50)
#     if r_num%2==0:
#         juft*=r_num
#     else:
#         toq+=r_num
# print(juft)
# print(toq)

# task 4
# userdan son qabul qiling (n) va 0 dan 1000 gacha bolgan sonlar orasidan tasodif n ta son tanlab oling. tasodifiy sonlar ichidan 3 ga bo'linadiganlari nechtaligini aniqlang
# [j for j in [random.randint(0, 1000) for i in range(int(input('>>>')))] if j%3==0]