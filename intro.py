# import keyword
# print(keyword.kwlist)

# Data Types
# bool , None , Type, int , float , complex , str, bytes, bytearray,
# list,tuple, dict
# range, set , frozenset, ellipsis, function, module, type,

# 1. int >> 1, 89, -96
# 2. float >> 23.3, 10.3 , -56.3
# 3. bool >> True, False
# 4. str >> 'Hello', "Hello", """Hellooo"""

# type() >> qiymat turini aniqlash
#x = 10 # + , - , * , / , %
#y = -5

# VARIABLES
# def main():
#     pass
# print(main)
# <function main at 0x000001C179D061F0> # 0x000001C179D061F0 >> main

# x = ''
# getUserAge = input("Write your age:")
# get_user_age = input("Write your age:")
# print(get_user_age)

# weight = 89.5
# height = 182.6
# print(weight + height) # 272.1
# print(type(height))

# is_admin = True #  int 1
# is_user = False # int 0
# print(True + False) # 1
# print(type(is_user)) #bool

# name = 'Abdullo'
# # print(type(name)) # <class 'str'>
# name2 = "abdullo " \
#         "Abdullo2"

# name3 = """Рекомендую выбирать
#     только версию Home или Pro (или обе),
#  в зависимости от ваших потребностей. Нажмите
#   на кнопку Next, чтобы продолжить."""
# print(len(name3))
#
# text = " lorem \n ipsum" # yangi qatorga otish \n
# text = "text\tabzats" # \t abzats ong tomonga surish
# text = " lorem \"ipsum\" dolor"
# text = 'don\'t : \a'
# print("salom 'qale' """" ssassa""" "")
# print("\a")



# input() >> Userdan malumot qabul qilish
# name = input("Ismingiz nima?") # str formatda belgilarni qabul qilish
# print(type(name))
# x = input("X = ")
# x = int(x)
# y = input("Y = ")
# y = int(y)
# print("Natija = ",x+y)
# s = int(input("Number ? :"))
# n = str(s)
# print(type(n))

# x = input("X = ")
# print(type(bool(True)))
# n = 10
# print(float(n))


# print('Salom', name)
# SyntaxError, IndentationError, TypeError
# int() , str(), float(), bool()
#height = int(input("Bo'yingiz ?")) # faqat int qiymatni qabul qiladi
# height = int(height)
# print(type(height))
#optimal_weight = height - 100 # TypeError
#print('Siz uchun optimal vazn ', optimal_weight, 'kg')
# .format() f"{height}"
# age = 25
# weight = 89
# info1 = "Mening yoshim {0}da Vaznim esa {1}kg \n".format(age,weight) # Python 2.7
# info2 = f"Mening yoshim {age}da Vaznim esa {weight}kg" # Python 3.5
# print(info1,info2)
# age = 10
# year = 2012
# print("Yoshim {0} da ,{1} chi yili tugilganman".format(age,year))
# print(f"{age}, {year}")
# x = 10 # int
# x = str(x) # str
# y = '10' # str
# y = int(y) # int
# z = 1
# z = bool(z) # True
# a = 0
# a = bool(a) # False
# f = ''
# print(bool(f))