from transliterate import translit, get_available_language_codes
import random
# STRINGS
# s = "python"
# n_str = str(123456)
# print(type(n_str))  # str
# print(len(s))  # 6
# print(type(len(s)))  # int

# """""" >> doc string


# def test():
#     """This is simple function"""
#     return True


# print(test.__doc__)  # This is simple function

# long_str = """\tTo create a link, \n enclose the link text in brackets \
#     (e.g., [Duck Duck Go])\U0001f600  and then follow it \
#     immediately with the URL in \U0001f600 parentheses (e.g.,\
#         \U0001f600 (https://duckduckgo.com))."""
# print(long_str)

# s = "python"  # index range [0,5]
# print(s[0])  # p
# print(s[10])  # IndexError: string index out of range
# String Slice [start:end]
# a = s[2:]  # 2 index dan to oxiriga qadar qirqish | thon
# a = s[:2]  # 2 index dan to oxiriga qadar qirqish | py
# c = s[1:-2]  # yth
# b = s[-4:-1]  # tho
# z = s[::-1]  # nohtyp
# print(z)
# Formatting strings

# s = "Python is %s pl" % "slow"
# print(s)  # Python is slow pl
# s2 = "Python is {} pl".format("fast")
# print(s2)  # Python is fast pl
# super_fast = "super fast"
# s3 = f"Python is {super_fast} pl"
# print(s3)  # Python is super fast pl

# STRING METHODS
# s = " Python "
# print(len(s))  # 8
# strip - qator boshida va oxiridagi probellarni ochiradi
# print(len(s.strip()))  # 6
# print(len(s.rstrip()))  # 7
# print(len(s.lstrip()))  # 7

# split - siz korsatgan belgi boyicha str ni elementlarga ajratadi (massiv qiladi)
# long_str = "python*js*cpp*html"
# print(long_str.split("*"))  # ['python', 'js', 'cpp', 'html']
# print(long_str.rsplit("*"))  # ['python', 'js', 'cpp', 'html']

# long_str = "python ok \n js ok \n cpp ok"
# splitlines - str ni qatorlar boyicha ajratadi
# print(long_str.splitlines())  # ['python ok ', ' js ok ', ' cpp ok']

# join - massivni str qiladi
# print("".join(long_str.splitlines()).split("\n"))
# ['python ok js ok cpp ok']

# s = "python"
# print("python is better".title())  # Python Is Better
# print(s.upper())  # PYTHON
# print(s.lower())  # python
# print("python is better".capitalize())  # Python is better

# print(chr(1))  # bu raqam qabul qiladi va ascii boyicha belgini qaytaradi
# print(ord("a"))  # bu belgini qabul qiladi va ascii boyicha tartib raqamini qaytaradi
# s = "python"
# long_str = "split - siz korsatgan belgi boyicha str ni elementlarga ajratadi"
# # siz korsatgan matnni boshlanish index ini qaytaradi
# print(long_str.find("siz"))  # 8
# print(long_str.find("text"))  # -1
# print(long_str.rfind("str"))  # 36
# print(s.index("h"))  # 3
# print(s.rindex("l"))  # ValueError
# aks holda -1 qayataradi


# s = "A byte of python"
# ru_text = "лучшее место для поиска векторных изображений."
# ['bg', 'el', 'hy', 'ka', 'l1', 'mk', 'mn', 'ru', 'sr', 'uk']

# print(translit(s, "ru"))  # А быте оф пытхон
# print(translit(ru_text, "mn"))  # А быте оф пытхон
# print(s.count("o"))  # 2 | elementni str dagi sonini qaytaradi

# print(s.startswith("A"))  # True
# print(s.startswith("a"))  # False
# print(s.startswith("a".lower()))  # Every OK

##########
# print(s.endswith("on"))  # True
# print(s.endswith("of"))  # False

########
# print(s.replace("python", "javascript"))

########
# print("abc123".isalnum())  # True | harf yoki osnlar
# print("abc123".isalpha())  # False | faqat harflar
# print("123".isdigit())  # True | faqat butun sonlar
# print("123".isdecimal())  # True | faqat  sonlar
# print("123".isnumeric())  # True | faqat butun, kasr, rim , qoldiqli sonlar
# print("str".isupper())  # False
# print("str".islower())  # True
# print("str".istitle())  # True


# task 1
# input: user son kiritadi agar  son - da bolmasa  yoki 0 ga teng bomasa
# sonlarni yigindisini hisoblang
# while orqali toxtovsiz son kiritiladi agar "stop" deb kiritlsa sikl toxtedi va sonlar
# yigindisi ekranga chiqadi

# task 2
# input : userdan str qabul qilinadi | masalan "python"
# output: "pyThON" | random belgilar katta harfda random belgilar kichik
# user = input()
# result = ""
# for i in range(len(user)):
#     r = random.randint(0, len(user) // 2)
#     if r % 2 == 0:
#         result += user[i].upper()
#     else:
#         result += user[i]
# print(result)
