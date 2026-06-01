from abc import ABC,abstractmethod

class Cat:
    def __init__(self):
        self.name=None
        self.age=None
        self.ishappy=None
    def set_data(self,name,age,ishappy):
        self.name=name
        self.age=age
        self.ishappy=ishappy
    
    def show(self):
        print(f'{self.name} {self.age} {self.ishappy}\n')

name1=input('name of first cat --> ')
age1=int(input('age of first cat --> '))
ishappy1=True
print()
name2=input('name of second cat --> ')
age2=int(input('age of second cat --> '))
ishappy2=False

cat1=Cat()
cat1.set_data(name1,age1,ishappy1)

cat2=Cat()
cat2.set_data(name2,age2,ishappy2)

cat1.show()
cat2.show()
