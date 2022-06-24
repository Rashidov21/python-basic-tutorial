import random
# ARRAYS
# list - tartiblangan elementlar ketma-ketligi
# list
# arr = list()
# arr = [1, "str", True, None, range(5)]

# arr2 = list("python") # list(), 1 ta pos arg qabul qiladi
# print(arr)
# print(arr2)
# a , b , c  = [1,2,3]
# print(a) # 1
# print(b) # 2
# print(c) # 3

# list methods
# arr = [1,2,3]
# arr.append(4) # oxiriga elem  qoshadi
# print(len(arr)) #4 >> [1,2,3,4]
# print(arr[0]) # 1
# print(arr[len(arr) - 1]) # 4 >> oxirige elem
# print(arr[-1]) # 4 >> oxirige elem
# print(arr[6]) # IndexError list index  out of range

# a = arr[2:]
# list_copy = arr[:]
# reversed_list = arr[::-1]
# print(a) # [3,4]
# print(list_copy) # arr nusxasi
# print(reversed_list) # arr teskarisi

# long_list = [[1,2,3,],[4,5,6],[7,8,9]]
# print(long_list)

# for i in long_list:
# 	for x in i:
# 		print(x)

# for x in long_list:print(x)
# print([1,2,3] * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3] elem kopaytirish
# print(1 in [2,3,6,4]) # False
# print(6 in [2,3,6,4]) # True

# print([1,2,3] + [4,5,6]) # list larni birlashtirish

# list generators
# beginner
# arr = []
# for i in range(10):
# 	arr.append(i)
# print(arr)
# # junior
# arr = [i for i in range(10)]
# print(arr)
# # middle +
# print(list(range(10)))

# 10 , 100 orasida faqat juft 10 lik olish
# # variant A
# arr = []

# for i in range(1,11):
# 	if i % 2 == 0:
# 		arr.append(i*10)
# arr = [i * 10 for i in range(1 , 11) if i % 2 == 0]
# print(arr)

# arr = [[1,2], [3,4],[5,6],[7,8],[9,10]]

# result_list = []
# for i in arr:
# 	# i = [1,2] yoki [3,4]
# 	for j in i:
# 		# j = 1 yoki 2 ...
# 		if j % 2 == 0:
# 			result_list.append(j * 10)
# # print(result_list) #[20, 40, 60, 80, 100]

# gen_list = [j * 10 for i in arr for j in i if j % 2 == 0]
# print(gen_list)

# summa = 0
# for i in range(1, 11):
# 	if i % 2 == 1:
# 		summa += i
# print(summa) # 25

# print(sum([x for x in range(1, 11,2)])) # 25

# def my_func(elem):
# 	"""return elem * 10"""
# 	return elem * 10

# arr = [1,2,3,4,5]
# print(list(map(my_func, arr))) # [10, 20, 30, 40, 50]


# def get_more_elems(elem1, elem2, elem3):
# 	return elem1 + elem2 + elem3

# a = [1,2,3]
# b = [4,5,6]
# c = [7,8,9]
# print(list(map(get_more_elems,a,b,c))) # [12, 15, 18]


# print(list(zip("abc",[1,2,3] ))) #[('a', 1), ('b', 2), ('c', 3)]

# names = ["john", "mike", "david"]
# # print(list(zip(names, range(1,len(names)+1))))

# # # [('john', 1), ('mike', 2), ('david', 3)]

# users = list(zip(names, range(1,len(names)+1)))
# for username, id in users:
# 	print(f'user = {username} | id = {id}')
# user = john | id = 1
# user = mike | id = 2
# user = david | id = 3


# arr = [1,2,3,4,5]

# for i in arr[::-1]:
# 	print(i)

# for x in range(len(arr)-1,-1, -1):
# 	print(arr[x])

# print(range(-len(arr)+1, 0))


# LIST METHODS

# append , pop, insert, index , count , extend,del , clear
# remove, any, all , in , reverse, sort , join
# arr = [1, 2, 3, 4, 5]
# arr.append(6)  # elem qoshish (oxiriga) [1, 2, 3, 4, 5, 6]
# arr.pop()  # elem ochirish (oxiridan) [1, 2, 3, 4, 5]
# arr.pop(0)  # 0 - indexdagi elem o'chadi
# arr.pop(7)  # IndexError: pop index out of range
# del arr[2]  # [2, 3, 5]
# del arr[7]  # IndexError: pop index out of range
# arr.pop(len(arr) // 2)  # array ortasidagi elem o'chirish
# other_arr = [6, 7, 8, 9]
# extended_arr = arr.extend(other_arr)  # boshqa arr bilan arr nmi kengaytirish
# print(extended_arr)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# arr += [6, 7, 8, 9]  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# arr = [1, 2, 3, 4, 5]
# arr.insert(0, 0)
# [0, 1, 2, 3, 4, 5] - insert bu korsatilgan index ga elem qoshish
# arr.insert(len(arr) // 2, "o'rtasi")
# [0, 1, 2, 'o'rtasi', 3, 4, 5]
# print(arr)

# a_arr = ["yahoo", "yandex", "google"]
# a_arr.remove("yahoo")  # ['yandex', 'google']
# b_arr = [1, 2, 3]
# b_arr.remove(2)  # [1, 3]
# b_arr.remove(6)  # ValueError: element topilmadi
# print(a_arr)
# print(b_arr)

# arr = [1, 2, 3, 4, 5]
# arr.clear()  # elementlarni o'chirib arr ni tozalash
# print(arr)  # []
# index - siz korsatgan elementni index'ini qayataradi
# print(arr.index(3))  # 2
# print(arr.index(5))  # 4
# print(["a", "b", "c", "d"].index("b"))  # 1

# str_arr = list("this method for array")
# count - siz ko'rsatgan elem arr da nechi marta ishtirok etganini qaytaradi
# print(str_arr.count("r"))  # 3

# any , all - 1 ta arg qabul qiladi va  array bo'lishi kerak
# print(any([0, False, None, "", 1]))  # True
# print(any([0, False, None]))  # False
# print(all([1, True, "str"]))  # True
# print(all([1, True, "str", 0]))  # False

# # sum , max, min
# print(sum([1, 2, 3, 4, 5]))  # 15
# print(max([1, 2, 3, 4, 5]))  # 5
# print(min([1, 2, 3, 4, 5]))  # 1

# eng qatta qiymatni topish
# arr = [100, 20, 5, 546, 46, 3, 2314, 565, 1, 0]
# elem_index = arr.index(max(arr))
# print(elem_index)  # 6
# print(arr[elem_index])  # 2314
# o'rta arifmetikni topish
# summa = sum(arr)
# mid_arf = summa / len(arr)
# print(mid_arf)  # 360.0
# arr = [1, 2, 3, 4, 5]
# arr.reverse()  # arr ni teskari qiladi
# print(arr)  # [5, 4, 3, 2, 1]
# print(arr[::-1])  # [5, 4, 3, 2, 1]
# not_sorter_arr = [1, 5, 4, 8, 9, 3, 2, 6]
# sort - elementlarni o'sish tartibida saralash
# not_sorter_arr.sort()
# print(not_sorter_arr)  # [1, 2, 3, 4, 5, 6, 8, 9]
# elementlarni kamayish tartibida saralash
# not_sorter_arr.sort(reverse=True)
# print(not_sorter_arr)  # [9, 8, 6, 5, 4, 3, 2, 1]

# words_arr = ["Python3", "python1", "python"]
# words_arr.sort()
# print(words_arr)  # ['Python3', 'python', 'python1']

# sorted , reversed
# arr = [23, 5, 68, 4]
# a = sorted(arr)
# print(a)  # [4, 5, 23, 68]
# for i in sorted([9, 6, 4, 2, 3, 1, 5]):
#     print(i, end="")  # 1234569
# for i in sorted([9, 6, 4, 2, 3, 1, 5], reverse=True):
#     print(i, end="")  # 9654321

# for x in reversed([1, 2, 3, 4]):
#     print(x, end="")  # 4321

# nums = list(reversed(range(1, 11)))

# print(nums)  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# n = list(range(1, 40))
# result = []
# for i in range(10):
#     x = random.choice(n)
#     if x not in result:
#         result.append(x)

# print(result)  # [10, 18, 39, 1, 26, 35, 7, 32, 6, 9]

# print(random.sample(range(1, 40), 10))  # [18, 28, 38, 37, 2, 32, 1, 20, 9, 19]
