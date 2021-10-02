from faker import Faker
# Object:
# 1-sifat >> atribute
# 2-method >> hatti harakatlari

# agar qanday , qanaqa savollariga javob bersa bu - sifat
# nima qiladi savoliga javob bersa bu - hatti harakat

# class MyClass:
#     """this is first Class in Python"""
#     # object ni atribut va metodlari
#     pass

# class Car:
#     def __init__(self,name,model,price):
#         self.name = name
#         self.model = model
#         self.price = price
#
#
#     def signal(self):
#         print(self.name , "signal cholyapti...")

# car1 = Car()
#
# print(car1.name)
# print(car1.model)
# print(car1.price)
# print(car1.signal())
#
# car2 = Car(name="Nexia",model="Shevrole",price=2500)
# print(car2.name)
# print(car2.model)
# print(car2.price)
#
# car3 = Car(name="Damas",model="Shevrolet",price=15000)
# print(car3.name)
# print(car3.model)
# print(car3.price)

fake = Faker()

# import keyword
# print(keyword.kwlist)

# getattr()
# setattr()
# delattr()

# class MyClass:
#     def __init__(self):
#         self.x = 10
#
#     def get_x_value(self):
#         return self.x
#
# c = MyClass()
#
# print(getattr(c,"x"))
# print(getattr(c,"get_x_value"))
#
# setattr(c,"y",20)
# print(getattr(c,"y"))
#
# delattr(c,"y")
# print(getattr(c,"y")) # AtributeError

# class Robot:
#     population = 0
#     def __init__(self, name,model):
#         self.name = name
#         self.model = model
#         Robot.population += 1
#
#     def showPopulationCount(self):
#         print(self.population)
#
# r1 , r2 ,r3 = Robot("R2D2","android"), Robot("CTD2","android"),Robot("Gt300","android")
#
# r4 = Robot("Test robot","model TEST")
# r4.showPopulationCount()

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f"{self.name} ismlik Person obyekti namunasi")
#
# class Student(Person):
#     def __init__(self):
#         print("Talaba obyekti namunasi")
#         Person.__init__(self,"Abdullo",15)
# s = Student()
# print(s.name)
# print(s.info())




