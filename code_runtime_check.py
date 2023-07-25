from timeit import Timer

code = """
# a = []
# i = 0
# while i < 10**6:
#     i += 1
#     a.append(i)
a = [i for i in range(10**6)]
"""

tl = Timer(stmt=code)
print("while: ", tl.timeit(number = 10))




