#1

# def outter():
#     lst=[]
#     def inner(a):
#         lst.append(a)
#         return lst
#     return inner

# a=outter()
# print(a(5))
# print(a(22))
# print(a(15))

#2

# def outter():
#     mn=9999
#     def inner(n):
#         nonlocal mn
#         if n<mn:
#             mn=n
#         return mn
#     return inner

# a=outter()
# print(a(5))
# print(a(25))
# print(a(15))

#3

# def outter():
#     t=''
#     def inner(a):
#         nonlocal t
#         if len(a)>len(t):
#             t=a
#         return t
#     return inner

# a=outter()
# print(a('salom'))
# print(a('elephant'))
# print(a('hello'))

#4

# def outter():
#     even=[]
#     def inner(a):
#         nonlocal even
#         if a%2==0:
#             even.append(a)
#         return even
#     return inner
# a=outter()
# print(a(7))
# print(a(6))
# print(a(3))

#5

# def outter():
#     sm=0
#     def inner(a):
#         nonlocal sm
#         sm+=a
#         return sm
#     return inner

# a=outter()
# print(a(5))
# print(a(15))

#6

# def outter(a):
#     def inner(b):
#         return b>a
#     return inner

# a=outter(10)
# print(a(20))
# print(a(2))

#7

# def outter(a):
#     cnt=0
#     def inner(b):
#         nonlocal cnt
#         if a==b:
#             cnt+=1
#         return cnt
#     return inner

# a=outter('python')
# print(a('java'))
# print(a('c++'))
# print(a('python'))
# print(a('python'))

#8

# def outter(a):
#     cnt=0
#     def inner():
#         nonlocal cnt
#         cnt+=1
#         if cnt>a:
#             return 'Limit reached'
#         elif cnt<=a:
#             return 'OK'
#     return inner

# a=outter(3)
# print(a())
# print(a())
# print(a())

#9

# def ouuter():
#     ls=None
#     def inner(a):
#         nonlocal ls
#         p=ls
#         ls=a
#         return p
#     return inner

# a=ouuter()
# print(a(5))
# print(a(10))
# print(a(15))

#10

# def outter():
#     sm=0.0
#     cnt=0
#     def inner(a):
#         nonlocal sm,cnt
#         sm+=a
#         cnt+=1
#         return sm/cnt
#     return inner

# a=outter()
# print(a(10))
# print(a(20))
# print(a(30))