# def my_d(f):
#     def inn():
#         print(f'Your name ==> {f}')
#         f()
#         print(f'Your age ==> 12')
#     return inn

# @my_d
# def name(a):
#     return a
# a=str(input())
# print(name(a))



# def dec(fun):
#     def inner(*args,**kwargs):
#         print(args,kwargs)
#         return fun(*args, **kwargs)
#     return inner
# @dec
# def sm(a,b):
#     return a+b
# a=int(input())
# b=int(input())
# print(sm(a,b))

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

