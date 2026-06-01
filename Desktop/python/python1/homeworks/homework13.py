from colorama import Back,Style,Fore
#1

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     @property
#     def name(self):
#         return self._name
#     @name.setter
#     def name(self,name):
#         if name=='' or name==' ':
#             print(f'{Style.BRIGHT}{Fore.RED}Error{Style.RESET_ALL}')
#         else:
#             self._name=name
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self,value):
#         if value<=0 or value>120:
#             print(f'{Style.BRIGHT}{Fore.RED}Error{Style.RESET_ALL}')
#         else:
#             self.__age=value
# name=input('Enter your name ==> ')
# age=int(input('Enter your age ==> '))
# s=Student(name,age)
# print(f"Your name ==> {s.name}\nYour age ==> {s.age}")

#2

# class Account:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.balance=balance
#     @property
#     def owner(self):
#         return self.__owner
#     @owner.setter
#     def owner(self,value):
#         if value.strip()=="":
#             print(f'{Style.BRIGHT}{Fore.RED}Error{Style.RESET_ALL}')
#         else:
#             self.__owner=value
#     @property
#     def balance(self):
#         return self.__balance
#     @balance.setter
#     def balance(self,value):
#         if value<0:
#             print(f'{Style.BRIGHT}{Fore.RED}Error{Style.RESET_ALL}')
#         else:
#             self.__balance=value

# owner=input('Enter name of owner account ==> ')
# balance=int(input('Enter balance of your account ==> '))
# acc=Account(owner,balance)

# print('Owner:',acc.owner)
# print('Balance:',acc.balance)

# dep=int(input('How many deposit you want? ==> '))
# acc.balance+=dep
# print('Balance with deposit:',acc.balance)

#3

# class Car:
#     def __init__(self,brand,speed):
#         self.brand=brand
#         self.speed=speed
#     @property
#     def brand(self):
#         return self.__brand
    
#     @brand.setter
#     def brand(self,value):
#         if value.strip()=='':
#             print(f'{Style.BRIGHT}{Fore.RED}Error{Style.RESET_ALL}')
#         else:
#             self.__brand=value
    
#     @property
#     def speed(self):
#         return self.__speed
    
#     @speed.setter
#     def speed(self, value):
#         if value<=0 or value>300:
#             print(f'{Style.BRIGHT}{Fore.RED}Error{Style.RESET_ALL}')
#         else:
#             self.__speed=value

# brand=input('Enter a brand of car ==> ')
# speed=int(input('Enter a speed which you want ==> '))
# car=Car(brand,speed)

# print('Brand:',car.brand)
# print('Speed:',car.speed)

# sp=int(input('Enter your speed ==> '))
# car.speed=sp
# print(car.speed)