# task 1
# input :  arr = [2,3,4,5,6,7,8]
# user numbers (index, step) 0 , 3
# output :  arr = [3,4,5,2,6,7,8]
# 2
# let arr = [3,4,5,2,6,7,8] massivda istalgan sonni tanlasam shu sonni onga yoki chapga suruvchi functiuon yozing
# masalan men 2 bilan 3 ni kiritsam function mendan sorasin 2-indexdagi elementni 3 ta index onga suremi yoki chapga deb chapga desam chapga sursin
# # task 2
# input: arr = [2,4,6,7,9]
# output: max sum and min sum

# task 3
# input: arr = list(random nums : 20)
# output: max sum and min sum

# task 4
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# massivni ichida 5 dan kichik barcha sonni chiqaring

# task 5
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# ikkala massivda ham qatnashgan sonlarni chiqaring

# task 6
# dict ni qiymatlari osishiga qarab saralang
# masalan : d = {'a':12, 'b':7} >> d = {'b':7, 'a':12}

# task 7
# user dan sonlarni vergul orqali kiritlgan string qabul qiling
# ushbu sonlardan int qiymatidagi tuple ni qaytaring
# u = "1,2,3"
# t = (1,2,3)
# def func(a : int,b : int) -> int:
#     return a * b
# task 8
# qator palindrom yoki palindrom emasligini aniqlan
# masalan alla palindrom u chunki onga ham chapga ham bir hil oqiladi

# task 9
# user kiritgan sonlar oraligida nechta aynan usha sonlarga
# qoldiqsiz bolinuvchi son borligini aniqlang
# masalan 2,10 >> 10 uchun 2 ga qadar 5 bor yani  1 ta

# task 10
# user kiritgan qator ichidan raqamlarni ajratib oladigan
# function yozing

# task 11
# random belgilar ketma ketligidan user kiritgan miqdorda unikal kod
# xosil qilib uni tuple da saqlaydigan getRandomCode() function ni yozing
# maslan user = 3
# t = ("dddas54f5","asfddv6c","cncnku5d52")

# Selection sort
# arr = [10,23,-8,6,-1,0,2,3,7]
# N = len(arr)
# for i in range(N - 1):
#     m = arr[i]
#     p = i
#     for j in range(i+1, N):
#         if m > arr[j]:
#             m = arr[j]
#             p = j
#     if p != arr[i]:
#         t = arr[i]
#         arr[i] = arr[p]
#         arr[p] = j
# print(arr)


# input: assalomu alaykum
# ouput: alkmosu

# task 1
# Petya va Vasya karta oynayapti, ular o'radan butun musbat sonlar
# biriktirlgan kartalarni tortishadi keyin qiymatlarini tekshirishadi
# kimda kam qiymat bolsa u yana karta tortadi va kartani ozida olib qoladi
# kartalar tugashi bilan kimda eng kam qiymat bolsa u yutgan boladi
# oyin oxirida golibni ismini va ochkolarini maglubni ismi va ochkolarini
# chiqaradgan dastur tuzing

# input: kartalar soni 52 ,biriktirilishi mumkin bolgan sonlar: 3 < n < 999
# output : winner = Vasya 12, looser=Petya 23

# a = 1
# try:
#     a = 2
#     print(a)
#     raise Exception()
# except:
#     a = 3
#     print(a)
#     raise
# else:
#     a = 4
#     print(a)
# finally:
#     a = 5
#     print(a)

# d1 = {
#     "a":1
# }
# d2 = {
#     "b":2
# }
# d1.update(d2)
# print(d1)
# print(tuple(range(10)))

# def mergeDict(*dicts):
#     d = {}
#     for i in dicts:
#         d.update(i)
#     return d
# print(mergeDict(d1,d2, {"c":3}))

# s = "alla"
#count a  ?
# def func(letter, word):
#     return print(word.count(letter))
#
# func("a", "alla")

# import random

# print(random.random()) 0 bilan 1 orasida
# s = 'python'
# print(random.choice(s)) # random 1 sini tanlash
# a = [1,2,3,4,5]
# random.shuffle(a)
# print(a) # massivni indexlarini alishtrish
# b = random.sample(a,3) # ketmaketlikdan tasodifiy siz korsatgancha elem, olish
# print(b)
#
# while orqali userni ismidan tasodify harflarni oling agar harf "s"
# ga togri kelsa sikl toxtasin va nechi marta sikl bogani hisoblansin
# max()
# min()

# print(max([1,2,3])) # 3
# print(min([1,2,3])) # 1
# print(min("Hello world"))
# print(ord("W"))# 87
# print(chr(76)) # L
# for i in range(3):
#     print(random.randint(1, 100))

# import random
# salary = [random.randint(100,1000),random.randint(100,1000),random.randint(100,1000)]
#
# print(f"Eng kam oylik = ${min(salary) }")
# print(f"Eng Katta oylik = ${max(salary) }")
# print(f"Orasidagi farq = ${max(salary)  - min(salary)}")
# import time
# team1 = 0
# team2 = 0
# for i in range(1,5):
#     sc1 = random.randint(15, 30)
#     sc2 = random.randint(15, 30)
#     team1 += sc1
#     team2 += sc2
#     print(f"Part {i} |Team 1 = {sc1} | Team 2 = {sc2}")
#     time.sleep(2)
# print(f"Total scores \n Team 1 = {team1} | Team 2 = {team2}")
# print(f"Winner = Team with score {max(team1, team2)}")
# import random
# coins = []
# print(random.randrange(-10 , 11))
# for i in range(10):
#     coins.append(random.choice(range(-10,10)))
# print(coins)
# for i in range(-10 , 11):
#     print(i)

# s = input() # 123
# n = []
# for i in s:
#     n.append(int(i))
# for x in reversed(n):
#     print(x , end="")
# n.reverse()


# 321 type int


# def strFunc(s):
#     s = s.strip()
#     s = s.split(" ")
#     s = ",".join(s)
#     return s
#
# test = " lorem ipsum dolor amet sit "
# t = strFunc(test)
# print(t)

# text = "lorem"
# def loremToTupple(s):
#     s = tuple(s)
#     return s
# print(loremToTupple(text))

# def s(x): #1
#     return x*x #2
# for n in [1, 2, 10]: #3
#     print(s(n))
n = 3
for x in [2, 5, 8]:
    n = n + x
    print(n)