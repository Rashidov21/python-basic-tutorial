"""docstring"""
# line comment 

# variables 
# 1-logical 
# 2-english 
# 3-first letter not a number

# _range = (1,11)
# _ = 10
# print(_ * 2) # 20

# HEADER = "head" # constant
 
# data types 
# int , float, complex , str, bool , None 
# x = 10 # int 
# f = 10.5 # float 
# c = 2j # complex 
# s = "python" # str '',"",""""""
# b = True # bool 
# n = None # None 


# data structures   
# list , tuple , set , frozenset , dict ,range 
# l = list() # [] - array - tartibli elemenlar ketma-ketligi
# t = tuple() # () - tuple - o'zgarmas elementlar ketma-ketligi 
# s = set() # {} - set - unikal elementlar to'plami 
# fs = frozenset() # frozenset - o'zgarmas ko'plik 
# d = dict() # {"k":1} - dict - lug'at , elementlarga murojaat kalit orqali boladi
# r = range() # range - sonlar diapazoni

# arifmetika 
# print(1+1) # 2
# print(3-1) # 2
# print(3*2) # 6
# print(4/2) # 2.0
# print(4//2) # 2
# print(2**2) # 4
# print(7%3) # 1

# print((10 + 2) * (9 - 6) / 2) # 18.0

# logika 
# print(2 > 1) # True
# print(2 >= 1) # True
# print(2 < 1) # False
# print(2 <= 1) # False

# print(1 == 1) # True 
# print(1 != 2) # True 

# is - bir hil qiymatga ega yoki yo'q 
# x = 10
# y = x
# print(x is not y) # False 
# print(x is not 30) # True 
# print(x + 2) # 12
# print(y * 2) # 20
# print(x is y) # True
# x = 10
# y = 5
# print(x + 2) # 12
# print(y * 2) # 10
# print(x is y) # False

# in - mavjudlikga tekshirish 
# print("s" in "sorry") # True

# not - inkor qilish
# print(not True) #  False
# print("s" not in "sorry") # False 
# print("t" not in "sorry") # True 


# and  - mantiqiy VA (False ga tekshiruv) 
# print(1 and 0) # 0
# print(1 > 0 and 10 < 90 ) # True

# or - mantiqiy YOKI (True ga tekshiruv)
# print(1 or 0) # 1 
# print(False or "" or 20 or 0) # 20
# print(1 > 0 or 1 < 0)  # True

# if conditions 
# x = 7
# if x == 3:
#     print("if : True")
# elif x == 5:
#     print("elif : True")
# else:
#     print("else : ")

# ternary if 
# year = 2024
# value = "FIFA 24" if year >= 2023 else "FIFA 23"
# print(value)

# loops 
# for i in range(5): # i , k , j , x 
#     if i % 2 == 0:
#         print(i)
#     else:
#         print("toq son")
# else:
#     print("for else")
# i = 0
# while True:
#     i += 1
#     if i == 100:
#         break # tsiklni to'xtatish
#     if i % 2 == 1:
#         continue # tsiklni tashlab keyingi tsiklga o'tish
#     print(i) 


# functions 
# def main(x,y=10):
#     print(x + y)
#     return x + y

# main(10,2) # 12

# *args , **kwargs 
# def arguments_keywordarguments(*args,**kwargs):
#     print(type(args)) # tuple
#     print(type(kwargs)) # dict
#     return [i for i in args]

# arguments_keywordarguments(1,"one", False, a=10,b=20,c=30)

# lambda - nomsiz yengil function
# arr = [0,1,2,3,4,5,6,7]

# print(list(filter(lambda x: x % 2 == 1, arr))) # [1, 3, 5, 7]
# x = lambda a,b,c: a + b +c
# print(x(1,2,3)) # 6

# Recursion - funktsiya o'zini o'zi chaqirganida

# def recursion_func(x):
#     x += 1
#     print(x)
#     if x == 10:
#         print("The end !")
#         return True
#     return recursion_func(x)

# recursion_func(1) 

# decorators - oddiy functionni ishini o'zgartiruvchi yoki undan avval biror bir ishni qiluvchi functionga aytiladi 

# def wrapper(f):
#     print(f"{f.__name__} - funktsiya ishga tushdi")
#     return f

# @wrapper
# def main():
#     print("Main func")
# @wrapper
# def some_func():
#     print("Some func !")
    
# main()
# some_func()




