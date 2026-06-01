# class shape:
#     def area(self):
#         pass

# class Circle(shape):
#     def __init__(self,radius) -> None:
#         super().__init__()
#         self.raduis=radius
#     def area(self):
#         return 3.14 * self.raduis **2
# class Rectangle(shape):
#     def __init__(self,a,b) -> None:
#         super().__init__()
#         self.a=a
#         self.b=b
#     def area(self):
#         return self.a*self.b
    
# sh1=Circle(10)
# sh2=Rectangle(5,12)
# print(f'Area --> {sh1.area()}')
# print(f'Area --> {sh2.area()}')

# class Employee:
#     def __init__(self,name,salary) -> None:
#         self.name=name
#         self.salary=salary
    
#     def get_salary(self):
#         print(f'salary of {self.name} is {self.salary}')
    
# class Manager(Employee):
#     def __init__(self, name, salary,bonus) -> None:
#         super().__init__(name, salary)
#         self.bonus=bonus
#         self.salary+=self.bonus

# class Developer(Employee):
#     def __init__(self, name, salary,hours) -> None:
#         super().__init__(name, salary)
#         self.hours=hours
#         self.salary+=(self.hours*24)

# leader=Employee('Nurullo',10000)
# mng=Manager('Khayriddin',5000,500)
# dv=Developer('Muhammad',8000,50)
# leader.get_salary()
# mng.get_salary()
# dv.get_salary()

# class Transport:
#     def move(self):
#         pass

# class Car(Transport):
#     def move(self):
#         print(f'I can move in road')
    
# class Plane(Transport):
#     def move(self):
#         print(f'I can fly')

# class Boat(Transport):
#     def move(self):
#         print('I can swim')

# mers=Car()
# f35=Plane()
# titan=Boat()

# mers.move()
# f35.move()
# titan.move()

# class Payment:
#     def pay(self,amount):
#         pass
    
# class CashPayment(Payment):
#     def pay(self, amount):
#         print(f'Payed {amount} $')

# class CardPayment(Payment):
#     def pay(self, amount):
#         print(f'Payed {amount} $ online')
        
# pay1=CashPayment()
# pay2=CardPayment()

# pay1.pay(200)
# pay2.pay(500)

# class Person:
#     def __init__(self,name) -> None:
#         self.name=name
    
#     def get_info(self):
#         pass

# class Student(Person):
#     def __init__(self, name,grade) -> None:
#         super().__init__(name)
#         self.grade=grade
#     def get_info(self):
#         print(f'Name --> {self.name}\nGrade --> {self.grade}\n')

# class Teacher(Person):
#     def __init__(self, name,subject) -> None:
#         super().__init__(name)
#         self.subject=subject    
#     def get_info(self):
#         print(f'Name {self.name}\nSubject --> {self.subject}')

# std1=Student('Umar',5)
# std2=Teacher('Usmon','arabic language\n')

# std1.get_info()
# std2.get_info()


# class Bird:
#     def fly(self):
#         pass

# class Eagle(Bird):
#     def fly(self):
#         print(f'Eagle can flying')

# class Penguin(Bird):
#     def fly(self):
#         print(f'Penguin can not flying')

# eagle=Eagle()
# penguin=Penguin()

# eagle.fly()
# penguin.fly()

