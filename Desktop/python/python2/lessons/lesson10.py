# def balance(a):
#     sm=a
#     def withraw(b):
#         nonlocal sm
#         if b>sm:
#             return f'You have not {b} money in your balance'
#         else:
#             sm-b
#         return sm
#     def deposit(c):
#         nonlocal sm
#         sm+c
#         return sm
#     return deposit,withraw

# def balance(a):
#     def deposit(n):
#         nonlocal a
#         a+=n
#         return a
#     def withdraw(n):
#         nonlocal a
#         if a<n:
#             return 'Not money'
#         a-=n
#         return a
#     return deposit,withdraw

# dep,wiz=balance(0)
# print(dep(150))
# print(wiz(200))


# recursion,closure,inmutabe,mutable,string