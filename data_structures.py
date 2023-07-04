# list , tuple , set , frozenset , dict 

# list - tartiblangan elementlar toplami 
# tuple - o'zgarmas tartiblangan elementlar toplami
# set - unikal elementlar toplami 
# frozenset - o'zgarmas unikal elementlar toplami 
# dict - kalit va qiymat usulida saqlanadigan elementlar toplami 

# data type - malumot turi
# a = 10 
# data structure - malumotlarni ma'lum bir usulda saqlash

# list - Massivlarni dinamik korinishi  (Ro'yhat)
# a = [10,20,"teen"]
# l = list("Hello")

# print(a) #  [10,20,"teen"]
# print(l) # ['H', 'e', 'l', 'l', 'o']

# a = []
# for i in range(1,11):
#     a.append(i)
    
# print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# print(list(range(1,11))) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# arr = list(range(1,11))
# arr[0] = -1
# print(arr)  # [-1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# s = "helloos"
# s[-1] = "o"

# l = list(s)[-1] = "o"
# print(f"{''.join(list(s)[:-1])}"+"".join(l))



# t = tuple()
# t = (1,2,(2,3), True,"none")
# print(t[2])
# s = t[0] = 1
# print(s)
# print(type(t)) # <class 'tuple'>


# List generators 

# for i in range(5):print(i)


# print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# s = "pythonjon"
# arr = [x for x in s if x == 'o']
# print("".join(arr))