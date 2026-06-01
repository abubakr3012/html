# from abc import ABC,abstractmethod

# class Person(ABC):
#     @abstractmethod
#     def speak(self):
#         print('I can speak')
#     @abstractmethod
#     def walk(self):
#         print('I can walk')

# class Student(Person):
#     def __init__(self,name) -> None:
#         self.name=name
#     def walk(self):
#         print(f'{self.name} can walk')
#     def speak(self):
#         print(f'{self.name} can speak')
    
# st1=Student('Ali')
# st1.speak()
# st1.walk()

# class Transport(ABC):
#     @abstractmethod
#     def move(self):
#         print('I can move')

# class Car(Transport):
#     def move(self):
#         print('I cam move in road')
    
# class Air(Transport):
#     def move(self):
#         print('I can fly in sky')

# tr1=Car()
# tr2=Air()

# tr1.move()
# tr2.move()

# class Payment(ABC):
#     @abstractmethod
#     def pay(self):
#         print('You are payed')

# class Card(Payment):
#     def __init__(self,amount) -> None:
#         super().__init__()
#         self.amount=amount
#     def pay(self):
#         print(f'You are payed {self.amount} with card')
    
# class Cash(Payment):
#     def __init__(self,amount) -> None:
#         super().__init__()
#         self.amount=amount
    
#     def pay(self):
#         print(f'You are payed {self.amount} with cash')

# lst=[Card(100),Cash(220)]
# for i in lst:
#     i.pay()

# class Auth(ABC):
#     @abstractmethod
#     def login(self):
#         print(f'You are joined')
    
#     @abstractmethod
#     def logout(self):
#         print(f'You are lefted')

# class Google(Auth):
#     def login(self):
#         print('Your are joined with google account')
    
#     def logout(self):
#         return super().logout()

# class Email(Auth):
#     def login(self):
#         print('Your are joined with email')
    
#     def logout(self):
#         return super().logout()

# lst=[Google(),Email()]
# for i in lst:
#     i.login()
#     i.logout()

# class Notification(ABC):
#     @abstractmethod
#     def send(self):
#        pass

# class EmailNotification(Notification):
#     def __init__(self,message) -> None:
#        self.message=message
    
#     def send(self):
#         print(f'You are sended message {self.message} with email')

# class SMSNotification(Notification):
#     def __init__(self,message) -> None:
#        self.message=message
    
#     def send(self):
#         print(f'You are sended message {self.message} with sms')

# lst=[EmailNotification(' |Hello I am in Softclub. I will left it at 12:30| '),SMSNotification(' |Hello. Thank you.| ')]
# for i in lst:
#     i.send()

# class FileHandler(ABC):
#     @abstractmethod
#     def read(self):
#         pass   
#     @abstractmethod
#     def write(self):
#         pass
# class TextFile(FileHandler):
#     def __init__(self,data) -> None:
#         self.data=data
#     def read(self):
#         print(f'You are read my text')
#     def write(self):
#         print(f'You are wrote text {self.data} to me')
# class JsonFile(FileHandler):
#     def __init__(self,data) -> None:
#         self.data=data
#     def read(self):
#         print(f'You are read my json text')
#     def write(self):
#         print(f'You are wrote json text {self.data} to me')
# lst=[TextFile('salom aleykum'),JsonFile('Voaleykum salom')]
# for i in lst: 
#     i.read()
#     i.write()

# class APIService(ABC):
#     @abstractmethod
#     def get(self):
#         pass
#     @abstractmethod
#     def post(self):
#         pass

# class UserApi(APIService):
#     def get(self):
#         print('You are given me API from user')
#     def post(self):
#         print('Your API that you give me is ...')

# class PrdApi(APIService):
#     def get(self):
#         print('You are given me API from product')
#     def post(self):
#         print('Your API product that you give me is ...')

# user=UserApi()
# product=PrdApi()

# user.get()
# user.post()

# product.get()
# product.post()


# class Person:
#     def __init__(self,name,age) -> None:
#         self.name=name
#         self.__age=age
#     @property
#     def age(self):
#         print(self.__age)

#     @age.setter
#     def age(self,m):
#         if m>0:
#             self.__age=m
#             print(self.name,self.__age)
#         else:
#             print('Error')

# ob=Person('Umar',10)
# ob.age=0

# class Cours:
#     def __init__(self) -> None:
#         self.__lst=[]
    
#     @property
#     def students(self):
#         for i in self.__lst:
#             print(i,end=" ")

#     @students.setter
#     def add_std(self,name):
        
#         if name not in self.__lst:
#             self.__lst.append(name)
#             print(self.__lst)
#         else:
#             print('error')
        
# st1=Cours()
# st1.add_std='Umar'
# st1.add_std='Umar'

# class Cours2:
#     def __init__(self) -> None:
#         self.__lst=[]
    
#     def get(self):
#         for i in self.__lst:
#             print(i,end=" ")
        
#     def set(self,std):
#         if std not in self.__lst:
#             self.__lst.append(std)
#         else:
#             print('Error')
# st1=Cours2()
# st1.set('Abubakr')
# st1.set('Ali')
# st1.set('Halim')
# st1.get()

