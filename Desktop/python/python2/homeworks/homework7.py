# def fun1(a):
#     return a**2
# print(fun1(int(input())))

# def fun2(a,b):
#     print(a+b)
# fun2(int(input()),int(input()))

# def fun3(a):
#     if a%2==0:
#         print(True)
#     elif a%2!=0:
#         print(False)
# fun3(int(input()))

# def fun4(a):
#     return len(a)
# print(fun4(input()))

# def fun5(a,b):
#     if a>b:print(a)
#     elif a<b:print(b)
# a=int(input())
# b=int(input())
# fun5(a,b)

# def fun6(*args):
#     sm=0
#     for i in args:
#         sm+=i
#     print(sm)
# a=list(map(int,input().split()))
# fun6(*a)

# def fun7(a):
#     print(a.upper())
# fun7(input())

# def fun8(*args):
#     for i in args:
#         if i%2==0:
#             print(i,end=" ")
# a=list(map(int,input().split()))
# fun8(*a)

# def fun9(a):
#     print(a[::-1])
# fun9(input())

# def fun10(*args):
#     mx=-999
#     for i in args:
#         if i>mx:
#             mx=i
#     print(mx)

# a=list(map(int,input().split()))
# fun10(*a)

# def fun11(*args):
#     a='eyuioa'
#     cnt=0
#     for i in args:
#         if i in a:
#             cnt+=1
#     print(cnt)
# a=list(map(str,input().split()))
# fun11(*a)

# def fun12(a):
#     sm=0
#     for i in range(1,a+1):
#         sm+=i
#     print(sm)
# a=int(input())
# fun12(a)

# def fun13(*args):
#     for i in args:
#         if i>0:
#             print(i,end=" ")

# a=list(map(int,input().split()))
# fun13(*a)

# def fun14(a):
#     b=a[::-1]
#     if a==b:
#         print(True)
#     else:
#         print(False)
# a=input()
# fun14(a)

# def fun15(*args):
#     mx=-9999
#     mx2=-9999
#     for i in args:
#         if i>mx:
#             mx=i
#     for i in args:
#         if i>mx2 and i<mx:
#             mx2=i
#     print(mx2)

# a=list(map(int,input().split()))
# fun15(*a)

# def fun16(l):
#     a={}
#     for i in l:
#         if i in a:
#             a[i]+=1
#         else:
#             a[i]=1
#     print(a)
# a=input()
# fun16(a)

# def fun17(*args):
#     x=[]
#     for i in args:
#         if i not in x:
#             x.append(i)
#     print(x)

# a=list(map(int,input().split()))
# fun17(*a)

# def fun18(*args):
#     b=''
#     for i in args:
#         if len(i)>len(b):
#             b=i
#     print(b)

# a=list(map(str,input().split()))
# fun18(*a)

# def fun19(x):
#     ls=[]
#     for i in range(x):
#         if i==0:
#             ls.append(0)
#         elif i==1:
#             ls.append(1)
#         else:
#             ls.append(ls[-1]+ls[-2])
#     print(ls)
# a=int(input())
# fun19(a)
# def fun20(*args):
#     ls=[]
#     for i in args:
#         if i%2!=0:
#             ls.append(i**2)
#     print(ls)

# a=list(map(int,input().split()))
# fun20(*a)

# def fun21(a):
#     ls=[]
#     for i in a:
#         if i not in ls:
#             ls.append(i)
#     print(ls)
# a=input()
# fun21(a)