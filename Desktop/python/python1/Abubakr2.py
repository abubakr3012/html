#1) Суммаи то n

# def fun(x):
#     sm=0
#     def fun2():
#         nonlocal sm
#         i=1
#         while i<=x:
#             sm+=i
#             i+=1
#     return sm
#     return fun2
# a=int(input())
# print(fun(a))


#2) Факториал



#3) Суммаи рақамҳо

# def fun(a):
#     sm=0
#     def fun2():
#         nonlocal sm
#         i=a
#         while i>0:
#             sm+=i
#             i//=10
#     return fun2
# a=int(input())
# print(fun(a))


# #4) Квадрат

# a=int(input())
# lm=lambda ls:[a**2]
# print(*lm(a))

#5) Максимум

# a=int(input())
# b=int(input())
# mx=lambda lst: [a if a>b else b]
# print(*mx(a))

#6
# a=list(map(int,input().split()))
# x=lambda lst: [i**2 for i in a]
# print(*x(a),end=" ")

#8) Мултипликатор

# def fun(k):
#     def fun2(x):
#         return k*x
#     return fun2
# a=int(input())
# b=int(input())
#print(fun(k,x))
