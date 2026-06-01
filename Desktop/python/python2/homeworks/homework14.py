# class Bank:
#     def __init__(self,owner,balance) -> None:
#         self.owner=owner
#         self.__balance=balance
#     @property
#     def get_balance(self):
#         print(f'Owner {self.owner}\nBalance {self.__balance}\n')
#     @get_balance.setter
#     def withdraw(self,amount):
#         if amount>self.__balance:
#             print('The deposit bigger than balance')
#             return
#         else:
#             self.__balance-=amount
#     def deposit(self,amount):
#         self.__balance+=amount
# o1=Bank('Abubakr',200)
# o1.withdraw=100
# o1.get_balance
# o1.deposit(200)
# o1.get_balance

# print()

# class User:
#     def __init__(self) -> None:
#         self.__password=None
    
#     def set_password(self,password):
#         if len(password)>=6:
#             self.__password=password
    
#     def check_password(self,password):
#         print(self.__password==password)

# user=User()
# user.set_password('1234')
# user.set_password('12345678')
# user.check_password('12345678')
# user.check_password('123321')

# print()
# class Temperature:
#     def __init__(self) -> None:
#         self.__cel=None
#     @property
#     def celcius(self):
#         return f"Celius {self.__cel}"
#     @celcius.setter
#     def celcius(self,c):
#         if c<-273:
#             print('Not -273')
#             return
#         self.__cel=c  
#     def to(self):
#         return self.__cel*9/5+32
# w1=Temperature()
# w1.celcius=-3200
# w1.celcius=25
# print(w1.celcius)
# print(w1.to())

# print()

# class Student:
#     def __init__(self) -> None:
#         self.__grades=[]
    
#     @property
#     def get_grades(self):
#         return self.__grades
    
#     @get_grades.setter
#     def add_grade(self,grade):
#         if 0<grade<=100:
#             self.__grades.append(grade)
#         else:
#             print('None grade')
    
#     def get_average(self):
#         return sum(self.__grades)/len(self.__grades)

# st1=Student()
# st1.add_grade=5
# st1.add_grade=10

# print(st1.get_grades)
# print(st1.get_average())
# print()


# class Product:
#     def __init__(self,name) -> None:
#         self.__name=name
#         self.__price=None
    
#     @property
#     def price(self):
#         return self.__price
    
#     @price.setter
#     def price(self,price):
#         if price<0:
#             print('Error price!')
#         self.__price=price
    
#     def get_count(self,percent):
#         return self.__price*(1-percent/100)
# prd=Product('Milk')
# prd.price=100
# print(prd.price)
# print(prd.get_count(2))