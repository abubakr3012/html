# 1

# def sm(x):
#     if x==1:
#         return 1
#     return x+sm(x-1)
# x=int(input())
# print(sm(x))

# 2

# def fac(n):
#     if n<=1:
#         return 1
#     return fac(n-1)*n
# a=int(input())
# print(fac(a))

# 3

# def fib(n):
#     if n<=1:
#         return 1 
#     return fib(n-1)+fib(n-2)
# a=int(input())
# print(fib(a))

# 4

# def cn(n):
#     n=str(n)
#     if len(n)==1:
#         return 1
#     return 1+cn(n[:-1])
# a=int(input())
# print(cn(a))

# 5

# def sm(ls):
#     if len(ls)==1:
#         return ls[0]
#     return ls[0]+sm(ls[1:])
# ls=list(map(int,input().split()))
# print(sm(ls))

# 6

# def rec(x):
#     return list(range(1,x+1))
# a=int(input())
# print(*rec(a))

# 7

# def rec(x):
#     return list(range(x,0,-1))
# a=int(input())
# print(*rec(a))

# 8

# def pw(x,y):
#     if y==0:
#         return 1
#     return x*pw(x,y-1)
# x=int(input())
# y=int(input())
# print(pw(x,y))

# 9 

# def pal(x):
#     x=str(x)
#     y=x
#     if len(x)<=1:
#         return 'YES'
#     if x[0]!=x[-1]:
#         return 'NO'
#     return pal(x[1:-1])
# x=str(input())
# print(pal(x))

# 10

# def mx(ls):
#     if len(ls)==1:
#         return ls[0]
#     x=mx(ls[1:])
#     return ls[0] if ls[0]>x else x
# ls=list(map(int,input().split()))
# print(mx(ls))
