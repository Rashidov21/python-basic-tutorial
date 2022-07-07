# def function nomi (qabul qiluvchi qiymatlar):
#   """Bu function docstring"""
#   bu yerda function tanasi
#   return  qaytariladigan natija


# def main():
#     pass # pass - operatori bu hech amal yo'qligini bildiradi
# def func(x):
#     print(x)
#     if x > 5:
#         return x ** 2
#     return x * 2  # return bu functionni ishini tugashi


#     # print(x) #bu kod hech qachon ishga tushmaydi
# print(func(2))  # 2 4
# print(func(6))  # 6 36

# def get_users():
#     """This function is my first function in Python"""
#     print("users = miguel, xavi, david")


# get_users()
# print(get_users.__doc__)  # function docstring
# This function is my first function in Python

# def main(x, y):
#     return x + y


# # TypeError: main() missing 1 required positional argument: 'y'
# print(main(10))


# def func(a, b=2):
#     return a + b

# # a = positional argument  (a ni qiymati ko'rsatilishi shart)
# # b = not positional argument (b ni qiymayi ko'rsatilmasa b siz ko'rsatagan qiymatga teng)


# print(func(10))  # 12


# def info(name, surname):
#     return f"{name} {surname}"


# print(info("Abdullo", "Valiyev"))  # Abdullo Valiyev
# print(info(name="Abdullo", surname="Valiyev"))  # Abdullo Valiyev

# * , ** - args (tuple) , kwargs (dict)
# a, b, *c = [1, 2, 3, 4, 5, 6]
# print(a, b, c)  # 1 2 [3, 4, 5, 6]

# def increment(number):
#     return number + 1


# print(increment(5))  # 6
# for i in range(1, 11):
#     print(increment(i))

# def myFun(*args):
#     print(type(args))  # tuple
#     print(args)  # ('Hello', 'Welcome', 'to', 'GeeksforGeeks')
#     for arg in args:
#         print(arg)


# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# def my_kwargs(**kwargs):
#     print(kwargs)  # {'a': 1, 'b': 2, 'c': 3}
#     print(type(kwargs))  # <class 'dict'>
#     for kw in kwargs.items():
#         print(kw)


# my_kwargs(a=1, b=2, c=3)


# def super_func(*args, **kwargs):
#     """Bu istalgan turdagi argument qabul qila oladigan function"""
#     print(args)
#     print(kwargs)


# super_func("assalom", 10, True, name="Abdullo", age=20)
# ('assalom', 10, True)
# {'name': 'Abdullo', 'age': 20}
# lambda - anonim function (nomsiz function)
# arr = ["python1", "PYTHON3", "Python2"]
# arr.sort(key=lambda s: s.lower())  # ['python1', 'Python2', 'PYTHON3']
# print(arr)


# def main(x=1):
#     print(x)


# print(lambda: 1+1)  # <function <lambda> at 0x000001C955DE9CA0>
# print(main)  # <function main at 0x0000026B766661F0>
# x = main
# print(x)  # <function main at 0x0000017EC95B61F0>
# import random


# arr = random.sample(range(100), 20)
# brr = list(filter(lambda n: n > 50, arr))
# # drr = list(filter(up_50(x), arr)) # Error
# print(arr)
# f = list(filter(lambda son: son % 2 == 0, arr))
# print(f)

# s = "assalomu alaykum"
# sl = list(filter(lambda char: char != 'a', s))
# print("".join([str(x) for x in sl]))  # sslomu lykum
# p = lambda x, y: x * 2, y + 2
# p(2,2) # 4 , 4
# r = list(filter(lambda x: x * 2, arr))
# print(r)
# for x, y in enumerate(range(10)):
#     print(x)  # index
#     print(y)  # value

# def up_50(n):
#     if n > 50:
#         return n
#     return 0


# r = []
# for i in arr:
#     r.append(up_50(i))
# print(r)

# task 1
# s = """The function is called with all the items in the list and a new list is returned which contains items returned by that function for each item."""
# get_vowels degan function yozing

# s dagi unlilarni alohida massiv qiling




 
