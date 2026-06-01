import asyncio
from math import floor
from time import time
# async def function1():
#     await asyncio.sleep(5)
#     print('Hello function 1')

# async def function2():
#     await asyncio.sleep(2)
#     print('Hello function 2')

# async def function3():
#     await asyncio.sleep(6)
#     print('Hello function 3')

# async def main():
#     await asyncio.gather(
#         function1(),
#         function2(),
#         function3(),
#     )

# st=time()
# asyncio.run(main())
# en=time()
# print(en-st)

#1

# async def download_user():
#     await asyncio.sleep(2)
#     print('User downloaded!')

# async def download_orders():
#     await asyncio.sleep(3)
#     print('Orders are downloaded!')

# async def download_balance():
#     await asyncio.sleep(1)
#     print('Balance downloaded!')

# async def show():
#     await asyncio.gather(
#         download_user(),
#         download_orders(),
#         download_balance()
#     )
# asyncio.run(show())
# print('All inf are downloaded!')

#2

# async def get_price():
#     for i in range(5):
#         await asyncio.sleep(1)
#         print(i,end=" ")
        
# async def check_signal():
#     for i in range(3):
#         await asyncio.sleep(2)
#         print('Signal is provered!')

# async def show():
#     await asyncio.gather(
#         get_price(),
#         check_signal()
#     )

# asyncio.run(show())

#3

# async def function():
#     await asyncio.sleep(5)
#     print('Task finished!')

# async def show():
#     try:
#         await asyncio.wait_for(function(),timeout=2)
#     except asyncio.TimeoutError:
#         print('Time is finished')

# asyncio.run(show())

# try:
#     a=int(input('Enter number 1 --> '))
#     b=int(input('Enter number 2 --> '))
#     sm=a+b
# except ValueError:
#     print("To zero we can't do division ")
# else:
#     print(f'{a}+{b}={sm}')
# finally:
#     print('the programm finished!')



# try:
#     a=int(input('Enter first number --> '))
#     b=int(input('Enter second number --> '))
#     t=a//b
# except ValueError:
#     print('Please enter a number!')
# except ZeroDivisionError:
#     print("Please don't enter zero!")
# else:
#     print(f'{a}//{b}={t}')
# finally:
#     print('\nProgram finished!\n')

# try:
#     with open('my_file.txt','r') as file:
#         f=file.read()
#         print(f)
# except:
#     print('File is not found! Please create a new file!')

# finally:
#     ('Programm finished!')



# async def task1():
#     await asyncio.sleep(2)
#     print('Task 1 added!')

# async def task2():
#     await asyncio.sleep(4)
#     print('Task 2 added!')
# async def task3():
#     await asyncio.sleep(1)
#     print('Task 3 added!')

# async def show():
#     await asyncio.gather(
#         task1(),
#         task2(),
#         task3()
#     )
#     print('All tasks are does!')
# try:
#     st=time()
#     asyncio.run(show())
#     ed=time()
#     print(floor(ed-st))
# finally:
#     print('Programm finised!')

# a=input('Enter a alpabet --> ').lower()
# cnt=0
# with open('my_file.txt','r') as file:
#     f1=file.read()

#     for i in f1:
#         if a==i.lower():
#             cnt+=1
# print(cnt)

#1

# try:
#     a=int(input('Enter first number --> '))
#     b=input('Your choise +-*/ --> ')
#     c=int(input('Enter first number --> '))
#     if b=='+':
#         print(f'{a}{b}{c}={a+c}')
#     elif b=='-':
#         print(f'{a}{b}{c}={a-c}')
#     elif b=='*':
#         print(f'{a}{b}{c}={a*c}')
#     elif b=='/':
#         print(f'{a}{b}{c}={a//c}')
#     else:
#         print('Operation is wrong!')
# except ValueError:
#     print('Please enter a number!')
# except ZeroDivisionError:
#     print('You cant not divide by zero!')
# finally:
#     print('Operation finished!')

#2

try:
    a=input('Enter text to save --> ')
    with open('my_file.txt','a') as file:
        file.write('\n'+a)
    print('Text added!')
except Exception:
    print('Wrong!')
finally:
    print('File is edited!')

#3

# async def task1():
#     await asyncio.sleep(3)
#     print('Task 1 added!')

# async def task2():
#     await asyncio.sleep(5)
#     print('Task 2 added!')
# async def task3():
#     await asyncio.sleep(2)
#     print('Task 3 added!')

# async def show():
#     await asyncio.gather(
#         task1(),
#         task2(),
#         task3()
#     )
#     print('All tasks are does!')
# try:
#     st=time()
#     asyncio.run(show())
#     ed=time()
#     print(floor(ed-st))
# finally:
#     print('Programm finised!')