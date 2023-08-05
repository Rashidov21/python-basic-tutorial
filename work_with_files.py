from os import path 
# ореn(<faylga olib boruvchi yol>[, mode='r']n buffering=-l][, encoding=None][, 
# errors=None][, newline=None][, closefd=True])


print(path.abspath("./test.txt")) # C:\Users\rashi\Documents\GitHub\python-basic-tutorial\test.txt

file_path = path.abspath("./test.txt")

file = open(file_path, "r", encoding="utf-8")
print(file.read()) # oqish
print(file.readline()) # qatorlarni alohida alohida oqiydi
print(file.readlines()) # o'qib har bir qatorni alohida massiv elementi qilib olasi 
file.close()
