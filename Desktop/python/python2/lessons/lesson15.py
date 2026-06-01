class User:
    def __init__(self,name,age,balance) -> None:
        self.name=name
        self.age=age
        self.balance=balance
    
    def __str__(self):
        return f'''
Name {self.name}
Age {self.age}
Balance {self.balance}
'''
    def __add__(self, other):
        return self.balance+other
    def __sub__(self, other):
        return self.balance-other
    def __mul__(self, other):
        return self.balance*other
    def __eq__(self, value: object):
        return self.age==value
    def __gt__(self, other):
        return self.age>other
user1=User('Ali',20,1000)
user2=User('vali',20,1000)
a=6
b=10
print(user1)
print(user1+10)
print(user1-10)
print(user1*10)
print(user1==user2)
print(a>b)
