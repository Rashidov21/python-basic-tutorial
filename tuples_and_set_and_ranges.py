# TUPLE kortej
# t = tuple()
# t = ()
# tuple - - tartiblangan o'zgarmas elementlar ketma-ketligi
# t = (1, 2, 3, 4, 5)
# for i in t:
#     print(i)
# t[0] = 0  # TypeError: 'tuple' object does not support item assignment
# print(t[0])  # 1
# print(t[1])  # 2
# print(t[2])  # 3

# tuple methods
# len(), min(), max(), index(), count()
# users = [
#     ("pablo10", "passwordpablo"),
#     ("mahatma122", "qwert123"),
#     ("john10333", "rtyy22"),
# ]

# set - ko'plik
# set - tartibsiz unikal elementlar ketma-ketligi
# s = set()
# s = {}
# st = "Python"
# print(set(st))
# {'h', 'y', 'n', 'o', 'P', 't'}
# {'t', 'P', 'y', 'o', 'n', 'h'}
# n = set("1222333")
# print(n)  # {'2', '1', '3'}
# for x in n:
#     print(x)

# set methods
# s1 = set([1, 2, 3, 4])
# s2 = set("abcd4")
# print(s1.union(s2))  # {1, 2, 3, 4, 'b', '4', 'a', 'c', 'd'}
# union - list dagi extend ga oxshaydi , biror bir set ni boshqa bir set bilan
# birlashtiradi
# s1.update(set([5, 6]))  # mavjud set ga element qoshish
# print(s1)  # {1, 2, 3, 4, 5, 6}
# print(set("abc") == set("abc"))  # True
# print(set("abc") == set("abe"))  # False
# print("s" in set("salom"))  # True
# print("n" not in set("salom"))  # True
# print(s1.isdisjoint(set([5, 6, 7])))  # True
# print(s1.isdisjoint(set([5, 6, 4])))  # False

# s_copy = s1.copy()  # set ni nushalash
# print(s_copy)  # {1, 2, 3, 4, 5, 6}
# s1.add(7)  # add bu element qoshish
# print(s1)  # {1, 2, 3, 4, 5, 6, 7}
# s1.remove(7)
# print(s1)  # {1, 2, 3, 4, 5, 6}

# s1.remove(8)  # s1.remove(8) KeyError: 8
# s1.discard(2)  # agar ko'rsatilgan element set da bor bo'lsa
# uni o'chiradi bo'lmasa hech qanday xatolik yuzaga kelmaydi
# s1.pop()  # boshidan bitta elementni o'chiradi
# s1.clear()  # set ni tozalash
# print(s1)
# a = {x for x in [1, 2, 3, 3, 6, 6, 4] if x % 2 == 0}
# print(a)  # {2, 4, 6}

# frozenset
# frozenset - set bilan bir xil faqat o'zgarmas unikal elementlar ketma-ketligi
# print(frozenset([1, 2, 3, 3, 6, 6]))  # frozenset({1, 2, 3, 6})

# range
# print(range(10))  # range(0, 10)
# print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(set(range(10)))  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# print(tuple(range(10)))  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
