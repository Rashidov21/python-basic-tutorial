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