from colorama import Style,Fore
# меросгири

# class Fahter:
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         return self.name
# class Child(Fahter):
#     pass
# a=Child(name='Abubakr')
# print(a.show())

# капсула

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

# #Полиморфизм

# class Transport:
#     def __init__(self,name):
#         self.name=name

#     def place_for_bying(self):
#         print('I can move')
    
#     def fuel(self):
#         print('My fuel is Oil')
    
#     def fly(self):
#         print('I can fly')
    
#     def swim(self):
#         print('I can swim')

#     def drive(self):
#         print('I can drive')
    
# class Plane(Transport):
#     def place_for_bying(self):
#         super().place_for_bying()
    
#     def fuel(self):
#         super().fuel()
    
#     def fly(self):
#         super().fly()
    
#     def swim(self):
#         pass

#     def drive(self):
#         pass

# class Car(Transport):
#     def place_for_bying(self):
#         super().place_for_bying()
    
#     def fuel(self):
#         super().fuel()

#     def fly(self):
#         pass

#     def swim(self):
#         pass

#     def drive(self):
#         super().drive()

# class Boat(Transport):
#     def place_for_bying(self):
#         super().place_for_bying()
    
#     def fuel(self):
#         super().fuel()

#     def fly(self):
#         pass

#     def swim(self):
#         super().swim()

#     def drive(self):
#         pass
    
# tran=[
#     Transport('Type of transport'),
#     Plane('Somon Air'),
#     Car('BMW'),
#     Boat('Oil Boat')
# ]
# a=input('Enter a name of transport ==> ')
# if a not in tran:
#     print('Error')
# else:
#     print()
#     print('*'*20)
#     print(a.name)
#     a.place_for_bying()
#     a.fuel()
#     a.fly()
#     a.swim()
#     a.drive()
#     print('*'*20)


# class Student:
#     def __init__(self,name,age,ave):
#         self.name=name
#         self.age=age
#         self.ave=ave

#     def name_stu(self):
#         return self.name
    
#     def age_stu(self):
#         return self.__age
    
#     def ave_stu(self):
#         return self.ave

# name=input('Enter a name of Student ==> ')
# age=int(input('Enter your age ==> '))
# ave=list(map(int,input('Enter a numbers of Student ==> ').split()))
# student=Student(name,age,ave)
# print()
# print(f'{'*'*25}\nYour name ==> {student.name}\nYour age ==> {student.age}\nYour average ==> {sum(student.ave)/len(student.ave)}\n{'*'*25}')
# print()