# pip install faker 
from faker import Faker

fake = Faker() # faker object exampleTag.objects.all()

# print(dir(fake))
# print(fake.user_agent())
# print(open(fake.image(), "r", encoding="utf-8"))
# print(fake.name())
# print(fake.text())
# print(fake.text(1500))
# print(fake.address())
# print(fake.phone_number())

# for i in range(10):
#     print(fake.name())

# task 1 
# user.db faylini hosil qiling , unda users_data nomli table oching va 
# ism , familya ,username , yosh, jins , shahar , kocha nomi , telefon raqami , rang , email , sayt manzili
# nomlarini saqlovchi ustunlar hosil qiling va 30 ta fake user ma'lumotlari bilan omborni to'ldiring 

# enumerate 

# data = ((1,2),(3,4),(5,6))
# for i,k in enumerate(data):
#     print(i) # data indexes
#     print(k) # data item
    
# arr = [1,2,3,4,5]
# for i,k in enumerate(arr):
#     print("list item index = ", i)
#     print("list item = ", k)

# task 2
# 10 ta tasodify sondan iborat massivda agar 7 raqami mavjud bolsa uni 70 ga o'zgartring , yangi massiv hosil qilinmaydi

# import random
# arr = [random.randint(1,30) for i in range(10)]
# print(arr)
# for i,k in enumerate(arr):
#     if k == 7:
#         arr[i] = 70
#         print("yes")
# print(arr)

# task 3
# Faker yordamida 500 ta tashkilot ma'lumotlarini DB'sini tuzing 
# tashkilot nomi , manzili , telefoni , sayt manzili , emaili,pochta indeksi , kocha nomi va tashkilot haqida qisqa matnli fake ma'lumotlar bolishi kerak