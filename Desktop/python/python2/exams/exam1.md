Python Exam — 10 Tasks
Task 1
Введите 3 числа. Выведите:
• их сумму
• их среднее арифметическое
• остаток от деления суммы на 2

Example
Input:
4
6
5

Output:
Sum = 15
Avg = 5.0
Sum%2 = 1

a=int(input())
b=int(input())
c=int(input())
sm=a+b+c
avg=sm/3
print(f'Sum = {sm}')
print(f'Avg = {avg}')
print(f'Sum%2 = {sm%2}')

Task 2
Введите количество минут. Переведите это значение в дни, часы и минуты.

ExampleInput:
3500

Output:
Days = 2
Hours = 10
Minutes = 20

a=int(input())
day=a//24//60 
minute=a%60
hour=minute//day
print(f'Days = {day}')
print(f'Hours = {hour}')
print(f'Minutes = {minute}')

Task 3%
Введите число от 1 до 12. Используя match-case, выведите название месяца.

a=int(input())
match a:
    case 1:
        print('January')
    case 2:
        print('February')
    case 3:
        print('March')
    case 4:
        print('April')
    case 5:
        print('May')
    case 6:
        print('June') 
    case 7:
        print('Jule')
    case 8:
        print('August')
    case 9:
        print('September')
    case 10:
        print('October')
    case 11:
        print('November')
    case 12:
        print('December')



Task 4
Введите 3 стороны треугольника. Определите, существует ли такой треугольник.

a=int(input())
b=int(input())
c=int(input())
if (a+b)<c and (a+c)<b and (b+c)<a:
    print('YES')
else:
    print('NO')


Task 5
Пользователь вводит слова бесконечно.
Если введено слово "stop", программа должна остановиться.
Выведите последнее слово перед "stop".

Example
Input:
apple
banana
orange
stop

Output:
orange

ls=[]
while True:
    a=input()
    ls.append(a)
    if a=='stop':
        break
print(ls[-2])

Task 6
Введите двоичное число. Преобразуйте его в десятичное.

Example
Input:
101101

Output:
45


Task 7
Дан список чисел. Выведите все чётные элементы списка.

Example
Input:
[3, 8, 1, 12, 7, 6]

Output:
8 12 6

a=list(map(int,input().split()))
for i in a:
    if i%2==0:
        print(i,end=" ")

Task 8
Дан кортеж:

student = ("Ali", 19, ("Math", 90), ("Physics", 85), ("English", 88))

Распакуйте кортеж так, чтобы:
• отдельно получить имя
• отдельно получить возраст
• отдельно получить названия предметов
• отдельно получить баллы
• вывести средний балл студента

student = ("Ali", 19, ("Math", 90), ("Physics", 85), ("English", 88))
print('Name -->',student[0])
print('Age -->',student[1])
print(f'{student[2][0]} {student[3][0]} {student[4][0]}')
print(f'{student[2][1]} {student[3][1]} {student[4][1]}')
sm=student[2][1]+student[3][1]+student[4][1]
print(sm/3)

Task 9
Дан словарь. Поменяйте местами ключи и значения.

Example
Input:
{'a': 1, 'b': 2, 'c': 3}

Output:
{1: 'a', 2: 'b', 3: 'c'}

a = {"a":1,"b":2,"c":3}
b = {}
for i in a:
    b[a[i]] = i
print(b)


Task 10
Дан словарь, где значением каждого ключа является список чисел.
Выведите те ключи, у которых сумма элементов списка не является простым числом.

Example
Input:
{
'x': [1, 2, 3],
'y': [2, 3],
'z': [4, 4]
}

Output:
x z

dct={
'x': [1, 2, 3],
'y': [2, 3],
'z': [4, 4]
}
ls=[]
for k,v in dct.items():
    sm=sum(v)
print(sm)