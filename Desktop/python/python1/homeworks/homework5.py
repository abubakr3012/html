#1
# st=set(map(str,input().split()))
# cnt=0
# for i in st:
#     if i.isdigit():
#         cnt+=int(i)
# print(cnt)

#2

# st=set(map(str,input().split()))
# cnt=0
# for i in st:
#     if i.isdigit():
#         cnt+=len(i)
# print(cnt)

#3












#4

# st=input().split()
# for i in st:
#     if i .isalpha():
#         print(i, end=" ")

#5

# st=input().split()
# for i in st:
#     if i.isdigit():
#         print(i, end=" ")

#6

# st=input().split()
# b=input()
# x=False
# for i in st:
#     if i in b:
#         x=True
#         break
#     else:
#         x=False
# if x==True:
#     print('YES')
# else:
#     print('NO')

#7

# st=input().split()
# b=input()
# s=[]
# for i in range(0, len(st),2):
#     s.append((st[i], st[i+1]))
# for k,v in s:
#     if k in b:
#         print(v)

#8

# st=input().split()
# b=input()
# s={}
# for i in st:
#     s.append(b)
# print(s)

#9

#10

# st=set(map(int,input().split()))
# sum=0
# for i in st:
#     sum+=i
# print(sum)

#11

# st=set(map(int,input().split()))
# for i in st:
#     s=len(st)
# print(s)

#12

# st=set(map(str,input().split()))
# b=str(input())
# x=False
# for i in st:
#     if i in b:
#         x=True
#         break
# if x==True:
#     print('YES')
# else:
#     print('NO')

#13

# st=list(map(str,input().split()))
# x=input()
# st.append(x)
# st.sort()
# print(*st)

#14

# st=list(map(str,input().split()))
# x=input()
# st.remove(x)
# print(st)

#15

# st=list(map(str,input().split()))
# st.sort()
# s=set(st)
# print(s)

#16

# s1=set(map(int,input().split()))
# s2=set(map(int,input().split()))
# s=s1&s2
# print(s)