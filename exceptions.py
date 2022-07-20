import requests

# Pythonda xatolik  turlari
# 1-SyntaxError
# 2-Mantiqiy
# 3-Dastur ishlash vaqtida yuzaga keladgan xatoliklar

# print(1 + ) # SyntaxError: invalid syntax

# print(int("a"))  # ValueError: invalid literal for int() with base 10: 'a'
# ConnectionAbortedError

# Exception, BaseException

# x = 1 / 0  # ZeroDivisionError: division by zero
# try:  # xatolik vujudga kelishi mumkin bo'lgan kod
#     x = 1 / 0
# except:  # agar xatolik bo'lsa
#     x = 1
#     print("Xatolik")
# else:  # xatolik bo'lmasa
#     print("davom etamiz")
# # finally:  # xatolik bo'lsayu bo'lmasa
# #     # print("har qanday holatda ishga tushadigan blok")
# print(x)  # 1

# f = open("notfile.pdf", "r")
# print(f.read())  # FileNotFoundError

# try:
#     f = open("notfile.pdf", "r")
# except FileNotFoundError as error:
#     print(f"bu yerda xatolik bor : {error}")

# print("Kod davom etadi...")
# try:
#     url = "http://yoqurl.com"
#     page = requests.get(url)
# except:
#     url = "https://google.com"
#     page = requests.get(url)
#     try:
#         x = page.yoqnarsa
#     except Exception as error_name:
#         print(error_name)  # 'Response' object has no attribute 'yoqnarsa'
