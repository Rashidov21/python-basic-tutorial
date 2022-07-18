# DICTS
# dict - obyektlar to'plami , va qiymatlarga kalit orqali murojaat qilinadi
# kalitlar doim string bo'lishi shart
# d1 = dict(name="number", value=10)
# d2 = {
#     'name': "number",
#     "value": 10,
#     "username": "mahatma"
# }
# print(d1)
# print(d2)

# print(d1.get("name"))  # number * 1- usul
# print(d1["name"])  # number 2-usul
# print(d1["color"])  # KeyError: 'color'
# print(d1.get("color"))  # None
# print(d1.name)  # Error

# user = {
#     "name": "John",
#     "surname": "Doe",
#     "age": 30,
#     "skills": ["python", "python-django"]
# }
# print(user.get("salary", 15000))  # 15000
# print(user.get("address", "undefined"))  # undefined

# del user["age"]
# print(user)
# # {'name': 'John', 'surname': 'Doe', 'skills': ['python', 'python-django']}

# for key in user.keys():  # dict kalitlarini dict_keys qilib qaytaradi
#     print(key)
# print(list(user.keys()))
# ['name', 'surname', 'age', 'skills']
# print(tuple(user.keys()))
# ('name', 'surname', 'age', 'skills')

# for x in user.items():  # dict elementlaridan iborat tuple qayataradi
#     print(x)

# for x in user.values():  # dict elementlarini qiymatlarini
#     print(x)


# user2 = user.copy()  # nusxasini olish
# user.update({"salary": 150})  # boshqa dict bilan yangilash


# print(user.pop("name"))  # dict dan kalit boyicha oladi
# print(user.pop("address"))  # KeyError
# Agar 2 - param ko'rsatilsa Error o'rniga
# print(user.pop("address", "Michigan, Alabama"))
# qiymatni qaytaradi
# print(user.popitem())  # dict oxirgi elementini qaytaradi
# user.clear()
# print(user)  # {}
# t = (1,)
# users = [
#     {
#         "name": "John",
#         "age": 30,
#         "family": (
#             {
#                 "name": "Sara",
#                 "position": "Mother"
#             },
#         )
#     },
#     {
#         "name": "Mike",
#         "age": 12
#     },
#     {
#         "name": "David",
#         "age": 20
#     }
# ]
# for user in users:
#     print(user["name"])
#     print(user["age"])

# task 1
# n = [1, 2, 3, 4, 5]
# u = ("a", "b", "c", "d", "e")
# d = {
#     "a":1,
#     "b":2
# }


# d = {}
# d = dict()
# key + value
# name = "John"
# surname = "Doe"
# d = {
#     'n': name,
#     's': surname
# }

# print(d["n"])
# print(d.get("s"))

# for i in d.items():
#     print(i)

# for x in d.keys():
#     print(x)

# for j in d.values():
#     print(j)
# import random
# key_list = "abcdef"
# value_list = random.sample(range(100), 6)
# my_dict = {k: v for k, v in zip(key_list, value_list)}
# print(my_dict)
# res = {}
# values = sorted(my_dict.items(), key=lambda v: v[1])
# for i in values:
#     res.update({f"{i[0]}": i[1]})
# print([x for x in res.values()])

# print([i for i in map(lambda x: x+2, res.values())])


# def main(x):
#     return x + 2


# print([i for i in map(main, res.values())])


# def filter_main(x):
#     if x >= 30:
#         return x


# print([i for i in filter(filter_main, res.values())])
# my_dict.update({"g": 7})  # dictga elem qoshish uchun kerak

# other_dict = {}

# for i in my_dict.items():
#     other_dict.update({k: v for k, v in zip(
#         my_dict.keys(), my_dict.values()) if v <= 50})

# print(other_dict)

# Mastercard, Paul Cooper, 2700140577577268, 11/23, CVV: 167
# Mastercard, Joseph Ho, 2511543921731250, 07/30, CVV: 924
# Mastercard, Kimberly Jackson, 5203932397901099, 09/30, CVV: 090
# Mastercard, Melissa Wilson, 2392633210200184, 12/22, CVV: 119
# Mastercard, Maria Holmes, 2720362817102568, 12/22, CVV: 377
# Mastercard, John Campbell, 2245927560784089, 12/23, CVV: 453
# Mastercard, Rebecca Anderson, 5503991835969990, 04/25, CVV: 597
# Mastercard, Aaron Barron, 5118831594337780, 08/24, CVV: 052
# Mastercard, Kristin Jimenez, 2445566370760125, 01/26, CVV: 174
# Mastercard, Danielle Eaton, 5321732292333381, 12/30, CVV: 877

# ushbu ro'yhatdan 10-oydan kichik bo'lgan kartalarni alohida dict ga yozings
