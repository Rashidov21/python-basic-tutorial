# BaseException :
#     1.Syntax Errors - yozishdagi sintaksis xatolar
#     2.Logical errors - mantiqiy xatolar
#     3.On runtime code errors   - dastur ishlayotganda vujudga kelishi mumkin bo'lgan xatolar

# try: # xatolik bo'lishi mumkin bo'lgan kod
#     n = int(input("Integer ?"))
#     print(n)
# except: # xatolik bo'lsa ishlashi kerak bo'lgan kod
#     print("Xatolik yuz berdi lekin ")
#     print("Continue...")
# else: # Xatolik bo'lmasa ishlaydigan kod
#     print("Xatolik yo'q shuning uchun else ishlaydi!")
# finally:# Xar qanday xolatda ishga tushadigan kod
#     print("Xar qanday xolatda ishga tushadigan kod - finally.")
    
# with as 
# with open("./test.txt","r") as file:
#     print(file.read()) # FileNotFoundError

# file = open("./test.txt", "r", encoding="utf-8")
# print(file.read()) # faylni o'qish
# file.close() # faylni yopish

# try:
#     with open("./test.txt","r") as file:
#         print(file.read()) # faylni o'qish
# # except FileNotFoundError as err:
# #     print(f"Error chiqdi - ", err)
# except:
#     raise FileNotFoundError("Bunday fayl topilmadi !") # FileNotFoundError: Bunday fayl topilmadi !


# def avg(ranks):
#     assert len(ranks) != 0, 'Список ranks не должен быть пустым'
#     return round(sum(ranks)/len(ranks), 2)

# ranks = []
# print("Среднее значение:", avg(ranks))
