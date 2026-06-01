class Payment:
    def __init__(self,amt):
        self.__amt=amt
    
    def get_amt(self):
        return self.__amt
    
    def set_amt(self,new_amt):
        if new_amt>0:
            self.__amt=new_amt

class Manager(Payment):
    def __init__(self):
        self.payment=[]

    def create(self,payment):
        self.payment.append(payment)

    def read(self):
        for i,pay in enumerate(self.payment):
            print(i,pay.get_amt())
# class Cash(Payment):
#     def show(self):
#         print(f'Paid {self.get_amt()} by cash')

# class Card(Payment): 
#     def show(self):
#         print(f'Paid {self.get_amt()} by card')

# class Online(Payment):
#     def show(self):
#         print(f'Paid {self.get_amt()} online')
