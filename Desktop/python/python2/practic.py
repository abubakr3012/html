# чопи элементхои индексашон чуфт
# a=(10,20,30,40)
# for i in range(0,len(a),2):
#     print(a[i],end=" ")

# ивази key ба value
# a = {"a":1,"b":2}
# b = {}
# for i in a:
#     b[a[i]] = i
# print(b)

# data = {
#     "a": 5,
#     "b": 12,
#     "c": 7
# }
# mx=-9999
# a=''
# for k,v in data.items():
#     if v>mx:
#         mx=v
#         a=k
# print(a)

# суммаи элементхои индексашон чуфт
# a=[1,-3,5,0,8,-2]
# sm=0
# for i in range(len(a)):
#     if i%2==0:
#         sm+=a[i]
# print(sm)

# ба value гузоштани дарозии калима аз list
# lst=["cat", "python", "code"]
# data={}
# for i in lst:
#     data[i]=len(i)
# print(data)

# dict бо индекс hello --> "h":1,"e":2,"l":3,"l":4,"o":5
# def fun(l):
#     a={}
#     for i in l:
#         if i in a:
#             a[i]+=1
#         else:
#             a[i]=1
#     print(a)
# a=input()
# fun(a)

# харфои такрорнашаванда
# def fun(a):
#     ls=[]
#     for i in a:
#         if i not in ls:
#             ls.append(i)
#     print(ls)
# a=input()
# fun(a)

#fibonachi
# def fun(x):
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
# fun(a)

#a pow b
# def pw(a,b):
#     if b==0:
#         return 1
#     elif b==1:
#         return a
#     return a*pw(a,b-1)
# print(pw(2,3))

#reverse with recursion
# def fun(a):
#     if len(a)==0:
#         return ''
#     return fun(a[1:])+a[0]
# print(fun(input()))

# sum of number 1234 --> 10
# def fun(a):
#     if a==0:
#         return 0
#     return a%10+fun(a//10)

# print(fun(int(input())))

#max element from list
# def fun(a):
#     if len(a)==1:
#         return a[0]
#     mx=fun(a[1:])
#     if a[0]>mx:
#         return a[0]
#     else: return mx
# lst=list(map(int,input().split()))
# print(fun(lst))

# reverse factorial
# def fun(a):
#     i=1
#     while a>1:
#         i+=1
#         a=a//i
#     if a==1:
#         return i
#     else:
#         pass

# a=int(input())
# print(fun(a))

#sum of elements list
# def fun(lst):
#     if not lst:
#         return 0
#     return lst[0]+fun(lst[1:])
# print(fun(list(map(int,input().split()))))

#нечётное number from list
# lst=list(map(int,input().split()))
# x=list(filter(lambda i: i%2!=0,lst))
# print(x)

# двумерный список --> одномерный
# lst=[[1,2],[3,4],[5,6]]
# fun=[j for i in lst for j in i]
# print(fun)

#4 fun=['Fizz' if i%3==0 
#     else 'Buzz' if i%5==0 
#     else i 
#     for i in range(1,31)]
# print(fun)

# количество строк и слов
# with open('users.txt','r') as file:
#     data=file.readlines()    
# ln=len(data)
# cnt=0
# for i in data:
#     w=i.split()
#     cnt+=len(w)

# print(ln)
# print(cnt)

#добавление цифр на файл
# lst=[]
# for i in range(10):
#     data=random.randint(1,100)
#     lst.append(data)
# print(lst)
# with open('users.txt','w') as file:
#     for i in lst:
#         file.write(str(i)+' ')
