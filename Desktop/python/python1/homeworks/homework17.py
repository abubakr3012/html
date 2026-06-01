from datetime import datetime, time,timedelta,date
import random

#1

# a=int(input())
# b=int(input())
# gn=random.randint(a,b)
# print(gn)

#2

# a=int(input())
# ls=[]
# for i in range(a):
#     gn=random.randint(1,100)
#     ls.append(gn)
# print(ls)

#3

# names=list(map(str,input().split()))
# name=random.choice(names)
# print(name)

#4

# num=list(map(int,input().split()))
# random.shuffle(num)
# print(num)

#5

# a=int(input())
# ls=''
# nums='1234567890'
# for i in range(a):
#     ls+=random.choice(nums)
# print(ls)

#6

# names=list(map(str,input().split()))
# name=random.choice(names)
# print(name)

#7

# a=int(input())
# if a<=50 and a>=1:
#     nums=random.sample(range(1,51),a)
#     print(nums)

#8

# ls=list(map(int,input().split()))
# nums=[]
# n1=random.choice(ls)
# nums.append(n1)
# ls.remove(n1)
# n2=random.choice(ls)
# nums.append(n2)
# ls.remove(n2)
# print(*nums)

# ls=list(map(int,input().split()))
# a=random.sample(ls,2)
# print(a)

#9

# com=random.randint(1,10)
# a=int(input())
# if a==com:
#     print('Correct')
# else: print('Wrong')

#10

#11

# now=datetime.now()
# print(now)

#12

# a=input('Year.month.day --> ')
# a=datetime.strptime(a,'%Y.%m.%d')
# print(a)

#13

# a=input('Year.month.day 1 --> ')
# b=input('Year.month.day 2 --> ')
# d1=datetime.strptime(a,'%Y.%m.%d')
# d2=datetime.strptime(b,'%Y.%m.%d')
# x=abs(d1-d2)
# print(x)

#14

# a=input('Year.month.day --> ')
# b=int(input())
# d=datetime.strptime(a,f'%Y.%m.%d')
# d1=d+timedelta(days=b)
# print(d1)

#15

# a=input('Year.month.day --> ')
# b=int(input())
# d=datetime.strptime(a,f'%Y.%m.%d')
# d1=d-timedelta(days=b)
# print(d1)


#16

# a=input('Year.month.day --> ')
# d=datetime.strptime(a,'%Y.%m.%d')
# print(d.strftime('%A'))

#17

# now=datetime.now()
# print(now.strftime('%H:%M:%S'))

#18

# a=input('Year.month.day --> ')
# x=datetime.strptime(a,'%Y.%m.%d')
# now=datetime.today()

# print((x-now).days)

#19

# a=input('Year.month.day --> ')
# d=datetime.strptime(a,f'%Y.%m.%d')
# d1=d+timedelta(days=30)
# print(d1.strftime('%Y.%m.%d'))

# 20

# now=datetime.today()
# a=input('Year.month.day --> ')
# x=datetime.strptime(a,'%Y.%m.%d')
# mn=abs((now-x).days)
# print(mn//365)