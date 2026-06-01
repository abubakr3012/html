# class Book:
#     def __init__(self,title, author, pages:int, price:int):
#         self.title=title
#         self.author=author
#         self.pages=pages
#         self.price=price
#     def discount(self,persent):
#         sk=self.price*persent/100
#         self.price=self.price-sk
#     def show(self,persent):
#         sk=self.price*persent/100
#         self.price=self.price-sk
#         return f'''
# Title : {self.title}
# Author : {self.author}
# Pages : {self.pages}
# Price : {self.price}
# '''

# title=input('Enter title of book --> ')
# author=input('Enter author of book --> ')
# pages=int(input('Enter pages of book --> '))
# price=int(input('Enter price of book --> '))

# book1=Book(title,author,pages,price)
# print(book1.show(10))


# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.balance=balance
#     def deposit(self,dep):
#         self.balance=self.balance+dep
#     def withdraw(self,minus):
#         if minus>self.balance:
#             return 'Not money'
#         self.balance-=minus
#     def display(self):
#         return f'Owner --> {self.owner}\nBalance --> {self.balance}'
    
# owner=input('Enter owner of account --> ')
# balance=int(input('Enter balance --> '))
# user=BankAccount(owner,balance)
# user.deposit(100)
# user.withdraw(500)
# print(user.display())


# class Student:
#     def __init__(self,name):
#         self.name=name
#         self.grades=[]
#     def add_grade(self,grade):
#         self.grades.append(grade)
#     def average(self):
#         sm=sum(self.grades)
#         ln=len(self.grades)
#         return f'Average {sm/ln}'
#     def show(self):
#         return f'name : {self.name}\ngrades : {self.grades}'
# name=input('Enter name of student --> ')
# user=Student(name)
# user.add_grade(5)
# user.add_grade(4)
# print(user.average())
# print(user.show())


# class Movie:
#     def __init__(self,title:str, director:str, year:int, rating:float):
#         self.title=title
#         self.director=director
#         self.year=year
#         self.rating=rating

#     def is_classic(self):
#         if (2026-self.year)>25:
#             return True
#         else:
#             return False
    
#     def update(self,new:float):
#         self.new=new
#         self.rating=self.new
#     def show(self):
#         return f'''
# name : {self.title}
# director : {self.director}
# year : {self.year}
# rating : {self.rating}
# '''

# title=input('Enter title movie --> ')
# director=input('Enter director movie --> ')
# year=int(input('Enter year movie --> '))
# rating=float(input('Enter rating movie --> '))
# film1=Movie(title,director,year,rating)
# film1.update(10.0)
# print(film1.is_classic())
# print(film1.show())


# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         s=3.14*(self.radius**2)
#         return s
#     def perimeter(self):
#         return 2*3.14*self.radius
#     def scale(self,factor):
#         self.radius=self.radius*factor
#         return self.radius

# circle1=Circle(5)
# print(circle1.area())
# print(circle1.perimeter())
# print(circle1.scale(500))