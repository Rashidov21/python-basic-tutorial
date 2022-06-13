# LOOPS
# while , for in
# count_chars = len("javascript")  # 10
# print(type(count_chars))  # class int
# print(count_chars + 2)  # 12
# for i in "python":
#     # print(i)
#     print(2 * 2)


# len(), range()
# range() - 0 dan siz korsatgan songa qadar sonlar diapazoni
# for i in range(len("python")):
#     print(i)

# for x in range(20, 50):
#     print(x)

# range(start, stop, step)

# range(0, 7, 3)  # 0,3,6
# print(type(range(len("str"))))  # <class 'range'>
# for k in range(20, 0, 2):
#     print(k)

# for i in "str":
#     print(i)

# for x in range(3):
#     i = int(input())
#     if i == 5:
#         print("OK")
#     else:
#         print("ERROR")

# s = input()
# for i in range(len(s)):
#     if s[i] == "a":
#         print("OK")
# for i in range(10):
#     print(i, end="")
# else:
#     print("For tugadi")
# task 1
# input : 0 , 20 number
# output : 0 , 20  juft sonlar kvadrati

# while
# control = True
# while control:
#     u = int(input())
#     if u == 7:
#         break
#     else:
#         continue
#     print(u)
# i = 101
# while i > 0:
#     i -= 1
#     print(i)
# task 2
# input : userdan str qabul qiling agar str "stop" ga teg bolsa
# sikl toxtedi
# keyin user kiritgan barcha sonlarni yigindisi chiqadi
# output: ~ 56
# summa = 0
# while True:
#     s = input("Kiriting >>")
#     if s == "stop":
#         break
#     else:
#         try:
#             summa += int(s)
#         except ValueError as error:
#             print("Raqam kirit! Qo'chqor!")
#             continue

# print(f"Yig'indi = {summa}")
# task 3 #for in
# input: "abc123"
# output: 123
# s = input("yoz >> ")  # str
# nums = "0123456789"
# result = ""
# for i in s:
#     if i in nums:
#         int_num = int(i)  # butun son qilish
#         result += i
# print(result)

# import re
# CHECK_RE = re.compile('[a-zA-Z]')

# while True:
#     s = input()
#     if CHECK_RE.search(s):
#         print("OK")
#         if s == "a":
#             break
#     else:
#         print("ERR")
# input()

# task 4
# input: userdan 3 num qabul qiling
# output: start , stop, step | 2 , 10, 3 >> 2 , 3 , 8
# start = int(input())
# stop = int(input())
# step = int(input())
# for i in range(start, stop, step):
#     print(i, end="")
# 0
# 10
# 2
# 02468
