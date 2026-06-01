#1

# a=int(input())
# b=int(input())
# for i in range(a,b):
#     if i%2==0:
#         print(i,end=" ")

#2

# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# for i in range(a,b):
#     if i%d==c:
#         print(i,end=" ")

#3

# a=int(input())
# b=int(input())
# for i in range(a,b+1):
#     if i**0.5==int(i**0.5):
#         print(i,end=" ")

#7

# a=int(input())
# for i in range(2,a+1):
#     if a%i==0:
#         print(i)
#         break

#8

# a=int(input())
# for i in range(2,a+1):
#     if a%i==0:
#         print(i,end=" ")

#9

# a=int(input())
# cnt=1
# for i in range(2,a+1):
#     if a%i==0:
#         cnt+=1

# print(cnt)

#10

# sm=0
# cnt=0
# while True:
#     n=int(input())
#     cnt+=1
#     if cnt==100:
#         break
#     sm+=n
# print(sm)

#11

# a=int(input())
# cnt=0
# for i in range(a):
#     b=int(input())
#     cnt+=b
# print(cnt)

#12

# a=list(map(int,input().split()))
# cnt=0
# for i in a:
#     if i==0:
#         cnt+=1

# print(cnt)

#13

# a=list(map(int,input().split()))
# cnt=0
# p=0
# n=0
# for i in a:
#     if i==0:
#         cnt+=1
#     if i>0:
#         p+=1
#     elif i<0:
#         n+=1
# print(cnt,p,n,end=" ")

#14

# a=list(map(int,input().split()))
# cnt=0
# for i in a:
#     if i==0:
#         cnt+=1
# if cnt==0:
#     print('NO')
# else:print('YES')

#15

# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# for i in range(0,1001):
#     if a*i**3+b*i**2+c*i+d==0:
#         print(i,end=" ")

#16

# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# for i in range(1001,0):
#     if a*i**3+b*i**2+c*i+d==0:
#         print(i,end=" ")

#17

# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# e=int(input())
# for i in range(0,1001):
#     if i!=e and a*i**3 + b*i**2 + c*i+d ==0:
#         print(i,end=" ")

#19

# a=int(input())
# cnt=0
# while a>0:
#     cnt+=a%10
#     a//=10
# print(cnt)

#20

# a=int(input())
# cnt=0
# while a>0:
#     if a%10==0:
#         cnt+=1
#     a//=10
# print(cnt)


#21

# a=int(input())
# mx=-9999
# mn=9999
# while a>0:
#     if a%10>mx:
#         mx=a
#     if a%10<mn:
#         mn=a
#     a//=10
# print(mn,mx,end=" ")

#23

# a=int(input())
# while a>0:
#     print(a%10)
#     a//=10


18