1

class Animal:
    def speak(self):
        print('Animal Sound')

class Dog(Animal):
    def speak(self):
        print('Woof - Woof')

class Cat(Animal):
    def speak(self):
        print('Meow - Meow')

animals=[Dog(),Cat()]
for i in animals:
    i.speak()

2

class Shape:
    def area(self):
        print('Shapes')

class Rectangle:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def show(self):
        print(self.a*self.b)

class Circle:
    def __init__(self,r):
        self.r=r
    def show(self):
        print(3.14*self.r*self.r)
    
a=int(input('Enter a lenght of Rectangle ==> '))
b=int(input('Enter a width of Rectangle ==> '))
r=int(input('Enter a radius of Circle ==> '))
shps=[Rectangle(a,b), Circle(r)]
for i in shps:
    i.show()

3

class Pay:
    def __init__(self,a):
        self.a=a
    def pay(self):
        pass

class Cash(Pay):
    def pay(self):
        print(f'Paid {self.a} by cash')
    
class Card(Pay):
    def pay(self):
        print(f'Paid {self.a} by card')
    
class Online(Pay):
    def pay(self):
        print(f'Paid {self.a} online')

a=int(input('Enter a money ==> '))
p=[Cash(a), Card(a), Online(a)]

for i in p:
    i.pay()
