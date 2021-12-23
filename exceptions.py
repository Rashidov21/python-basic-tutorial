# Exception - Dastur davomida vujudga kelgan xatoliklar haqida bildirishlar
# 1- SyntaxError - dasturda sintaksis xatolik (yozma)
# 2- Mantiqiy - dastur mantigidagi xatolik
# 3- Bajarish vaqtidagi xatoliklar

# try except else finally
# x = 1 / 0
# try:
#     x = 1 / 0
# except ZeroDivisionError as zr:
#     print("Error", zr)
#     x = 0
# print(x)

# n = int(input())
# print(n)
# try:
#     n = int(input()) # xatolik bor kod
# except:
#     print("Xatolik") # xatolik bolsa ishlaydigan kod
# else:
#     print("Xatolik yoq") # xatolik bolmasa ishlaydigan kod
# finally:
#     print("Farqi yo ishlaydi") # xatolik bolsa-bolmasa ishlaydigan kod
#
# print("Davom etadi")
# # BaseException
# try:
#     x = 1 / 0
# except:
#     # raise ArithmeticError("1 , 0 ga bolinmedi")
#     raise ArithmeticError
# try:
#     x = -3
#     assert x >= 0, "Xatolik infosi"
# except AssertionError as err:
#     print(err)

# assert 10 > 1 # ifoda True bolsa gap yoq
# assert 10 < 1 # ifoda False AssertionError vujudga keladi
# print()

# print(x)
# try:
#     n = int(input())
# except (ValueError, NameError):
#     print("Xatolik...")

# try: # Xatolikni qidiradi
#     x = 1 / 0.5
# except ZeroDivisionError as error: # xato bosa qilinishi kerak bolgan ishlar
#     print(error)
# else: # xato bomasa qilinishi kerak bolgan ishlar
#     print("else Block")
# finally: # har doim qilinishi kerak bolgan ishlar
#     print("Block finally ... every time!")
