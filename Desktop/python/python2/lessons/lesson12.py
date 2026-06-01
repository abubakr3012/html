# class Car:
#     def __init__(self,model,color,constructor,price:int):
#         self.model=model
#         self.color=color
#         self.constructor=constructor
#         self.price=price
    
#     def show(self):
#         return f'''
# Name --> {self.model}
# Color --> {self.color}
# Constructor --> {self.constructor}
# Price --> {self.price}'''

# model=input('Enter model of car --> ')
# color=input('Enter color of car --> ')
# constructor=input('Enter names constructor of car --> ')
# price=int(input('Enter price of car --> '))
# car=Car(model,color,constructor,price)
# print(car.show())
# print()


# class Book:
#     def __init__(self,title, author, pages:int, price:int):
#         self.title=title
#         self.author=author
#         self.pages=pages
#         self.price=price
#     def is_expensive(self):
#         if self.price>500:
#             return 'Expensive'
#         else:
#             return 'Cheap'
#     def show(self):
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

# print(book1.show())
# print(book1.is_expensive())

# class Student:
#     def __init__(self,name:str,age:int,faculty:str,gpa:int):
#         self.name=name
#         self.age=age
#         self.faculty=faculty
#         self.gpa=gpa
    

        
        


class Products:
    def __init__(self,name:str,price:int,cnt:int):
        self.name=name
        self.price=price
        self.quantity=cnt
    def discount(self,n):
        p=self.price
        p=(p*n)/100
        self.price=self.price-p
    def show(self):
        if n>self.quantity:
            return f'You have not {n} {name}'
        else:
            total=self.price*(self.quantity-n)
        return f'''
name of product {self.name}
price of product {self.price}
quantity of producit {self.quantity}
you are saled {n}
you have {self.quantity-n} {name}
you must pay {total} somoni
'''

name=input('Enter name --> ')
price=int(input('Enter price --> '))
cnt=int(input('Enter quantity --> '))
n=int(input('How many product you want sale --> '))
product=Products(name,price,cnt)
print(product.show())
print(product.discount(10))