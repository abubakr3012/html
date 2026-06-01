from datetime import date,time,datetime,timedelta
import random

#1 print(date.today())

#2 now=datetime.now
# (print(now.time())

# date='2026-3-31'
# date1=datetime.strptime(date,'%Y-%m-%d')
# print(date1.date())

# week=input('Enter date y/m/d -> ')
# date1=datetime.strptime(week,'%Y/%m/%d')
# print(date1.strftime('%A'))

# date1=datetime.now()
# x='2026-1-1'
# date2=datetime.strptime(x,'%Y-%m-%d')
# print((date1)-date2)

# date1=datetime.now()
# date2=date1+timedelta(days=5,hours=5)
# print(date2)

# birthday=input('Enter your birthday y-m-d -> ')
# date1=datetime.today()
# d1=datetime.strptime(birthday,'%Y-%m-%d')
# x=date1-d1
# print(x.days//365)

# time1=input('Enter time h:m:s -> ')
# time2=input('Enter time h:m:s -> ')
# times1=datetime.strptime(time1,'%H:%M:%S')
# times2=datetime.strptime(time2,'%H:%M:%S')
# x=times1-times2
# print(x)

# new_year='2026-05-27'
# now=datetime.today()
# x=datetime.strptime(new_year,'%Y-%m-%d')
# print(x-now)


#RANDOM


# lst=[]
# sm=0
# for i in range(10):
#     ran=random.randint(1,100)
#     lst.append(ran)
#     sm+=ran

# ran=random.choice(lst)
# random.shuffle(lst)

# print(lst)
# print(sm)
# print(ran)

# lst=[]
# lst2=[]
# for i in range(5):
#     ran=random.randint(1,20)
#     lst.append(ran)

# print(lst)
# for k in lst:
#     if k not in lst2:
#         lst2.append(k)
# print(lst2)

# b=any(j>15 for j in lst2)
# print(b)

# lst=["red", "blue", "green", "black"]
# # x=random.sample(lst,2)
# x=random.choices(lst,k=2)
# print(x)
# if x[0]==x[1]:
#     print('Same')
# else:
#     print('different')

# x=random.random()
# lst=[10,20,30,40]
# if x<0.5:
#     r=random.randint(1,10)
#     print(r)
# elif x==0.5:
#     print(random.choice(lst))

# lst=[1,2,3]
# lst2=random.choices(lst,weights=[1,2,7],k=10)

# print(lst2)
# for i in lst:
#     print(i,lst2.count(i))

# lst=[]
# for _ in range(8):
#     lst.append(random.randint(1,50))
# print(lst)

# random.shuffle(lst)
# x=random.sample(lst,3)
# print(lst)

# for i in x:
#     lst.remove(i)
# print(lst)

# lst=[]
# for _ in range(5):
#     lst.append(random.uniform(1.0,10.0))

# print(lst)
# lst2=[]
# for i in lst:
#     r=round(i,2)
#     lst2.append(r)

# print(min(lst2))
# print(max(lst2))

# lst=["python", "java", "c++", "js", "go"]
# random.shuffle(lst)
# lst2=lst[:3]

# print(lst2)
# print(random.choice(lst2))

# lst=random.randrange(0,20,2)
# if lst%4==0:
#     print('good')
# else:
#     print('normal')

# lst=[i for i in range(1,11)]
# lst2=random.choices(lst,k=7)
# dct={}
# for i in lst2:
#     dct[i]=lst2.count(i)

# for k,v in dct.items():
#     print(k,v)