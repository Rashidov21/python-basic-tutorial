q = lambda l: q([x for x in l[1:] if x <= l[0]]) + [l[0]] + q([x for x in l if x > l[0]]) if l else []

# lst = [x**2 for x in range(10)]


# trick 1

# l = [(x,y) for x in range(3) for y in range(3)]
# print(l) # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# l = []
# for i in range(3):
#     for x in range(3):
#         l.append((i,x))
# print(l)

# # print([x*2 for x in range(1,6)]) # list generator

# # zip 
# print(list(zip("abc","123"))) # [('a', '1'), ('b', '2'), ('c', '3')]

# def get_sum(a,b):
#     if a > b:
#         return a + b
#     else:
#         return b - a

# l = []
# for i in range(1,6):
#     for x in list(range(1,6))[::-1]:
#         l.append(get_sum(i,x))
        
# for i in l:
#     if i > 0:
#         pass
#     else:
#         l.remove(i)
# print(l) # [4, 3, 2, 1, 3, 2, 1, 3, 2, 1, 5, 4, 1, 7, 6, 5, 9, 8, 7, 6]
# func = lambda a , b: a + b if a > b else b - a 
# print(list(filter(lambda x: x != 0,[func(x,y) for x in range(1,6) for y in list(range(1,6))[::-1]])))

# trick 2 
# text = '''
# Call me Ishmael. Some years ago - never mind how long precisely - having
# little or no money in my purse, and nothing particular to interest me
# on shore, I thought I would sail about a little and see the watery part
# of the world. It is a way I have of driving off the spleen, and regulating
# the circulation. - Moby Dick'''
# print(text[9:100])
# t = "tango"
# print(t.replace("t","m")) #mango
# print("m"+t[1:]) # mango
# print()


# matnda har bir qatorda 3 ta belgidan kop bolgan so'zlardan iborat massiv tuzing 

# TASK 2
# shu yozayotgan faylni ochish undagi keyinga qatorga o'tish belgilarini va bosh joylar sonini sanash


# bytes - hom , bit ko'rinishidagi belgilar ketma-ketligi 
# str - bu o'zida unicode belgilarni saqlaydi
# unicode - belgilarni bayt ya'ni 8 ta bit ko'rinishida saqlanishi , (utf-8) 

# x = "1"
# print("True" if x else "False") 

# if x:
#     print("True")
# else:
#     print("false")

# task 
matrix = [ [ 1, 2, 3 ] , [4, 5, 6 ] , [7, 8, 9 ] ]
# massiv ichidagi har bir son uchun lambda funksiya qollang funksiya agar son toq bolsa uni darajasini aks holda kubini qaytarsin, massivni o'zgartrib ekaranga chiqaring . faqat list generator orqali qiling
print([x**2 if x % 2 == 0 else x ** 3 for i in matrix for x in i ])
print(list(map(lambda x: x**2 if x % 2 == 0 else x ** 3, [x for i in matrix for x in i])))