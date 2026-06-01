import asyncio
import random
from datetime import datetime
#1

# async def fun1():
#     await asyncio.sleep(2)
#     print('File 1 is downloaded!')
# async def fun2():
#     await asyncio.sleep(4)
#     print('File 2 is downloaded!')
# async def fun3():
#     await asyncio.sleep(1)
#     print('File 3 is downloaded!')
# async def  show():
#     await asyncio.gather(
#         fun1(),
#         fun2(),
#         fun3()
#     )
#     print('All downnloads finished!')
# asyncio.run(show())

#2

# a=input()
# b=input()

# async def user1():
#     await asyncio.sleep(2)
#     print('\n'+a)

# async def user2():
#     await asyncio.sleep(1)
#     print('\n'+b)

# async def show():
#     await asyncio.gather(
#         user1(),
#         user2()
#     )
# asyncio.run(show())

#3

# nms='1234567890'
# alpha1='qwertyuiopasdfghjklzxcvbnm'
# alpha2='QWERTYUIOPASDFGHJKLZXCVBNM'
# pas=nms+alpha1+alpha2
# password=''
# ln=random.randint(8,12)
# for i in range(ln):
#     password+=random.choice(pas)

# print(password)


#4
# nm='123456'
# u1=0
# u2=0
# for i in range(1,11):
#     p1=random.randint(1,6)
#     p2=random.randint(1,6)
#     if p1>p2:
#         u1+=1
#     elif p1<p2:
#         u2+=1
# print('User 1 --> ',u1)
# print('User 2 --> ',u2)

# if u1>u2:
#     print('User 1 wins!')
# elif u1<u2:
#     print('User 2 wins!')
# else:
#     print('Draw')

#5

# a=input('Enter your birthday day.month.year --> ')
# x=datetime.strptime(a,'%d.%m.%Y')
# now=datetime.now()
# y=now-x
# print(f'{y.days} days\n{y.days//12} month\n{y.days//365} years')

#6

# a=input('Enter date at future (day/month/year)--> ')
# date=datetime.strptime(a,'%d/%m/%Y')
# now=datetime.now()    
# print(date-now)

#7

# async def  fun1():
#     await asyncio.sleep(2)
#     with open('my_file.txt','a') as file:
#         file.write(input())
#         f1=datetime.now()

# async def  fun2():
#     await asyncio.sleep(1)
#     with open('my_file.txt','a') as file:
#         file.write('\n'+input())
#         f2=datetime.now()

# async def  fun3():
#     await asyncio.sleep(3)
#     with open('my_file.txt','a') as file:
#         file.write('\n'+input())
#         f3=datetime.now()

# async def  fun4():
#     await asyncio.sleep(3)
#     with open('my_file.txt','a') as file:
#         file.write('\n'+input())
#         f4=datetime.now()

# async def  fun5():
#     await asyncio.sleep(1)
#     with open('my_file.txt','a') as file:
#         file.write('\n'+input())
#         f5=datetime.now()

# async def show():
#     await asyncio.gather(
#         fun1(),
#         fun2(),
#         fun3(),
#         fun4(),
#         fun5()
#     )

# asyncio.run(show())

# async def std():
#     for i in range(5):


# nums='0123456789'
# password=''
# x=random.randint(0,9)
# for i in range(8):
#     password+=random.choice(nums)

# print(password)

# ls=['Abubakr','Umar','Usmon','Ali','Hasan']
# name=random.choice(ls)
# print(name)

# nums='1234567890'
# l_a='qwertyuioplkjhgfdsazxcvbnm'
# u_a='QWERTYUIOPLKJHGFDSAZXCVBNM'
# gen=nums+l_a+u_a
# pas=''
# for i in range(12):
#     pas+=random.choice(gen)
# print(pas)

# name=input('Enter your name --> ').upper()
# with open('my_file.txt','a') as file:
#     file.write('\n'+name)

# with open('my_file.txt','r') as file:
#     print(file.read())


# name=input('Enter name --> ').upper()

# try:
#     with open('my_file.txt','r') as file:
#         users=file.readlines()
#     cnt=0
#     for i in users:
#         if i.strip()==name:
#             cnt=1
#             break
#     if cnt==1:
#         print('User found!')
#     else:
#         print('User is not found!')
    
# except FileNotFoundError:
#     print('File is not found!')


now=datetime.now()
date=now.strftime('%d-%m-%Y %H:%M')
print(date)