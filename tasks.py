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

def sum_two_number(x,y):
    print(x+y)
MAX_VALUE = 100
apple = "Stive Jobs"