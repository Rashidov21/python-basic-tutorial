import json

# import locale
# locale.setlocale(locale.LC_ALL, "UZ_uz")
# Pythonda fayllar bilan ishlash
# open() , with open() as
# f = open("test.txt", "r") # read - faylni o'qish
# f = open("test.txt", "w") # write - faylni yozish
# f = open("test.txt", "a") # append - faylni o'zgartirish
# f = open("test.txt", "x") # faylni yozish uchun ochish agar fayl bo'lmasa xatolik
# f = open("test.txt", "b") # binary - faylni binar rejimda ochish - 0101010
# f = open("test.txt", "t") # text - oddiy text rejimida ochish (doimiy)

# f = open("poem.txt", "w")
# print(type(f))  # <class '_io.TextIOWrapper'>
# print(dir(f))
# print(f)  # <_io.TextIOWrapper name='poem.txt' mode='w' encoding='cp1251'>
# f.close()  # faylga murojaat tugashi bilan uni yopish kerak !
# for method in dir(f):
#     print(method)
# f.write("lorem ipsum dolor sit amet")
# f = open("poem.txt", "w")
# for i in range(10):
#     f.write(f"number = {i}\n")  # yangi qatordan yozish
# f.close()  # faylni yopish
# f = open("poem.txt", "r")  # o'qish rejimida ochish
# print(f.read())  # faylni o'qish
# f.close()  # faylni yopish

# poems = open("poem.txt", "r", encoding='utf-8')
# # print(poems.readlines())  # har bitta yangi qatorni list element qilib oladi
# c = 0
# for x in poems.readlines():
#     if "by" in x:
#         c += 1
# print(c)  # 20
# poems.close()
# print(dir(json))
# json.loads() - json malumotni python dict ga olish
# json.dumps() - python dict nmi jsonga olish

# user = {
#     "name": "John",
#     "age": "23"
# }
# users = []
# users.append(user)
# file = open("users.json", "w")
# # dump python ma'lumotni turini siz ko'rsatgan faylga yozadi
# json.dump(users, file)
# file.close()

# with open("users.json", "r") as users_json:
#     print(users_json.read())  # [{"name": "John", "age": "23"}]


# with open("poem.txt", "r") as file:
#     print(sum([int(x) for i in file.readlines()
#           for x in i.split("=") if i.index(x) % 2 == 1]))
