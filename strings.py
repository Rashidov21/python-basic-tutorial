# ASCII - american code for information interchange
# A - 72

# len() >> int count letters

# s = "Python"
# print(len(s)) # 6
# print(len(s) * 2) # 12

# print(s[0]) # P
# print(s[1]) # y

# for i in s:
#     print(i, end="") #Python

lang = "Python"

# print(lang[0]) # P
# print(lang[len(lang)-1]) # n

# print(lang[-1]) # n

# print(lang[0:2]) # Py - :2 ikkinchi indexgacha qirqish

# s = "Python best of the best!"
# print(s[7:12]) #best
# print(s[7:]) #best of the best!
# print(s[:-1])
# s2 = s[:] # copy string
# print(s2) #Python best of the best!

# print(s[::-1]) # !tseb eht fo tseb nohtyP

# num = 10
# s = "Your number is %s" %num
# s = "Your number is {0} = {1}".format(num,5)
# s = f"Your number is {num*2}"
# print(s) # Your number is 20

# String method
# Object 
#     Attribute - qanday,qanaqa ... *(sifat)
#     Method - nima qiladi ? ... *(harakati)

# s = "Javascript and Python"
# print(s.center(15)) # markazga tekislash
# print(s.ljust(5)) # left 
# print(s.rjust(5)) # right

# print(ord("A")) # 65
# print(chr(65)) # H

# s = "\nJavascript and Python\n"
# print(len(s)) #23
# print(len(s.strip("\n"))) #21
# print(len(s.lstrip("\n"))) #22
# print(len(s.rstrip("\n"))) #22

# s = 'Javascript and Python'
# print(s.split()) # ['Javascript', 'and', 'Python']
# s = 'Javascript\tand\tPython'
# print(s.split('\t')) # ['Javascript', 'and', 'Python']
# print(s.rsplit('\t')) # ['Javascript', 'and', 'Python']
# more_text = "Lorem ipsum\n \
# dolor amet \n \
# sit color"

# # print(len(more_text))
# print(more_text)
# print(more_text.splitlines()) # ['Lorem ipsum', ' dolor amet ', ' sit color']

# print("".join(["a",'A',"b","B"])) # aAbB
# print("-".join(["a",'A',"b","B"])) # a-A-b-B

# task 1
# user kiritgan sonlar orasidagi barcha sonlarni toq va juft ekaniga qarab alohida alohida string ga yozing 

# n1 = int(input())
# n2 = int(input())

# odd = ""
# even = ""

# for i in range(n1,n2+1):
#     if(i%2==0):
#         even += f"{i},"
#     else:
#         odd += f"{i},"
# print(odd.strip(',') , even.rstrip(','))

# s = "Hello world in Python"
# print(s.find("world")) #6
# print(s.find("open")) #-1

# s = "hello"
# print(s.index('l'))
# print(s.index('t')) # ValueError: substring not found


# s = "Hello world"
# print(s.count("l")) # 3
# print(s.count("u")) # 0


# parser_text = """Python api basic framework django rest full api fast api tarnado parler 
# silk debug tool bar rest api"""

# s = "Javascript"
# print(s.startswith("java")) # False
# print(s.startswith("Java")) # True

# print(s.endswith("pt")) # True


# print(s.replace("Java", "Type")) # Typescript


# s = "ab12"
# print(s.isalnum()) # True
    # isalpha() - faqat harflar
    # isdigit() - faqat butun sonlar
    # isdecimal() - faqat 10 lik sanoq tizimidagi sonlar 
    # isnumeric() - faqat sonli belgi
    # isupper() - Faqat katta harflar
    # islower() - Faqat kichik harflar
    # istitle() - Birinchi harfi katta
    # isspace() - qatordagi bosh joylar faqat probel






# task 1
    # task 1.1
    # Berilgan matnda eng kop ishtirok etgan sozni toping 
    # task 1.2
    # Eng kop ishtirok etgan sozni 'baqlajon' so'ziga almashtiring

