# def factorial(a):
#     if a==1:
#         return 1
#     return a*factorial(a-1)

# print(factorial(5))

# def fibonachi(a):
#     if a==0:
#         return 0
#     elif a==1:
#         return 1
#     return fibonachi(a-1)+fibonachi(a-2)
# print(fibonachi(7))

# def sm(a):
#     if a==1:
#         return 1
#     return a+sm(a-1)
# a=int(input())
# print(sm(a))

# def pw(a,b):
#     if b==0:
#         return 1
#     elif b==1:
#         return a
#     return a*pw(a,b-1)
# print(pw(2,3))

def fun(lst):
    if len(lst)==1:
        return lst[0]
    return lst[-1]+fun(lst[0:-1])
a=[1,2,3,4,5]
print(fun(a))