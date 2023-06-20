# for loop 
# range - diapazon , oraliq  
# range(start,stop,step)
# range(1,10,2) >> 3,5,7,9,11

# print(range(1,10,2)) # range(1, 10, 2)
# print(type(range(1,10,2))) # <class 'range'>

# for i in range(10):print(i)

# for i in range(1,10,2):
#     print(i)
# print(1)
# print(2)
# print(3)

# for i in "text":
#     print(i)
#     if i == "t":
#         print(i*2) # IndentationError
# else:
#     print("for loop end")

# k = 5
# n = int(input("N"))
# if n > 0:
#     for i in range(n):
#         print(k)


# while 

# i = 100
# while i:
#     i -= 1
#     print(i)
    
# while True:
#     print("hello world")

# for i in range(10):
#     if i % 2 == 0:
#         continue # keyingi iteratsiyaga o'tish
#     if i == 7:
#         break # tsikldan chiqish
#     print(i)
    
# i = 0
# while True:
#     i += 1
#     if i > 50:
#         if i % 2 == 1:
#             continue
#     if i > 100:
#         break
#     print(i)

# task 1
# while orqali userdan sonlar qabul qiling va kiritgan sonlarini yigindisini hisoblab boring , agar user "stop" deb kiritsa dastur toxtasin va sonlar yigindisi ekranga chiqsin

# summa = 0
# while True:
#     user = input("Son kirit ?")
#     if user == "stop":
#         break
#     summa += int(user)
# print(summa)