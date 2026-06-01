class Animal:
    def sound(self):
        print('Animal sound!')
    
class Dog(Animal):
    def sound(self):
        print('Woof woof')
    
class Cat(Dog):
    def sound(self):
        print('Meow meow')

lst=[Dog(),Cat()]
for i in lst:
    i.sound()

