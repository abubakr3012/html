# name='Abubakr'
# age=20
# adress='Dushanbe'

# print(f'My name is {name}\nI am {age} years old\nI am from {adress}')

# print('\nMy name is',name,'\n''I am',age,'years old''\n''I am from',adress)

# print(f'''
# My name is {name}
# I am {age} years old
# I am from {adress}
# ''')

# try:
#     a=int(input())
#     if a%2==0:
#         print('Even')
#     elif a%2!=0:
#         print('Odd')
# except:
#     print('Error!')
# finally:
#     print('Programm is done!')

a=int(input())
if a>0 and a%2==0:
    print('evm and positive')

elif a<0 and a%2!=0:
    print('odd and negative')

if a>0 and a%2!=0:
    print('evm and negative')