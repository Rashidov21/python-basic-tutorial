# -*- coding: utf-8 -*-
import json 
from openpyxl import load_workbook

file = load_workbook("./students_result.xlsx") 
data = file.active

student_results_list = [_ for _ in data.values][1:18]
cleaned_data = []

for i in student_results_list:
    print(i[2])
    cleaned_data.append(
        {
            "id":i[0],
            "name":i[1],
            "right_answer":i[2],
            "point":round(int(i[2])*3.3,2)
        }
    )
    
with open("student_res_jsondata.json", "w+") as st_res_jsondata:
    jd = json.dumps(cleaned_data)
    st_res_jsondata.write(jd)
 
# from os import path 
# ореn(<faylga olib boruvchi yol>[, mode='r']n buffering=-l][, encoding=None][, 
# errors=None][, newline=None][, closefd=True])


# print(path.abspath("./test.txt")) # C:\Users\rashi\Documents\GitHub\python-basic-tutorial\test.txt

# file_path = path.abspath("./test.txt")

# file = open(file_path, "r", encoding="utf-8")
# print(file.read()) # oqish
# print(file.readline()) # qatorlarni alohida alohida oqiydi
# print(file.readlines()) # o'qib har bir qatorni alohida massiv elementi qilib olasi 
# file.close()

# task 1 
# Berilgan  massivlardan ichidagi takrorlangan elementlarni yangi massivga tartiblab chiqaring 
# input : a = [[1,2,3],[4,5,6,1],[7,8,9,1]]
# output : b =[[1,1,1],[6,6],[7,7]]

# f = open() 

# with open("./test.txt", "r") as file:
#     print(file)
    
# with open("./phone_data.json", "r") as json_file:
    # print(json_file.read())
    # print(type(json_file)) # <class '_io.TextIOWrapper'>
    # print(dir(json_file)) #

    
# JSON - Javascript Object Notation