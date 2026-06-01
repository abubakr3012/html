# def outter(a):
#     def inner(b):
#         return a+b
#     return inner
# a=outter(int(input()))
# print(a(int(input())))

# def outter(a):
#     def inner(b):
#         return a*b
#     return inner
# a=outter(int(input()))
# print(a(int(input())))

# def limit(a):
#     def lst(*args):
#         ls=[]
#         for i in args:
#             if i>a:
#                 ls.append(i)
#         return ls
#     return lst
# a=limit(int(input()))
# lst=list(map(int,input().split()))
# print(a(*lst))

# def outter(x):
#     def inner(y):
#         if y>x:
#             return True
#         elif y<x:
#             return False
#     return inner

# a=outter(int(input()))
# print(a(int(input())))

# def outter(a,b):
#     def inner(n):
#         lst=[]
#         for i in range(a,b+1):
#             lst.append(i)
#         if n not in lst:
#             return False
#         else:
#             return True
#     return inner
# a=outter(1,10)
# print(a(5))

# def outter(a,b):
#     def inner(n):
#         if a<n<b:
#             return True
#         else:
#             return False
#     return inner
# a=outter(1,10)
# print(a(5))

# def outter(a,b):
#     def inner(n):
#         return a<=n<=b
#     return inner
# a=outter(1,10)
# print(a(5))


# def outter(a):
#     def inner():
#         nonlocal a
#         a+=1
#     return inner
# count=outter()
# print(count())