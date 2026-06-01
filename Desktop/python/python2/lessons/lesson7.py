# while True:
#     try:
#         a=list(map(int,input().split()))
#         sm=0
#         for i in a:
#             sm+=i
#         print(sm)
#     except ValueError:
#         print('The value is error')
#     else:
#         print('Type of a is integer')
#     finally:
#         print('Program is running')
#         print()


# def my_print(a):
#     print(a)
# a=input()
# my_print(a)

# def mx_num(*args):
#     mx=-9999
#     for i in args:
#         if i>mx:
#             mx=i
#     print(mx)
# a=list(map(int,input().split()))
# mx_num(*a)

# def fun(**kwargs):
#     sm=0
#     for k,v in kwargs.items():
#         sm+=v
#     print(sm)
# a={'a':12,'b':10,'c':30}
# fun(**a)


# def fun(*args,**kwargs):
#     sm=0
#     for i in args:
#         sm+=i
#     print(sm)
#     for k,v in kwargs.items():
#         print(k,v)

# fun(1,2,3,name='Ali',age=20)