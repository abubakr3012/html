#1

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

#2

# def mx(*args):
#     mx=-9999
#     for i in args:
#         if i>mx:
#             mx=i
#     print(f"Max==> {mx}")
# a=list(map(int,input().split()))
# mx(*a)

#3

# def ln(*args):
#     print(len(args))
# a=list(map(int,input().split()))
# ln(*a)

#4

# from colorama import Style,Fore
# def sm(*args):
#     cnt=1
#     for i in args:
#         if isinstance(i,(int,float)):
#             cnt*=i
#     print(cnt)
# a=tuple(map(int,input().split()))
# sm(*a)

#5

# def fun1(**kwargs):
#     for k,v in kwargs.items():
#         print(k,v)
# d=input().split()
# x={}
# for i in range(0,len(d),2):
#     x[d[i]]=d[i+1]
# fun1(**x)

#6

# def ln(**kwargs):
#     print(len(kwargs))
# a=input().split()
# x={}
# for i in range(0,len(a),2):
#     x[a[i]]=a[i+1]
# ln(**x)

#7

#8

# def n1(x):
#     def n2(y):
#         return x**y
#     return n2
# a=int(input())
# b=int(input())
# x=n1(a)
# print(x(b))

#9

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

#10
