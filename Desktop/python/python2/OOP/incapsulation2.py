class BankAccount:
    def __init__(self,owner,balance) -> None:
        self.owner=owner
        self.__balance=balance
    
    @property
    def balance(self):
        print(self.__balance)
    @balance.setter
    def balance(self,n):
        self.__balance=n

ob1=BankAccount('Ali',200)
ob1.balance
ob1.balance=50
ob1.balance