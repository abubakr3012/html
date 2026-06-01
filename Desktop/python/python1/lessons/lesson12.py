# class Father:
#     def __init__(self,user):
#         self.user=user
#     def __str__(self):
#         return self.user
# class Child(Father):
#     pass
# a=str(input())
# c1=Child(user=a)
# print('Your username is ==>', c1.__str__())

import math
class Parent:
    def __init__(self, last_name, money = 0, car = 0):
        self.last_name = last_name
        self.money = money
        self.car = car

    def show_money_inheret(self):
        return f'{self.money}$'
    
    def coun_car(self):
        return f"Count cars -- > {self.car}"
    
    def meroshoi_padar(self):
        return f"""
            Last name -> {self.last_name},
            Legacy -> {self.money}$
            Cars -> {self.car}        
        """
    
class Child(Parent):
    def init(self, age, name, home, gold, last_name, money=0, car=0):
        super().__init__(last_name, money, car)
        self.age = age
        self.name = name 
        self.home = home
        self.gold = gold

    def child_legacy(self):
        return f"""
            Age -> {self.age},
            Name -> {self.name},
            Home -> {self.home},
            Gold -> {self.gold} kg,        
        """
    def gold_by_dollar(self):
        return f'{math.floor(self.gold / 0.31 * 5100 * 960)}$'

