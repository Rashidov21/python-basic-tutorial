# SQL - Structed Query Language
# SQL - Jadval

# NoSQL - Not Only SQL
# NoSQL - key + value ko'rinishida saqlash


import sqlite3

con = sqlite3.connect("./customers.db")  # db ga boglanish
cur = con.cursor()  # db ni boshqarish obyekti

# sql_command_1 = """
#     CREATE TABLE customers(
#       customer_id INT PRIMARY KEY,
#       customer_name TEXT,
#       customer_address TEXT,
#       customer_country TEXT
#     );
# """
# sql_command_2 = """
#     INSERT INTO customers
#     VALUES(1,'John','New York','USA');
# """
# try:
#     cur.execute(sql_command_2)  # execute - sql buyruqlarimi amalga oshirish
# except sqlite3.DatabaseError as error:
#     print(error)
# else:
#     con.commit()  # o'zgarishlarni tasdiqlash
#     cur.close()  # boshqaruv obyektini yopish
#     con.close()  # bog'lanishni uzish
#     print("Success")

# names = ["mike", "david", "sara"]
# addreses = ["Texas", "Nevada", "LA"]
# countries = ["USA", "USA", "USA"]
# for i in range(3):
#     try:
#         cur.execute(f"""
#             INSERT INTO customers
#             VALUES({i+2},'{names[i]}','{addreses[i]}','{countries[i]}');""")
#     except sqlite3.DatabaseError as er:
#         print(er)
#     else:
#         con.commit()

#         print("Success !")
# else:
#     cur.close()
#     con.close()
#     print("tugadi")

# query_1 = """SELECT * FROM customers WHERE customer_id=2"""
# query_2 = """SELECT * FROM customers"""


# all_items = cur.execute(query_2).fetchall()
# print(all_items)
# berilgan so'rov boyicha barcha obyektlar
# one_item = cur.execute(get_one_item).fetchone()
# berilgan so'rov bo'yicha 1 ta obyekt
# many_items = cur.execute(get_one_item).fetchmany()
# berilgan so'rov boyicha bir nechta obyektlar

# print(all_items)  # [(2, 'mike', 'Texas', 'USA')]
# print(one_item)  # (2, 'mike', 'Texas', 'USA') -
# print(many_items)  # [(2, 'mike', 'Texas', 'USA')]

# staff.db

# languages
#     name TEXT
#     frameworks TEXT

# coders
#     name TEXT
#     age TEXT
#     language TEXT

# sql = """
#     CREATE TABLE languages(
#         name TEXT,
#         frameworks TEXT);
# """

# sql = """
#     CREATE TABLE coders(
#         name TEXT,
#         age TEXT,
#         language TEXT,
#         );
# """
