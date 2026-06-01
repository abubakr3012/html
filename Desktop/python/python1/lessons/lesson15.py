# from abc import ABC,abstractmethod
# from colorama import Style,Fore
# class Car(ABC):
#     def __init__(self,mark,model,color):
#         self.mark=mark
#         self.model=model
#         self.color=color
    
#     def start(self):
#         print('The car is starting .... ')
    
#     def stop(self):
#         print('the car is stoping .... ')
    
#     @abstractmethod
#     def petrol(self):
#         pass

#     @abstractmethod
#     def dizel(self):
#         pass
    
# class Mers(Car):
#     def __init__(self, mark, model, color):
#         super().__init__(mark, model, color)

#     def petrol(self):
#         print('True')
    
#     def dizel(self):
#         print('False')

#     def show(self):
#         print(self.mark)
#         print(self.model)
#         print(self.color)
# mark=input('Mark of car --> ')
# model=input('Model of car --> ')
# color=input('Color of car --> ')
# car=Mers(mark,model,color)

# car.start()
# car.petrol()
# car.dizel()
# # car.mark()
# # car.model()
# # car.color()
# car.stop()

# class Animal(ABC):
#     def __init__(self,name,type,food):
#         self.name=name
#         self.type=type
#         self.food=food
    

# USERS_WALLET=[]

# class Utils:
#     def check_full(self,fio,num):
#         cnt1,cnt2=0,0
#         for i in range(len(USERS_WALLET)):
#             if USERS_WALLET[i].get('Full name')==fio:
#                 cnt1+=1
        
#         for i in range(len(USERS_WALLET)):
#             if USERS_WALLET[i].get('Wallet number')==num:
#                 cnt2+=1
    
#     def check_passport_info(self,param):
#         if param == True:
#             return 'Confirm request'
#         return 'Reject request'

# class CNUBA(Utils):
#     def __init__(self,passport_info, full_name,bank_name,wallet_number):
#         self.passport_info=passport_info
#         self.full_name=full_name
#         self.bank_name=bank_name
#         self.wallet_number=wallet_number


#__init__
#Конструктор ҳангоми сохтани объект автоматикӣ иҷро мешавад ва барои инициализация 
#(танзими атрибутҳои аввалия) истифода мешавад.

# Атрибут
# Атрибут — тағйирёбанда (variable), ки дар дохили class ё object  мешавад.

# Бо ёрии self мо метавонем ба атрибутҳо ва методҳои ҳамон объект дастрасӣ пайдо кунем.

# Меросгирӣ — вақте ки як класс хусусиятҳо ва методҳои класси дигарро мегирад.
   
# super() - барои даъват кардани методи падар аз дохили фарзанд истифода мешавад.

# фаркияти метод аз функсия - Метод ба объект вобаста аст, функсия не.

# Static vs Class method
# staticmethod → ба class ё object вобаста нест
# classmethod → бо cls кор мекунад

# Magic method - __str__, __len__, __add__

# Сохтани объект
# obj = ClassName()

# Override
# Аз нав навиштани методи падар дар фарзанд.

# Multiple inheritance
# Як класс аз якчанд класс мерос мегирад

# Полиморфизм
# Як ном — рафтори гуногун.

# Duck typing
# Агар объект метод дошта бошад — тип муҳим нест.

# Overloading → як ном, параметрҳои гуногун
# Overriding → аз нав навиштан

# Капсула
# Пинҳон кардани маълумот.

# Getter/Setter
# Барои идора кардани дастрасӣ ба private атрибут.

# capsula public protected (_name) private (__name)

# Абстраксия
# Пинҳон кардани деталҳо ва нишон додани функсионал.

# Abstract class
# Класс бо методҳои ҳатмӣ.

