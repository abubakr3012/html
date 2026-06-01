# def f_fun(a): 
#     def s_fun(b):
#         def t_fun(c):
#             return a+b+c
#         return t_fun
#     return s_fun
# a=int(input())
# b=int(input())
# c=int(input())
# a1=f_fun(a)
# a2=a1(b)
# a3=a2(c)
# print(a3)

# def counter():
#     cnt=0
#     def inner():
#         nonlocal cnt
#         cnt+=1
#         return cnt
#     return inner
# fff=counter()
# a=int(input())
# for i in range(a):
#     print(fff())

# def sale(per):
#     def cal(price):
#         return price * per / 100
#     return cal
# per=sale(10)
# iphone=per(22000)
# samsung=per(12000)
# redmi=per(7000)
# print(f"Iphone 22000 10% sale {iphone}. You bcan buy it {22000-iphone}")
# print()
# print(f"Samsung 12000 10% sale {samsung}. You bcan buy it {22000-samsung}")
# print()
# print(f"Redmi 7000 10% sale {redmi}. You bcan buy it {22000-redmi}")


# def pass1(ps1):
#     def pass2(ps2):
#         return ps1==ps2
#     return pass2

# from colorama import Style,Fore
# def sm(*args):
#     cnt=0
#     for i in args:
#         if isinstance(i,(int,float)):
#             cnt+=i
#         else:
#             print(f"{Style.BRIGHT}{Fore.RED}It is not number!{Style.RESET_ALL}")
#             return
#     print(f"Sum of numbers ==> {cnt}")
# a=tuple(map(int,input().split()))
# sm(*a)

# def fun1(**kwargs):
#     for k,v in kwargs.items():
#         print(f"Key==>{k} Value==>{v}")
# d=input().split()
# x={}
# for i in range(0,len(d),2):
#     x[d[i]]=d[i+1]
# fun1(**x)