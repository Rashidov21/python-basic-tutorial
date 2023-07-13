# list , tuple , set , frozenset , dict 

# list - tartiblangan elementlar toplami 
# tuple - o'zgarmas tartiblangan elementlar toplami
# set - unikal elementlar toplami 
# frozenset - o'zgarmas unikal elementlar toplami 
# dict - kalit va qiymat usulida saqlanadigan elementlar toplami 

# data type - malumot turi
# a = 10 
# data structure - malumotlarni ma'lum bir usulda saqlash

# list - Massivlarni dinamik korinishi  (Ro'yhat)
# a = [10,20,"teen"]
# l = list("Hello")

# print(a) #  [10,20,"teen"]
# print(l) # ['H', 'e', 'l', 'l', 'o']

# a = []
# for i in range(1,11):
#     a.append(i)
    
# print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# print(list(range(1,11))) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# arr = list(range(1,11))
# arr[0] = -1
# print(arr)  # [-1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# s = "helloos"
# s[-1] = "o"

# l = list(s)[-1] = "o"
# print(f"{''.join(list(s)[:-1])}"+"".join(l))



# t = tuple()
# t = (1,2,(2,3), True,"none")
# print(t[2])
# s = t[0] = 1
# print(s)
# print(type(t)) # <class 'tuple'>


# List generators 

# for i in range(5):print(i)


# print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# s = "pythonjon"
# arr = [x for x in s if x == 'o']
# print("".join(arr))
# import random

# arr1 = [1,4,6,9,8,2,3,5,6,9,4]
# arr2 = [2,5,69,47,5,3,1,2,35,4,56,23,1]

# result = []

# for i in arr1:
#     if i in arr2:
#         result.append(i)
# print(result) # [1, 4, 2, 3, 5, 4]

# result = [i for i in arr1 if i in arr2]
# # print(result) # [1, 4, 2, 3, 5, 4]

# text = "lorem ipsum dolor"
# res = ""
# for word in text.split(" "):
#     for letter in word:
#         if letter == "o":
#             res += letter
# # print(len(res)) # 3
# res_arr = [letter for word in text for letter in word if letter == "o"]

# print(len(res_arr)) # 

# letters = "Python"
# nums = [1,2,3,4,5,6]

# print(zip(letters,nums))

# print(list(zip(letters,nums)))

# arrl = [1, 2, 3, 4, 5] 
# arr2 = [10, 20, 30, 40, 50] 
# arr3 = [100, 200, 300, 400, 500]

# print(sum(arrl)+sum(arr2)+sum(arr3)) # 1665
# (1,10,100) + (2,20,200)
# print(sum([a+b+c for (a,b,c) in zip(arrl,arr2,arr3)])) # 1665

# range() , len() , print() , filter()

# arr = [1,4,5,9,7,8,6,2,1]

# def checkUp(num):
#     if num > 5:
#         return num
# print(filter(checkUp,arr)) # <filter object at 0x000001C2B527B5E0>
# print(list(filter(checkUp,arr))) # [9, 7, 8, 6]


# def main(num):
#     return num + 2

# arr = [1,2,3,4,5]
# print(map(main,arr)) # <map object at 0x0000025BBF69B580
# print(list(map(main,arr))) #[3, 4, 5, 6, 7]

# Array methods 
# append - qoshish
# extend - boshqa massiv bilan kengaytrish
# insert - indeks boyicha qoshish
# index - elementni indexini olish
# remove - qiymat boyicha ochirish 
# del - index boyicha ochirish 
# pop - index boyicha ochirish 
# clear - tozalash
# copy - nusxalash
# arr = [1,2]
# arr.append(3)
# print(arr) # [1, 2, 3]
# a = [4,5]
# arr.extend(a)
# print(arr) # [1, 2, 3, 4, 5]
# arr.insert(2,"zero")
# print(arr) # [1, 2, 'zero', 3, 4, 5]
# print(arr.index("zero")) # 2
# arr.remove("zero")
# print(arr) # [1, 2, 3, 4, 5]
# # del arr[2:]
# # print(arr) # [1, 2]
# arr.pop(3)
# print(arr) # [1, 2, 3, 5]
# arr.clear() # []
# a = arr.copy()

# task 1
# Qatorda bir belgi necha marta qatnashganini hisoblang.
    # task 1.1
    # string = 'Python Software Foundation'
    # letter = "o"
    # task 1.2
    # string = 'Python Software Foundation'
    # output : "o" = 4 
    
# chalanoxot
# task 2 
# 9 karra ni 10 ta savolini ekranga chiqaruvchi va userdan javob qabul qiliuvchi dastur tuzing
# maslan birinchi savol: 9 x 1 = ?  , userdan sonni qabul qilib dastur keyingi savolga o'tadi 10 ta savoldan keyin
# dastur foydalanuvchini barcha variantlarini tekshiradi va ekranga qaysi savolga tog'ri qaysi savolga xato javob berganini chiqaradi masalan :
# 9 x 1 = 1 xato javob 9 bo'ladi  
# 9 x 2 = 18 tog'ri javob 
# ....



# sort , sorted 
# arr = [1,5,4,8,9,6,3,4]
# arr.sort()
# print(arr) # [1, 3, 4, 4, 5, 6, 8, 9]
# arr.sort(reverse=True)
# print(arr) # [9, 8, 6, 5, 4, 4, 3, 1]

# arr = ['Python','PYTHON','python','pytHon','pythoN']

# arr.sort()
# print(arr) # ['PYTHON', 'Python', 'pytHon', 'pythoN', 'python']

# alpha = "BaTSZxy1U2"
# t = (1,5,4,6,8,3)

# for i in sorted(t, reverse=True):
#     print(i, end="") # 12BSTUZaxy , 865431

# s = set()
# s = {1,2,3,4,6}


# hi = "Hello Guys !"
# s = set(hi)
# print(s) # {'o', ' ', 'e', 'G', 's', '!', 'y', 'u', 'H', 'l'}
# print(s[0]) # TypeError: 'set' object is not subscriptable

# frozenset - set ni o'zgarmas varianti 
# fs = frozenset("hello")
# print(fs) # frozenset({'l', 'e', 'o', 'h'})

# dict - obyektlar toplami , ularga indeks orqali emas balki kalit so'z orqali murojaat qilinadi

# d = dict(name="John", age=20)
# print(d) # {'name': 'John', 'age': 20}
# user = {
#     'username' : 'gandi123',
#     'age': 23
# } 
# print(user) # {'username': 'gandi123', 'age': 23}

# print(user.username) # AttributeError: 'dict' object has no attribute 'username'

# print(user['username']) # gandi123

# for i in user:
#     print(i) # username , age
    
# for i in user:
#     print(user[i]) # gandi123 , 23

# print(user.keys()) # dict_keys(['username', 'age'])
# for key in user.keys():
#     print(key) # username , age
# for val in user.values():
#     print(val)
# for item in user.items():
#     print(item) # ('username', 'gandi123'), ('age', 23)
# d = {}
# d["age"] = 12 # 1 variant
# print(d) # {'age': 12}
# d.update({"salary":500}) # 2 variant
# print(d) # {'age': 12, 'salary': 500}


# task 1
# a = "ABCDEFHG"
# b = "12345678"
# d = {}
# # d dictiga a dan kalit va b dan qiymat olgan holatda yozing
# # output: {"A":1,"B":2 ..}

# for i in range(len(a)):
#     d.update({a[i]:b[i]})
# print(d) # {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5', 'F': '6', 'H': '7', 'G': '8'}

# print({k:v for (k,v) in zip(a,b) }) 


# task 2 
# userdan so'z qabul qiling va uni bo'gimlarga ajrating
# input: bemaza , palov
# output: be , ma , za  : pa , lo


# d = {"age":20,"position":"backend"}

# print("age" in d) # True
# print("country" in d) # False

# print(d["country"]) # KeyError: 'country'
# print(d.setdefault("age")) # 20
# print(d.setdefault("country")) # None
# d.setdefault("country","USA")
# print(d) # USA

# d = {"age":20,"position":"backend"}
# print(d.keys())
# print(d.values())
# print(d.items())


# olish 
# d = {"age":20,"position":"backend"}

# print(d["country"]) # KeyError: 'country'
# print(d.get("age"))
# print(d.get("country")) # None
# d.pop("age") # korsatilgan key boyicha elementni ochirish
# print(d) # {'position': 'backend'}
# d.popitem() # tasodify bitta elementni ochirish
# d.clear()
# print(d) # {}

# d.update({'country':"USA"}) 
# print(d)# {'age': 20, 'position': 'backend', 'country': 'USA'}
# d.update(country='USA',salary=1200)
# print(d)# {'age': 20, 'position': 'backend', 'country': 'USA', 'salary': 1200}