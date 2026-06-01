# def dec(fun):
#     def inner(a):
#         print('start')
#         f=fun(a)
#         print('end')
#         return f
#     return inner

# @dec
# def fun(a):
#     return a**2

# print(fun(2))

# def dec(fun):
#     def inner():
#         fun()
#         fun()
#         fun()
#     return inner

# @dec
# def word():
#     print('Hi')

# word()

# def dec(fun):
#     def inner(*args,**kwargs):
#         r=fun(*args,**kwargs)
#         if r is None:
#             return "Error"
#         return r
#     return inner

# @dec
# def fun(a):
#     return a

# print(fun(2))


# def dec(fun):
#     def inner(w):
#         return fun(w)
#     return inner

# @dec
# def fun(a):
#     return a

# print(fun('salom'))


# def dec(fun):
#     def inner(word):
#         word=word.strip()
#         word=word.upper()
#         return fun(word)
#     return inner

# @dec
# def fun(a):
#     return a

# print(fun('  salom  '))


# def dec(fun):
#     def inner(a,b):
#         if b==0:
#             return 'Error value'
#         return fun(a,b)
#     return inner

# @dec
# def fun(a,b):
#     return a/b

# print(fun(20,0))

 