# Data Types >> Malumot turlari >> int ,str,bool, float
# Data Structure >> Malumot tuzilishlari >> list, tuple, dict, set, frozenset, range
# arr = ['first','second',1,2,True, False,['arr1','arr2']] # list >> array
# print(arr[6][0])

# arr = list("string")
# print(arr)

# arr = [1,2,3,4,5]
# arr.append(6) # oxiriga element qoshish
# print(arr) # [1,2,3,4,5,6]
# print(arr[8]) # IndexError list index out of range
# print(arr[-1]) # oxirgi element
# for i in arr:
#     print(i)
# print(len(arr))# 5
# x = arr[1:3]
# print(x)
# print(arr)
# ls = [[2,3,5],[5,689,78],[89,56,12,36]]
# for k in ls:
#     for x in k:
#         print(x)
# ls2 = [1,2,3,5,6,8]
# i , c = 0 , len(ls2)
# while i < c:
#     ls2[i] *= 2
#     i += 1
# print(ls2)
# name , age , salary = "Abdulhaq",15,0
# print(name, age, salary)
# import random
# arr = [1,2,3,4,5,6]
# print(random.choice(arr))

# task 1
# input:arr = []
# output: arr = [10 random number range 0,50]

# task 2
# input:arr = [1,2,3,4,5,6,7,8,9,10,11]
# output: new_arr = [2,4,6,8,10]

# task 3
# input:arr = [1,2,3,4,5]
# output: new_arr = [1,9,25]

# task 4
# input:arr = [1,2,3,4,5,6,7,8,9,10,11]
# output = summa >> arr
# arr = [1,2,3,4,5,6,7,8,9,10,11]
# print(sum(arr))
# s = 0
# for i in arr:
#     s += i
# print(s)
# s = 0
# for x in arr:
#     if x % 2 == 0:
#         pass
#     else:
#         s += x
# print(s)
# s = []
# for k in arr:
#     if k % 2 == 0:
#         s.append(k**2)
# print(s)
# print(sum(s))

# task 5
# letters = ['1','2','3','4','5', "q","w","e","r","t","y", "@","#","_","&","$"]
# # user password length = 8
# # output: str = '2#6$_q6r'

# task 6
# input: int numbers >> 2,3
# output: 8 cube
# while >> while stop >> result <= 10000

# task 7
# ord() chr() >>
# input: "letters >> A, l, P ..."
# output: [12,963,1052,15]

# /xb15 >> is_alpha >> split("/")

# arr = ["word", "word1", "word2"]
# print("".join(arr))

# t = (1,2,3)
# l = list(t)
# l.reverse()
# t = tuple(l)
# str_tuple = tuple("word")
# print(str_tuple)
# print(t)

# s = set("NON")
# s2 = {"n","o", "n"}
# print(s)
# print(s2)
# s = set("al")
# s.union(set("to")) # kengaytirish
# s.update(set("to")) # yangilash ,qoshish
# s.add(22) # element qoshish
# s.remove(22) # element ochirish
# s.discard("a") # agar elem bosa ochiradi bomasa xatolik yuz bermaydi
# s.pop() # tasodifiy bitta elem ni ochiradi
# s.clear() # tozalash
# print(s)
# f = frozenset("str")
# print(f)

# dict()
# d = dict(name="Abdulloh")
# print(d["name"])
# user = {
#     "name":"Abdullo",
#     "age":12,
#     "is_admin":False
# }
# user["name"] = "John" # mavjud elemni ozgartirish
# user["skills"] = ["html","css"] # yangi elem qoshish
# print(user)
# print("age" in user)# True
# print("age" not in user) # False
# print(user.get("age")) # 12 : key orqali value olish
#
# for x in user: # faqat key lari olinadi
#     print(x)
# for x in user.items(): # elementlar olinadi tuple() korinishida
#     print(x)
# for x in user.keys():# faqat key lari olinadi
#     print(x)
#
# for x in user.values(): # faqat value lari olinadi
#     print(x)

# d = {
#     "y":1,
#     "x":0,
#     "z":2
# }
# k = list(d.values())
# k.sort()
# print(k)
# for i in sorted(d.values()):
#     print(i)
# company = {
#     "apple":"Iphone",
#     "samsung":"Samsung",
#     "mi":"Xiaomi",
# }
# c = company.copy() # nusxasini olish
# c.clear() # tozalash
# company.update({"nokia":"Nokia3310"})
# company.pop("nokia") # siz korsatgan key boyicha elem ochiradi
# company.popitem() # tasodify bitta elem ochiradi >> tuple() qaytaradi
# print(company)

# a,b,*c = 1,2,3,4,5,6
# print(a,b,c)
# import time
# import locale
# locale.setlocale(locale.LC_ALL, "uz-Latn-UZ")
# t = time.strftime("%d.%m.%Y : %B") # bugunlik sana
# print(t)
# import datetime

# print(datetime.timedelta(weeks=1, days=2,hours=10, minutes=5, seconds=55))
# d1 = datetime.timedelta(days=3)
# d2 = datetime.timedelta(days=1)
# print(d1 - d2) #2 days, 0:00:00
# t = datetime.date
# print(t.today()) #2021-12-11
# print(t.year) #2021
# print(t.month) #12
# print(t.day) #11
# n = datetime.datetime.now() #2021-12-11 18:36:22.012067
# print(n)
# import time
# for i in range(10):
#     print("Hello")
#     time.sleep(3)
# import calendar
# c = calendar.TextCalendar(0)
# html = calendar.LocaleHTMLCalendar(0 , "uz-Latn-Uz")
# uzcalendar = calendar.LocaleTextCalendar(0, "uz-Latn-Uz")
# # print(c.formatyear(2022))# matn korinishidagi calendar
# # print(uzcalendar.formatyear(2022))# matn korinishidagi calendar ozbecha
# # print(html.formatyear(2022))# html korinishidagi calendar ozbecha
# print(uzcalendar.formatmonth(2021, 12))# html korinishidagi 1 oy uchun calendar ozbecha

# from timeit import Timer
#
#
# code1 = """\
# i, j = 1, 0
# while i < 10001:
#     j += 1
#     i += 1
#     """
# t1 = Timer(stmt=code1)
# print("while:", t1.timeit(number=1000))
# code2 = """\
# j = 0
# for i in range(1,10001):
#     j += 1
# """
# t2 = Timer(stmt=code2)
# print("for:", t2.timeit(number=1000))
# code3 = """\
# j = sum(range(1,10001))
# """
# t3 = Timer(stmt=code3)
# print("sum:", t3.timeit(number=1000))


# a = [1,2]
# b = [3,4]
# print(zip(a,b)) # [(1, 3), (2, 4)]

# def func(x, y):    
#     return x*y

# a = [1,3]
# b = [3,4,5]
# a = map(func, a, b)
# for i in a:
#     print(i)

# a = list(range(6))
# # b = list(range(99,103))
# for i in zip(a,"python"):
#     print(i, end="")

# def toUp(num):
#     return num * num

# a = list(range(1,6))

# for i in map(toUp, a):
#     print(i, end="")





