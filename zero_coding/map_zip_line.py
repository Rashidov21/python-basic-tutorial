# map() 
# def main(item):
#     return item + 1

# arr = [1,2,3]
# for i in arr:
#     print(main(i))
    
# print(list(map(main,[1,2,3]))) # [2, 3, 4]
# print(list(map(main,(2,3,4)))) # [3, 4, 5]

# task 1 
# letters_amazon = '''
# We spent several years building our own database engine,
# Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible
# service with the same or better durability and availability as
# the commercial engines, but at one-tenth of the cost. We were
# not surprised when this worked.
# '''

# task 2 
price = [[9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
 [9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
 [8.4, 7.9, 7.9, 8.1, 8.0, 8.0],
 [7.1, 5.9, 4.8, 4.8, 4.7, 3.9]]
# berilgan massivdan har ikkinchi elementlardan iborat alohida massiv hosil qiling

# task 3 
visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted',
 'Safari', 'corrupted', 'Safari', 'corrupted',
 'Chrome', 'corrupted', 'Firefox', 'corrupted']
# berilgan massivdagi har ikkinchi element qiymatini undan oldingi elementniki bilan almashtiring alohida massiv ochilmaydi




# print(visitors)
# arr = list(range(1,15))
# for i in range(0,len(arr),2):
#     arr[i-1] = arr[i]
    
# print(arr)

# task 3 
companies = {
 'CoolCompany' : {'Alice' : 33, 'Bob' : 28, 'Frank' : 29},
 'CheapCompany' : {'Ann' : 4, 'Lee' : 9, 'Chrisi' : 7},
 'SosoCompany' : {'Esther' : 38, 'Cole' : 8, 'Paris' : 18}
 }

# ushbu ma'lumotlardan foydalanib qaysi kompaniyalarda ishchilar uchun soatiga $9 dan kam mablag to'lanishini korsatadigan dastur tuzing

illegal = [x for x in companies if any(y < 9 for y in companies[x].values())]