# STRINGS
# s = "python"
# n_str = str(123456)
# print(type(n_str))  # str
# print(len(s))  # 6
# print(type(len(s)))  # int

# """""" >> doc string


# def test():
#     """This is simple function"""
#     return True


# print(test.__doc__)  # This is simple function

# long_str = """\tTo create a link, \n enclose the link text in brackets \
#     (e.g., [Duck Duck Go])\U0001f600  and then follow it \
#     immediately with the URL in \U0001f600 parentheses (e.g.,\
#         \U0001f600 (https://duckduckgo.com))."""
# print(long_str)

# s = "python"  # index range [0,5]
# print(s[0])  # p
# print(s[10])  # IndexError: string index out of range
# String Slice [start:end]
# a = s[2:]  # 2 index dan to oxiriga qadar qirqish | thon
# a = s[:2]  # 2 index dan to oxiriga qadar qirqish | py
# c = s[1:-2]  # yth
# b = s[-4:-1]  # tho
# z = s[::-1]  # nohtyp
# print(z)
# Formatting strings

# s = "Python is %s pl" % "slow"
# print(s)  # Python is slow pl
# s2 = "Python is {} pl".format("fast")
# print(s2)  # Python is fast pl
# super_fast = "super fast"
# s3 = f"Python is {super_fast} pl"
# print(s3)  # Python is super fast pl

# STRING METHODS
# s = " Python "
# print(len(s))  # 8
# strip - qator boshida va oxiridagi probellarni ochiradi
# print(len(s.strip()))  # 6
# print(len(s.rstrip()))  # 7
# print(len(s.lstrip()))  # 7

# split - siz korsatgan belgi boyicha str ni elementlarga ajratadi (massiv qiladi)
# long_str = "python*js*cpp*html"
# print(long_str.split("*"))  # ['python', 'js', 'cpp', 'html']
# print(long_str.rsplit("*"))  # ['python', 'js', 'cpp', 'html']

# long_str = "python ok \n js ok \n cpp ok"
# splitlines - str ni qatorlar boyicha ajratadi
# print(long_str.splitlines())  # ['python ok ', ' js ok ', ' cpp ok']

# join - massivni str qiladi
# print("".join(long_str.splitlines()).split("\n"))
# ['python ok js ok cpp ok']
