# import json
# from bs4 import BeautifulSoup
# from mod1 import activate
# import intro
# print(intro.USER)  # ModuleNotFoundError: No module named 'intro'
# import mod1  # bu modulni yoki to'liq yuklash
# print(mod1.activate) # True

# from mod1 import *  # bu modulni ichidagi hamma narsani yuklash
# print(plus(10, 20))


# from mod1 import activate  # bu aniqlik bilan yuklash
# print(activate)  # True
# from mod1 import AGE, long_str, plus
# as - bu modul yoki o'zgaruvchini boshqa nom bilan yuklash
# from bs4 import BeautifulSoup as bs
# from mod1 import (AGE, long_str,
#                   plus, activate)

# print(AGE)

# soup = bs()

# from math import pi, floor, ceil
# print(pi)  # 3.141592653589793
# print(ceil(12.3))  # 13
# import os
# import sys
# print(os.path)  # python o'rnatilgan fayl yo'li
# print(sys.path)  # modullarni fayl yo'llarini list ko'rinishida olish
# print(os.path.abspath(__file__))  # shu faylni absalutniy fayl yo'li

# print(os.path.dirname(__file__))
# print(__file__)  # mod2.py
# print(__name__)  # __main__
# bu kod modul o'zi ishga tushganmi yoki uni import qilinganmi aniqlaydi
# if __name__ == "__main__":
#     print("OK")
