from abc import ABC, abstractmethod
# class BankAccount:
#     def __init__(self,owner,balance) -> None:
#         self.name=owner
#         self.__balance=balance

#     def deposit(self,amount):
#         self.__balance+=amount
    
#     def withdraw(self,amount):
#         if amount>self.__balance:
#             print('Not money')
#             return
#         self.__balance-=amount
    
#     def get_balance(self):
#         print(f'''
# Owner : {self.name}
# Balance : {self.__balance}
# ''')

# user1=BankAccount('Abubakr',1000)
# user1.deposit(500)
# user1.withdraw(1200)
# user1.get_balance()

# class Student:
#     def __init__(self,name,grade) -> None:
#         self.name=name
#         self.__grade=grade
    
#     def set_grade(self,value):
#         if 0<value<100:
#             self.__grade=value
#         else:
#             print('Invalid grade')
    
#     def get_grade(self):
#         print(f'Name --> {self.name}\nGrade --> {self.__grade}')

# std1=Student('Usmon',20)
# std1.set_grade(10)
# std1.get_grade()


# class Car:
#     def __init__(self,model,speed) -> None:
#         self.model=model
#         self.__speed=speed
    
#     def accelerate(self,value):
#         self.__speed+=value
    
#     def brake(self,value):
#         if value>self.__speed:
#             print('Wrong Speed')
#             return
#         self.__speed-=value
    
#     def get_speed(self):
#         print(f'Model --> {self.model}\nSpeed --> {self.__speed}')
    
# car1=Car('BMW',220)
# car1.accelerate(80)
# car1.brake(310)
# car1.get_speed()

# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class rectangle(shape):
#     def __init__(self,a,b) -> None:
#         self.a=a
#         self.b=b
#     def area(self):
#         print(self.a*self.b)

# class circle(shape):
#     def __init__(self,radius) -> None:
#         self.radius=radius
#     def area(self):
#         print(3.14*self.radius**2)

# sh1=rectangle(4,5)
# sh2=circle(10)

# sh1.area()
# sh2.area()

# class Payment(ABC):
#     @abstractmethod
#     def pay(self,amount):
#         pass

# class CashPayment(Payment):
#     def pay(self,amount):
#         print(f'Payed {amount} by cash')

# class CardPayment(Payment):
#     def pay(self,amount):
#         print(f'Payed {amount} by card')

# p1=CashPayment()
# p2=CardPayment()

# p1.pay(200)
# p2.pay(120)
