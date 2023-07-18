import time 
import datetime
import calendar

import locale
locale.setlocale(locale.LC_ALL, "UZ_uz") # Ozbek tili uchun 


# locale.setlocale(locale.LC_ALL, "RU_ru") # Rus tili uchun
# time , localtime , sleep


# print(time.time()) # 1970.01.01 hozirgacha otgan sekundlar

# print(time.localtime())

# time.struct_time(tm_year=2023, tm_mon=7, tm_mday=15, tm_hour=14, tm_min=39, tm_sec=6, tm_wday=5, tm_yday=196, tm_isdst=0)
# print(type(time.localtime())) # <class 'time.struct_time'>
# print(len(time.localtime())) # 9
# while True:    
#     our_localtime = time.localtime()

#     year = our_localtime[0]
#     month = our_localtime[1]
#     day = our_localtime[2]
#     hour = our_localtime[3]
#     minute = our_localtime[4]
#     second = our_localtime[5]

#     print(f"Bugun {year}-yil, {month}-oy,{day}-kun") # 2023
#     print(f"soat {hour}:{minute}:{second}")
#     time.sleep(1) # dastur ishini 1 sekundga uxlatish

# today = time.strftime("%d %m %Y")
# print(today) # 15 07 2023
# print(type(today)) # <class 'str'>

# %y > 01-99 yil raqami qisqa
# %Y > 2023 - yil raqami toliq  
# %m > 01-12 Oy raqami 
# %b > jan Oy nomi qisqa
# %B > January Oy nomi toliq
# %d > 01-31 oydagi kun raqami 
# %j > 01-366 yildagi kun raqami 
# %U > 01-53 - hafta raqami 
# %a - Hafta nomi qisqa 
# %A - hafta nomi toliq
# %H - Soat
# %M - Minut
# %S - Sekund
# %c - Sana va vaqt toliq 
# %x - Sana va vaqt toliq 
# print(time.strftime("%x")) # 07/15/23
# print(time.strftime("%H:%M:%S")) # 14:54:31
# print(time.strftime("%A")) # Saturday

# _now = datetime.datetime.now()
# print(_now) # 2023-07-15 15:18:39.587940
# print(_now.date)
# print(_now.day)
# print(_now.month)
# print(_now.year)

# main_time = datetime.timedelta(days=5,hours=10,minutes=30) # 4 haftayu 5 kun 10.30 soat
# active_time = datetime.timedelta(days=3,hours=5)

# print(main_time - active_time) # 2 days, 5:30:00

# task 1
# tugilgan sanangizni kiritib xozirgi vaqt bilan hisoblab necha kun yashaganizni chiqaring

# print(datetime.date(_now.year,_now.month,_now.day) - datetime.date(1995,10,30))


# day = datetime.date.today().day # int day number
# month = datetime.date.today().month # int month number
# year = datetime.date.today().year # int year number

# print(f"Today {day}/{month}/{year}")

# your_brth = int(input(" year ?"))
# print(f"Your age {year - your_brth}")

# cal = calendar.LocaleHTMLCalendar()
# cal = calendar.TextCalendar()
# cal = calendar.HTMLCalendar()
# # print(cal.formatmonth(7))
# print(cal.formatyear(2023))
