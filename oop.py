# OOP
# object - Attribute + Method
# Attribute - sifat , qanday , qanaqa , qachon , qancha ..
# Method - harakat , usul , nima qiladi
# class - bu chizma

# class MyClass:
#     """class docstring"""
#     # Attributes
#     name = "myclass"

#     # methods
#     def get_info(self):
#         print(self.name)


# # x = 10
# # print(type(x))

# # print(MyClass)  # <class '__main__.MyClass'>

# example = MyClass()  # yangi namuna xosil qilish
# print(example.get_info())  # myclass
# print(MyClass.__name__)  # MyClass

# Car obyektini hosil qilish
# class Car:

#     # sifatlarini qoshish
#     name = "c200"
#     make = "mercedez"
#     model = 2008

#     # harakatlarini qoshish
#     def start(self):
#         print(f"{self.name } :Moshinda yurdi")

#     def stop(self):
#         print("Moshinda o'chdi")


# car2 = Car()
# car2.name = "damas"
# car2.make = "shevrolet"
# car2.model = 2010

# print(car2.start())


# создаем класс Car
# class Car:
#     message1 = "Двигатель заведен"

#     def start(self):
#         if self.message1:
#             print("OK")
#         message2 = "Автомобиль заведен"
#         return message2


# car_a = Car()
# car_a.message1 = "blabla"
# print(car_a.message1)
# print(car_a.start())


# class Car:
#     def __init__(self):
#         print("Двигатель заведен")
#         self.name = "corolla"
#         self.__make = "toyota"
#         self._model = 1999


# car_a = Car()
# print(car_a.name)  # bu public qiymat
# # print(car_a.make)  # protected qiymat
# # AttributeError: 'Car' object has no attribute 'make'
# print(car_a._model)  # protected qiymat

# oddiy ozgaruvchi bu public qiymat
# _ bor ozgaruvchi bu private qiymat
# __ bor ozgaruvchi bu protected qiymat


# Meros olish
# class Person:
#     age = 20

#     def get_age(self):
#         print(self.age)


# class Player(Person):
#     def __init__(self, age, name):
#         self.age = Person.age
#         self.name = name


# p = Player(23, "John")
# print(p.name)
# print(p.age)
# print(p.get_age())

# class Calculator:
#     version = "1.0"

#     def plus(self, x, y):
#         return x + y

#     def minus(self, x, y):
#         return x - y

#     def multiple(self, x, y):
#         return x * y

#     def division(self, x, y):
#         return x / y

#     @staticmethod
#     def show_info():
#         print(Calculator.version)


# calc = Calculator()

# # print(calc.plus(10, 5))
# print(calc.show_info())
# class Robot:
#     population = 0

#     def __init__(self, name, model):
#         self.name = name
#         self.model = model
#         Robot.population += 1


# r1 = Robot("A2", "Tesla")
# r2 = Robot("A3", "Apple")
# r3 = Robot("A4", "Samsung")

# print(r3.population)

class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        print('(Инициализация {0})'.format(self.name))

        Robot.population += 1


def __del__(self):
    '''Я умираю.'''
    print('{0} уничтожается!'.format(self.name))
    Robot.population -= 1

    if Robot.population == 0:
        print('{0} был последним.'.format(self.name))
    else:
        print('Осталось {0} работающих роботов.'.format(Robot.population))


r1 = Robot("A2", "Tesla")
r2 = Robot("A3", "Apple")
r3 = Robot("A4", "Samsung")
# r3.__del__(self)
print(r3.population)
# Polimorfizm
# Inkapsulyatsiya
