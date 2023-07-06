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
# string = 'Python Software Foundation'
