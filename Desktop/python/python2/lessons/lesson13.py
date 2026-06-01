class Bank:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
        self.history=[]
    def deposit(self,d):
        self.balance+=d
        self.history.append(f'depostit {d} your balance {self.balance}\n')
    
    def withdraw(self,c):
        if c>self.balance:
            print('Noy money')
        self.balance-=c
        self.history.append(f'depostit {c} your balance {self.balance}\n')
    def show(self):
        print(f'Owner {self.owner} Balance {self.balance}')
    
    def show_history(self):
        print(self.history)
user1=Bank('Abubakr',1000)
user2=Bank('Umar',700)

user1.deposit(500)
user2.deposit(500)

user1.withdraw(100)
user2.withdraw(100)

user1.show()
user2.show()
