from colorama import Fore,Style,Back
#1

# class Info:

#     name=None
#     username=None
#     password=None

#     def show_info(self):
#         print(self.name)
#         print(self.username)
#         print(self.password)

# user1=Info()
# user1.name=str(input())
# user1.username=str(input())
# user1.password=str(input())

# user2=Info()
# user2.name=str(input())
# user2.username=str(input())
# user2.password=str(input())

# print(user1.show_info())
# print(user2.show_info())

#2

class Info:
    def __init__(self,name,username,password):
        self.name=name
        self.username=username
        self.password=password
    def show(self):
        return f"""
name ==> {self.name}        
username ==> {self.username}
password ==> {self.password}"""
Style.BRIGHT
Fore.LIGHTGREEN_EX
ls=int(input("How manu users you want to send ==> "))
Style.RESET_ALL
lst = []
for i in range(ls):
    a=Info(
        input('Name ==> '),
        input('Username ==> '),
        input('Password ==> ')
    )
    print()
    if a not in lst:
        lst.append(a)
    else:
        print(f"{Style.BRIGHT}This username is added! {Style.RESET_ALL}")
        break
for i in lst:
    print(i.show())