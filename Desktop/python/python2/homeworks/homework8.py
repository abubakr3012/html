# def adder(a):
#     def inner(b):
#         return a+b
#     return inner

# a=adder(int(input()))
# print(a(int(input())))

# def count():
#     cnt=0
#     def inner():
#         nonlocal cnt
#         cnt+=1
#         return cnt
#     return inner
# a=count()
# print(a())
# print(a())
# print(a())

# def fun(lst):
#     def fun2(lst2):
#         for i in lst2:
#             if i>lst:
#                 return i
#     return fun2

# a=fun([2,4,5,-12,9])
# print(a(2,4,5,12))