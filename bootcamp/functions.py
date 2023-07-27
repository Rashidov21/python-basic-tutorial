# import keyword
# print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# function - harakat 

# len() , range() , max() , min(), print() , zip() , filter() , sorted()
# l = len
# print(l("12345")) # 5

# def plus(num1,num2):
#     """summa 2 sonni"""
#     # print(num1 + num2)
#     return num1 + num2
# print(plus.__doc__) # summa 2 sonni

# print(len.__doc__) # Return the number of items in a container.
 

# res = plus(2,2)
# print(res)

# def main():
#     pass 

# print(main)  # <function main at 0x00000243F30E8A60>


# def get_user(name,email,password=None):
#     print(name)
#     print(email)
#     print(password)
#     return True 

# get_user("John",'johndoe@gmail.com','john123')
# get_user('johndoe@gmail.com','john123',"John")
# get_user('johndoe@gmail.com','john123') # TypeError: get_user() missing 1 required positional argument: 'password'
# get_user("Nathan","nat@mail.ru")


# a,b,c = 1,2,3
# print(a+b+c) # 6

# x,y,z = 1,2,3,4,5 # ValueError: too many values to unpack (expected 3)
# x,y,*z = 1,2,3,4,5, "six", False , [1,2,3] # 
# print(x,y,z) #  1 2 [3, 4, 5, 'six', False, [1, 2, 3]]

# def main(*args):
#     print(args) # 1 2 [3, 4, 5, 'six', False, [1, 2, 3]]
#     print(type(args)) # <class 'tuple'>
#     return len(args) # 8

# print(main(1,2,3,4,5, "six", False , [1,2,3]))

# def check_password(username,password):
#     if username == "chaplin" and password == "1234":
#         print('Welcome !')
#         return True 
#     else:
#         print("Authorization fail !")
#         return False 

# check_password(username='chaplin', password='1234')

# *args, **kwargs
# def user_kwargs(**kwargs):
#     print(kwargs)# {'username': 'chaplin', 'password': '1234', 'name': 'john'}
#     print(type(kwargs)) # <class 'dict'>
#     if kwargs.get("username") == "chaplin" and kwargs.get("password") == "1234":
#         print('Welcome !')
#         return True 
#     else:
#         print("Authorization fail !")
#         return False 
# user_kwargs(username="chaplin", password="1234", name="john") # Welcome !

# def super_func(*args, **kwargs):
#     for i in args:
#         print(i)
#     for k in kwargs.items():
#         print(k)
#     return True
# super_func(1,"some string", False, name="john", age=20)

# def arrow_main(x,y):
#     return x * y
# print(arrow_main(round(2.3), 10)) # 

# task 1 
# userdan son qabul qiling agar son toq bolsa uni darajasini qaytaradigan funksiya ishga tushadi agar juft  bolsa uni 2 ga qo'shib yig'indisini qaytaradigan funksiya ishga tushadi  

    
# task 2
# userdan qabul qilingan qiymat  faqat raqamlardan iborat bo'lsa, uni ikkiga ko'paytiring

# task 3
# userdan qabul qilingan qiymatlarni tekshiring ichidan  faqat raqamlarni  ikkiga ko'paytiring va yig'indini qaytaring
# input: "str", 2, False, 4
# output: 12

# task 4
# userdan kalit hamda qiymat korinishidan ma'lumotlar qabul qiling ularni kamayish tartida saralab alohida massivda qaytaring 

# input: a=30, b=50,c=10
# output: [('b',50),('a',30),('c',10)] 

def sorted_values(**kwars):
    res = [i for i in kwars.items()]
    res = sorted(res, key=lambda x : x[1], reverse=True)
    return res
    
print(sorted_values(a=30, b=50,c=10)) # [('b', 50), ('a', 30), ('c', 10)]
    
x = lambda **kwargs: [sorted(kwargs.items(), key=lambda x : x[1], reverse=True)]
print(x(a=30, b=50,c=10)) # a=30, b=50,c=10