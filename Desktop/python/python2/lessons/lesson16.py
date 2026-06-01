# def decorator(fun):
#     def inner():
#         print('Start')
#         fun()
#         print('End')
#     return inner

# @decorator
# def say_hello():
#     print('Hello')

# say_hello()

# def decorator(fun):
#     def inner(a,b):
#         print(f'a={a}')
#         fun(a,b)
#         print(f'b={b}')
#     return inner

# @decorator
# def add(a,b):
#     print(a+b)

# add(2,3)

# def dec(fun):
#     def inner(*args):
#         try:
#             lst=[int(i) for i in args]
#             return fun(*lst)
#         except ValueError:
#             return 'Error'
#     return inner

# @dec
# def summ(*args):
#     return sum(args)
# print(summ(2,'5',7,True,False,True,'salom'))

# def dec(fun):
#     cnt=0
#     def inner(*args):
#         nonlocal cnt
#         try:
#             cnt+=1
#             lst=[int(i) for i in args]
#             return fun(*lst),cnt
            
#         except ValueError:
#             return 'Error'
#     return inner

# @dec
# def summ(*args):
#     return sum(args)

# print(summ(2,'5',7,True,False,True,))
# print(summ(2,'5',7,True,False,True,))

def dec(fun):
    def inner(*args):
        try:
            lst=[int(i) for i in args]
            return fun(*lst)
        except ValueError:
            return 'Error'
    return inner
@dec
def summ(*args):
    return sum(args)
print(summ(2,'5',7,True,False,True,'salom'))