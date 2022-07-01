# Work with date and time
from timeit import Timer
import time  # vaqt bilan ishlash uchun (vaqt obyekti)
# from datetime import datetime  # sanan va vaqt bilan ishlahs uchun
import datetime
import calendar  # kalendar moduli
import locale
locale.setlocale(locale.LC_ALL, "Uz_uz")  # locale ni (dastur tilini)
# o'zbekcha qilish
# date_time_now = datetime.now()  # joriy sana va vaqt
# print(date_time_now)
# print(dir(date_time_now))
# 1656329169.7389219 1970 yil 1-yanvardan boshlab qancha sekund o'tgani
# time_now = time.time()
# gm_time = time.gmtime()
# print(gm_time)
# time.struct_time(tm_year=2022, tm_mon=6, tm_mday=27, tm_hour=11, tm_min=27, tm_sec=40, tm_wday=0, tm_yday=178, tm_isdst=0)

# GMT - buni afrika yevropa ishlatadigan vaqt
# DST - yozgi vaqt
# UTC - butun dunyo boyicha ishlaydigan vaqt zonalari to'plami

# print(datetime.utcnow())  # 2022-06-27 11:32:40.810167
# print(datetime.now())  # 2022-06-27 16:33:00.380261
# Vaqt zonalari ishlash uchun alohida (pytz) kutubxona ishlatish kerak!!!

# print(time.localtime())  # haqiqiy lokal sana va vaqti olish uchun
# time.struct_time(tm_year=2022, tm_mon=6, tm_mday=27, tm_hour=16, tm_min=34, tm_sec=45, tm_wday=0, tm_yday=178, tm_isdst=0)

# lc_time = time.localtime()
# print(lc_time[0])  # 2022
# print(lc_time[1])  # 6
# print(lc_time[2])  # 27


# while True:
#     lc_time = time.localtime()
#     h = lc_time[3]  # soat
#     m = lc_time[4]  # minut
#     s = lc_time[5]  # sekund
#     print(f"{h}:{m}:{s}")
#     time.sleep(1)  # kodni 1 sekundga uxlatish

# u = input("username ?")
# p = input("password ?")
# auth_users = {}

# if u == "admin" and p == "1234":
#     lc_time = time.localtime()
#     y = lc_time[0]
#     m = lc_time[1]
#     d = lc_time[2]
#     h = lc_time[3]  # soat
#     mi = lc_time[4]  # minut
#     s = lc_time[5]  # sekund
#     auth_users.update(
#         {
#             "username": u,
#             "password": p,
#             "register_date": f"{y}/{m}/{d}-{h}:{mi}:{s}"}
#     )
# if len(auth_users) > 0:
#     print(auth_users)
# strftime - string format time
# print(time.strftime("%Y %m %d"))  # 2022 06 27
# print(time.strftime("%H:%M:%S"))  # 16:55:59
# while True:
#     print(time.strftime("%H:%M:%S"))
#     time.sleep(1)

# Qator korinishida sana va vaqtni aks ettirish uchun :
# %y - yil(00-99)
# print(time.strftime("%y"))  # 22
# print(time.strftime("%Y"))  # 2022
# print(time.strftime("%m"))  # 06 - (01-12)
# print(time.strftime("%b"))  # jun
# print(time.strftime("%B"))  # June
# print(time.strftime("%d"))  # 27 - (01 - 31)
# print(time.strftime("%j"))  # 178 - (001 - 366)
# print(time.strftime("%U"))  # 26- (01 - 54)
# print(time.strftime("%W"))  # 26- (01 - 54)
# print(time.strftime("%w"))  # 0- (0 - 6)
# print(time.strftime("%a"))  # Mon
# print(time.strftime("%A"))  # Monday
# # Vaqt
# print(time.strftime("%H"))  # soat
# print(time.strftime("%M"))  # minut
# print(time.strftime("%S"))  # sekund
# print(time.strftime("%I"))  # soat (12 soatlik formatda)
# print(time.strftime("%x"))  # sana  joriy locale dagisi
# print(time.strftime("%X"))  # vaqt joriy locale dagisi
# print(type(time.strftime("%Y %m %d")))  # <class 'str'>


# print(time.strftime("%A"))  # dushanba
# print(time.strftime("%A").title())  # Dushanba

# tm_now = "%A %d-%B soat - %H:%M:%S"
# print(time.strftime(tm_now))  # dushanba 27-Iyun soat - 17:10:28
# print(time.strftime("%x / %X"))  # 27/06/2022 / 17:11:00
# print(time.strftime("%z"))  # +0500


#  task 2
#  arr = [[1,5,6],[5,8,1], [9,7,9],[1,2,8]]
#  newArray = []
#  rezultat >>> newArray = [25,14,12,11] ni xosil qiling


# arr = [12, 5, 6, 9, 8, 2, 6, 6, 3, 4, 58, 6, 7]
# _from = arr.index(min(arr))
# _to = arr.index(max(arr))
# print(arr[_from:_to])  # [2, 6, 6, 3, 4]

# arr_2 = [2, 3, 5, 96, 8, 1]

# max_elem = max(arr_2)
# min_elem = min(arr_2)
# arr_2[arr_2.index(min_elem)] = max_elem
# arr_2[arr_2.index(max_elem)] = min_elem

# print(arr_2)


# print([x * 3 for x in range(0, len(list(range(1, 16))), 3)])
# print(len([x * 3 for x in range(0, len(list(range(1, 16))), 3)]))
#######################################################################
# import datetime
# t1 = datetime.timedelta(
#     days=5, hours=10, minutes=30)  # vaqt oraligi obyekti
# t2 = datetime.timedelta(days=3, hours=5, minutes=20)
# print(t1 - t2)  # 2 days, 5:10:00
# days - kunlar butun sonlarda
# minutues - minutlar butun sonlarda
# milliseconds - millisekundlar butun sonlarda
# weeks - haftalar butun sonlarda

# y = int(input("Year "))
# m = int(input("Month "))
# d = int(input("Day "))
# brthday = datetime.date(y, m, d)
# td = datetime.date.today()
# print(td.year)  # 2022
# print(td.month)  # 07
# print(td.day)  # 01
# print(td)  # 2022-07-01
# print(td - brthday)  # 7189 days, 0:00:00
# d = datetime.date(2022, 7, 1)  # sana  obyekti
# print(d)  # 2022-07-01
# print(type(d))  # <class 'datetime.date'>


# dt = datetime.datetime(2002, 10, 25, hour=11, minute=23, second=30)
# print(dt)  # 2002-10-25 11:23:30


# print(dt.date())  # 2002-10-25
# print(dt.time())  # 11:23:30

# y = int(input("Year "))
# m = int(input("Month "))
# d = int(input("Day "))
# h = int(input("Hour "))
# minute = int(input("Minute "))

# bth = datetime.datetime(y, m, d, hour=h, minute=round(minute))
# td = datetime.datetime.now()
# print(td - bth)
# import calendar
# c = calendar.LocaleTextCalendar(0, "UZ_uz")
# print(c.formatyear(2022))  # <class 'str'>
# with open("calendar.txt", "w") as file:
#     file.write(c.formatyear(2022))

# html_calendar = calendar.LocaleHTMLCalendar(0, "UZ_uz")  # Russuin_Russia.1251
# with open("calendar.html", "w") as file:
#     file.write(html_calendar.formatyear(datetime.datetime.now().year))


# ['dushanba', 'seshanba', 'chorshanba', 'payshanba', 'juma', 'shanba', 'yakshanba']
# print([i for i in calendar.day_name])
# print([i for i in calendar.day_abbr])
# # ['', 'Yan', 'Fev', 'Mar', 'Apr', 'May', 'Iyn',
# # 'Iyl', 'Avg', 'Sen', 'Okt', 'Noy', 'Dek']
# print([x for x in calendar.month_abbr])
# # ['', 'Yanvar', 'Fevral', 'Mart', 'Aprel', 'May', 'Iyun', 'Iyul', 'Avgust', 'Sentabr', 'Oktabr', 'Noyabr', 'Dekabr']
# print([x for x in calendar.month_name])


# Timer >> stmt - bu tezligini o'lchanishi keral bo'lgan kod
# Timer >> setup - bu tezligini o'lchashdan oldin ishga tushirilishi bo'lgan kod
# Timer >> timer - bu tezligini o'lchanishi keral bo'lgan kod
# code1 = """\
# i , j = 1,0
# while i < 10001:
#     j += 1
#     i += 1
# """
# t1 = Timer(stmt=code1)
# print("while : ", t1.timeit(number=10000))
# code2 = """\
# j = 0
# for i in range(1,10001):
#     j += 1
# """
# t2 = Timer(stmt=code2)
# print("for: ", t2.timeit(number=10000))
# code3 = """\
# j = sum(range(1,10001))
# """
# t3 = Timer(stmt=code3)
# print("sum : ", t3.timeit(number=10000))
