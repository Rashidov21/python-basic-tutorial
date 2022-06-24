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
