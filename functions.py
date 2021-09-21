# list() >> array
# len() >> lenght int

# def <fuknsiya nomi>([parametrlar]):
#     ["""Funksiyani documentataion"""]
#     <Funksiyani tanasi>
#     [return <Natija>]

# def printOk():
#     """This is my first function in Python"""
#     print("Ok")
# print(printOk())

# def func():
#     pass
#
# def echo():
#     print("echo hello world")
#
# echo() # funksiyani chaqirish

# def plus(x,y):
#     return x + y
# print(plus(20,10))

# def getUserShortname(name,surname):
#     return name + " " + surname
# print(getUserShortname("Abdurahmon","Rashidov"))

# def getMaxValue(arr):
#     return max(arr)
# m = getMaxValue([2,6,7,8,9])
# print(m)
# def userInfo(name,surname, age=None):
#     return name + " " + surname + " " +  str(age)
# print(userInfo("ali", 'vali', 23))
# num = 10
# print(num)
# def func(x):
#     return print(x * 2)
# func(num)
# def func(x,y):
#     return print( x ** y )
# func(x=10,y=2)


# def plus(a,b):
#     return a + b

# def main(param1=10): # deafult params , doimiy qiymatlar
#     print(param1)
# main()

# x,y,*z = [1,2,3,4,5,6]
# print(x,y,z) #1 2 [3, 4, 5, 6]

# *args
# bitta * lik metod bu berilayotgan argumentlarni tuple ga joyledi
# def summa(*t):
#     """ funksiya nomalum miqdorda qiymat qabul qiladi """
#     res = 0
#     for i in t:
#         res += 1
#     return res
#
# print(summa(10,20))
# print(summa(10,20,30,40,50,60))

# def summa(*args):
#     print(type(args)) # tuple
#     res = 0
#     for i in args:
#         res += 1
#     return res
# print(summa(1,2,3,4,5))

# **kwargs
#  ikita * lik metod bu berilayotgan argumentlarni dict ga joyledi

# def func(**k):
#     print(k)
#     for i in k:
#         print(i)
# func(a=1,b=2,c=3)
# func(abdullo=15,oylik=15000,kun=13)

# def func(**kwargs):# keyword arguments
#     print(kwargs)
#     for i in kwargs:
#         print(i)
# func(a=1,b=2,c=3)

# def superFunc(*args,**kwargs):
#     """ function istalgan argumentni qabul qila oladi"""
#     for i in args:
#         print(i, end="")
#     for j in kwargs.items():
#         print(j)
# superFunc(1,2,3,4,5, olti=6,yetti=7)

# f = lambda: 10 + 20
# print(f()) # 30
# f1 = lambda x,y: x + y
# print(f1(10,20))# 30
# f2 = lambda x,y=5:x * y
# print(f2(10)) # 50
# print(f2(10,2)) # 20

# arr = list(range(0,11))
# arr2 = []
# for i in arr:
#     f = lambda x: x ** 2
#     arr2.append(f(i))
#
# print(arr2)

# Decorators
# Decorator bu biror bir funtionni ishlashiga tasir otqizadgan boshqa bir
# functionga aytiladi, masalan function ishga tushishidan avval biror bir
# ishni qilishi kerak bolsa decorator buni unga qildira oladi

# def deco(f):
#     print("f funksiyasi chaqirildi")
#     return f
#
# @deco
# def func(x):
#     return f"x = {x}"
# print(func(10))

# password = input("parolni kirit..")
# def testPassword(p):
#     def deco(f):
#         if p == "10":
#             return f
#         else:
#             return lambda : "Sizga ruxsat yo'q !"
#     return deco
# @testPassword(password)
# def func()
#     return "Sizga ruxsat bor!"
#
# print(func())

# pin = input("PIN kodni kiriting..")
# def check_pinCode(pin):
#     def deco(f):
#         if pin == "1234":
#             return f
#         else:
#             return lambda : "Sizga ruxsat yo'q !"
#     return deco
#
# @check_pinCode(pin)
# def getMoney():
#     m = int(input("Qancha yechamiz ?"))
#     balance = 100
#     print("Chekni oling: balans=",balance-m)
#
# @check_pinCode(pin)
# def addMoney():
#     m = int(input("Qancha soamiz ?"))
#     balance = 100
#     print("Chekni oling: balans=", balance + m)
#
# print(getMoney())
# print(addMoney())

# Rekursiya
# Rekursiya bu - biror bir functionni ozini ozi chaqiqirishia aytiladi

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return  n * factorial(n - 1) 5,4
# while True:
#     x = int(input("Sonni kiriting.."))
#     print(f"{x} ni faktoriali =  {factorial(x)}")

# task 1

# decorator orqali login va username togri bolgandagina saytga xush kelibsiz
# degan matnni print qiladgan function yozing

# task 2
# login va username tori boganda user dan son sorab uni factorialini
# hisoblaydigan function yozing

# task 3
# input: user  = "123456970"
# output: str  dagi barcha sonlarni bir biriga qoshin va agar 0 mavjud bolsa
# summani print qiling script toxtasin