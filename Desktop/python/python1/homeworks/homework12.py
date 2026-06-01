#import math
#1

# class Trans:
#     def __init__(self,b,s):
#         self.b=b
#         self.s=s
#     def move(self):
#         print('TRANSPORT IS MOVING! ')
# class Car(Trans):
#     def move(self):
#         print('CAR IS DRIVING!')
# class Plane(Trans):
#     def move(self):
#         print('PLANE IS FLYING')
# t1=Trans('Gender',200)
# c1=Car('BMW',200)
# p1=Plane('Poing',900)
# t1.move()
# c1.move()
# p1.move()

#2

# class Person:
#     def __init__(self,name):
#         self.name=name
#     def info(self):
#         print(self.name)

# class Student(Person):
#     def __init__(self, name,grade):
#         super().__init__(name)
#         self.grade=grade
#     def info(self):
#         super().info()
#         print(self.grade)
    
# name=str(input('Enter a surname ==> '))
# ps=str(input('Enter a name of child ==> '))
# padar=Person(name)
# pisar=Student(name,ps)
# print('Padar')
# padar.info()
# print('Pisar')
# pisar.info()

#3

# class System:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def work(self):
#         return 'Employee works'

# class Developer(System):
#     def work(self):
#         return 'Writes code'
    
# class Manager(System):
#     def work(self):
#         return 'Manages team'

# dev1=str(input())
# dev2=int(input())
# man1=str(input())
# man2=int(input())
# dev=Developer(dev1,dev2)
# man=Manager(man1,man2)
# print(dev.work())
# print(man.work())

#4

# class Character:
#     def __init__(self,name,health=100):
#         self.name=name
#         self.health=health
#     def attack(self):
#         return 'Basic attack'
    
# class Warrior(Character):
#     def __init__(self, name, health=100):
#         super().__init__(name, health)

#     def attack(self):
#         return 'Sword attack'

# class Mage(Character):
#     def __init__(self, name, health=100):
#         super().__init__(name, health)

#     def attack(self):
#         return 'Magic attack'
    
# w=str(input())
# m=str(input())
# war=Warrior(w)
# mag=Mage(m)
# print(war.attack())
# print(mag.attack())

#5

# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def sound(self):
#         print('Animal sound')
    
# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)
#     def sound(self):
#         super().sound()
#         print('Bark')

# s=str(input())
# anm=Animal('Generator animal')
# d=Dog(s)
# print('Animal Sound')
# anm.sound()
# print('\nDog Sound:')
# d.sound()