# class - Chizma , real hayotdagi obyekt tuzilishi

# class cat:
#     pass 
# print(cat) # <class '__main__.cat'>

# def cat():
#     pass

# print(cat) # <function cat at 0x00000277A2A38A60>
# class Cat:
#     """Cat object"""
#     # Attributes 
#     name = "Kisa"
#     color = "gray"
#     age = 2.5
#     # Methods
#     def mew_mew(self):
#         print("Mew-mew !")
    
#     def jump(self):
#         print("Jumping !")

# class Player:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age 
    
#     def player_info(self):
#         print(f"Player name = {self.name}")
#         print(f"Player age = {self.age}")

# # class namunasini xosil qilish 
# p1 = Player("John Doe", 30)
# print(p1) # <__main__.Player object at 0x0000022D70297880>
# p2 = Player("Mike Tyson", 20)
# p1.name = "Sara David"
# p1.player_info()
# p2.player_info()

# OOP - Object Oriented Programming 


# class MyClass:
#     def __init__(self, name):
#         self.name = name

#     def say_hello(self):
#         print(f"Hello, {self.name}!")

#     def __str__(self):
#         return self.name

# obj_name = MyClass("Joji")
# print(obj_name) # Joji


# my_object = MyClass("World")
# my_object.say_hello() # Output: Hello, World!

# print(dir(my_object))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'say_hello']

# class Dog:
#     name = "Buz"
#     age = 3

# # print(getattr(Dog ,"name")) # Buz
# # print(getattr(Dog ,"home")) # AttributeError
# setattr(Dog, "home", "Ohio, Texas")
# print(Dog.home) # Ohio, Texas
# # delattr(Dog , "home")
# # print(Dog.home) # AttributeError

# print(hasattr(Dog, "salaray")) # false
# print(hasattr(Dog, "home")) # true


# Inheritions 

# class Person:
    
#     def __init__(self,name,gender):
#         self.name = name 
#         self.gender = gender
    
#     def say_hi(self):
#         print("Hi my name is, ", self.name)
    
            
# class Student(Person):
    
#     def __init__(self, name , gender ,point):
#         self.point = point
#         Person.__init__(self,name,gender)

    
#     def show_point(self):
#         print(f"Student {self.name} point = {self.point}")

# st1 = Student("John", "male", 30) 
# st1.say_hi()# Hi my name is,  John
# st1.show_point() # Student John point = 30
# st1.student_method()

# class Car:
#     def __init__(self, model) -> None:
#         self.model = model
    
#     def drive(self):
#         print(self.model, " car driving...")
    
#     @staticmethod # self siz metod hosil qilish
#     def plus(x,y):
#         return x + y

# c = Car("Model X")
# c.drive() # Model X  car driving...
# print(c.plus(2,2)) # TypeError: plus() takes 2 positional arguments but 3 were given
# print(c.plus(2,2)) # 4

