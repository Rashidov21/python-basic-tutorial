# from faker import Faker
# Object:
# 1-sifat >> atribute
# 2-method >> hatti harakatlari

# agar qanday , qanaqa savollariga javob bersa bu - sifat
# nima qiladi savoliga javob bersa bu - hatti harakat

# class MainClass:
#     """this is first Class in Python"""
#
#     x = "First Class"
#
#     # object ni atribut va metodlari
#     def mainMethod(self):
#         print("Hello world, I am", self.x)
# m = MainClass()
# m.mainMethod()

# print(MainClass.__doc__)
#
# class Car:
#     _myCar = "No name"
#     __count = 0
#     def __init__(self,name,model,price):
#         self.name = name
#         self.model = model
#         self.price = price
#
#     def signal(self):
#         print(self.name , "signal cholyapti...")
# #
# car = Car("ds", "dsds", 45)
# car.__count = 11
# print(car.__count)
# car1 = Car("Lexus", "Shevrolet", 1500)
# car1.signal()

# car2 = Car("Moseratti", "Moseratti R3", 56000)
#
# print(dir(car1))
# print(car1.model)
# print(car1.price)
# print(car2.name)
# print(car2.model)
# print(car2.price)
# print(car1.signal())
# print(car2.signal())
# car2 = Car(name="Nexia",model="Shevrole",price=2500)
# print(car2.name)
# print(car2.model)
# print(car2.price)
#
# car3 = Car(name="Damas",model="Shevrolet",price=15000)
# print(car3.name)
# print(car3.model)
# print(car3.price)

# fake = Faker()

# import keyword
# print(keyword.kwlist)

# getattr()
# setattr()
# delattr()
# class Horse():
#     isHorse = True
#
# class Donkey():
#     isDonkey = True
#
# class Mule(Horse, Donkey):
#     pass
# mule = Mule()
# mule.isHorse # True
# mule.isDonkey # True
# class MyClass:
#
#     def __init__(self):
#         self.x = 10
#
#     @classmethod
#     def main_class_method(cls,x):
#         print(cls, x)
#
#     @staticmethod
#     def main_method(a):
#         print(a * 2)
#
#     def get_x_value(self):
#         return self.x

# MyClass.main_method(10) # 20
# MyClass.main_class_method(5)
# c = MyClass()
# c.main_class_method(10)
# print(c.get_x_value())
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
# #
# r1 , r2 ,r3 = Robot("R2D2","android"), Robot("CTD2","android"),Robot("Gt300","android")
# #
# r4 = Robot("Test robot","model TEST")
# r4.showPopulationCount()

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"{self.name} ismlik Person obyekti namunasi")
#
# class Student(Person):
#     def __init__(self,name,age,rating,collage_name):
#         self.name = name
#         self.rating = rating
#         self.collage_name = collage_name
#         print("Talaba obyekti namunasi")
#         Person.__init__(self,name,age)
#
# s = Student("Abdullo", 15, "superstar", "ATS")
# s2 = Student("Mike", 23, "none", "BTS")
#
# print(s2.info())
# print(s2.rating)
# print(s2.collage_name)
# print(s.name)
# print(s.info())

# class MyClass:
#     x = 10
#
#     def info(self):
#         print(self.x)
#
# x = MyClass()
# setattr(x, "y",20) # MyClass uchun yangi atrr qoshyapti
# print(x.y) # 20
#
# delattr(x, "y") # MyClass ni y attr ni ochirib yuborildi
# print(x.y) # AttributeError: 'MyClass' object has no attribute 'y'
# class MyClass:
#     x = 10
#
#     def __str__(self):
#         return str(self.x)
#
#     def info(self):
#         print(self.x)
#
# print(MyClass())

# class Phone:
#
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model
#
#     @staticmethod
#     def myStmetod():
#         print("this is static method in Phone class")
#
#     def check_sim(self, mobile_operator):
#         if self.model == 'iphone' and mobile_operator == 'UMS':
#             print('Your mobile operator is UMS')
#
# Phone.myStmetod()

# p = Phone("gray","iphone")
# # print(p.color , p.model)
# p.check_sim(mobile_operator="UMS")

# class MyClass:
#     def __init__(self,x):
#         self.__privateVar = x
#
#     def setVar(self,x):
#         self.__privateVar = x
#     def getVar(self):
#         return self.__privateVar
# c = MyClass(10)
# print(c.getVar())
# c.setVar(20)
# print(c.getVar())


class SchoolMember:
# '''Представляет любого человека в школе.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'.format(self.name))

    def tell(self):
        print(f"Ismi = {self.name} . Yoshi = {self.age}")
# m = SchoolMember("John", 35)
# member.tell()

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        # SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Создан Teacher: {0})'.format(self.name))

    # def tell(self):
    #     SchoolMember.tell(self)
    #     print('Зарплата: "{0:d}"'.format(self.salary))
t = Teacher('Mrs. Shrividya', 40, 30000)
t.tell()

