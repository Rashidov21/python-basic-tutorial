import keyword  # zaxiranlagan operatorlar
# print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
#     'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# name = "John"
# print(name)  # John

# userNameProfilePage = "/home/profile/"  # Camel Case
# user_name_profile_page = "/home/profile/"  # Kebab Case
# n1 = 10
# User = "oblivion"  # mumkin emas
# USER = "gandi12"  # constanta
# USER = "pablo"
# print(USER)  # PABLO

# DATA TYPES
"""
bool , None , int , float, str, complex , bytes, bytearray, list , tuple, dict , set , frozenset, function, module, type
"""
# yes = True  # 1
# no = False  # 0
# print(type(yes))  # bool | <class 'bool'>
# print(yes + no)  # 1
# print(type(None))  # <class 'NoneType'>

# int | butun sonlar = integer
# n = 10
# n2 = -10
# print(type(n))  # <class 'int'>
# # float | qoldiqli
# x = 1.2
# y = -5.3
# print(type(x))  # <class 'float'>

# str  | qatorlar
# name = "Guido Van Rossum"
# s = 'python %s' % 10  # 2.7 eski usul xozir ishlatilmaydi
# s2 = "{0} pyt {1} hon {2}".format(10, 5, 20)  # bu ishlatiladi lekin eski usul
# s3 = f"""python  - {name}"""  # aktual usul
# s4 = f"Value = {10+10}"
# s5 = r"\tPython\n\\is\n\"better\"\a"

# print(s, s2, s3)
# print(type(s))
# print(s)
# print(s2)
# print(s3)
# print(s4)
# print(s5)
# complex | katt
# print(type(2 + 2j))  # <class 'complex'>
# print(bool(1))  # True
# print(bool(0))  # False
# print(bool(""))  # False
# print(bool("sas"))  # True

# n = int(1.2)  # butun songa aytantiradi
# n2 = float(1)
# s = str(1)
# print(n)
# print(n2)
# print(type(s))

# x = input("Str kirit")  # userdan str qiymat qabul qilish
# print(type(x))
# int_num = int(input("Son kirit:"))
# print(type(int_num))

# del x  # x ni ochirish
# print(x)  # Error , NameError | name 'x' is not defined

# Arifmaetika
# print(2 + 2)  # 4
# print(2 - 1)  # 1
# print(4 / 2)  # 2.0
# print(4 * 2)  # 8
# print(7 // 3)  # 2
# print(2 ** 2)  # 4
# print(7 % 2)  # 1
# print("salom" / 2) # Error
# str uchun operatorlar
print("Salom " + " Dunyo")
print("python" * 2)  # pythonpython
print("s" in "salom")  # True
print("s" not in "Hello")  # True
