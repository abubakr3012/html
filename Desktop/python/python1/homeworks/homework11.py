from colorama import Fore,Style
# class Calc:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def jam(self):
#         return self.a+self.b
#     def tarh(self):
#         return self.a-self.b
#     def zarb(self):
#         return self.a*self.b
#     def taqsim(self):
#         if self.b==0:
#             return f"{Style.BRIGHT}{Fore.RED}Error!{Style.RESET_ALL}"
#         return self.a//self.b
#     def show(self):
#         return f"""
# a==> {self.a}
# b==> {self.b}
# """
# a=int(input())
# b=int(input())
# x=Calc(a,b)
# print(f"{a}+{b}={x.jam()}")
# print(f"{a}-{b}={x.tarh()}")
# print(f"{a}*{b}={x.zarb()}")
# print(f"{a}//{b}={x.taqsim()}")


# class Stud:
#     def __init__(self,name):
#         self.name=name
#         self.b=[]
#     def add_b(self,b):
#         self.b.append(b)
#     def ave(self):
#         if len(self.b)==0:
#             return 0
#         return sum(self.b)/len(self.b)
#     def show(self):
#         x=None
#         y=(sum(self.b)/len(self.b))
#         if y>=4.0 and y<=5.0: 
#             x='EXCELLENT'
#         elif y>=3.0 and y<4.0:
#             x='GOOD'
#         elif y>=2.0 and y<3.0:
#             x='BAD'
#         print(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}NAME ==> {self.name.upper()}{Style.RESET_ALL}")
#         print(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}NUMBERS ==> {self.b}{Style.RESET_ALL}")
#         print(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}AVERAGE OF {self.name.upper()} IS ==> {self.ave()}. IT IS {x}{Style.RESET_ALL}")
#         print()
# ls=int(input(f'{Style.BRIGHT}{Fore.BLUE}HOW MANY STUDENTS YOU WANT TO ADD ==> {Style.RESET_ALL}'))
# lst=[]
# for i in range(ls):
#         name=input(f'{Style.BRIGHT}{Fore.LIGHTCYAN_EX}STUDENT NAME ==> {Style.RESET_ALL}')
#         b=list(map(int, input(f'{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}ENTER 5 NUMBER OF STUDENT ==> {Style.RESET_ALL}').split()))  

#         std=Stud(name) 

#         for i in b:
#              std.add_b(i)
        
#         lst.append(std)
#         print()

# for i in lst:
#      i.show()