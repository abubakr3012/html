#1
# a=list(map(int,input().split()))
# print(*a[::2])

#2
  
# a=list(map(int,input().split()))
# for i in a:
#     if i%2!==0:
#         print(i,end=" ")

#3

# a=list(map(int,input().split()))
# cnt=0
# for i in a:
#     if i>0:
#         cnt+=1
# print(cnt)

#4

# a=list(map(int,input().split()))
# for i in range(1,len(a)):
#     if a[i]>a[i-1]:
#         print(a[i],end=" ")

#5

# a=list(map(int,input().split()))
# for i in range(len(a)):
#     if a[i]>0 and a[i+1]>0 and a[i-1]>0:
#         print(a[i],end=" ")

#6

# a=list(map(int,input().split()))
# cnt=0
# for i in range(1,len(a)-1):
#     if a[i]>a[i-1] and a[i]>a[i+1]:
#         cnt+=1
# print(cnt)

#7

# a=list(map(int,input().split()))
# for i in range(1,len(a)-1):
#     if a[i]>a[i-1] and a[i]>a[i+1]:
#         print(a[i],i,end=" ")

#8

# a=list(map(int,input().split()))
# b=[]
# cnt=0
# for i in range(1,len(a)-1):
#     if a[i]>0:
#         b.append(a[i])
# if len(b)>0:
#     print(b[-1])

#9

# a=list(map(int,input().split()))
# b=[]
# cnt=0
# for i in range(1,len(a)):
#     if a[i]%2!=0 or a[i]==1:
#         b.append(a[i])
# if len(b)==0:
#     print(0)

#10

# a=list(map(int,input().split()))
# b=int(input())
# a.append(b)
# a.sort()
# print(a.index(b)+1)

#11

# a=list(map(int,input().split()))
# cnt=0
# b=[]
# for i in range(1,len(a)-1):
#     if i not in b:
#         cnt+=1
# print(cnt-1)

#12

# a=list(map(int,input().split()))
# a.reverse()
# print(a)

#13

# a=list(map(int,input().split()))
# a.reverse()
# print(a)

#14

# a=[1,2,3,4,5]
# for i in range(len(a)-1,0,-1):
#     a[i],a[i-1]=a[i-1],a[i]
# print(a)

#17

# a=list(map(int,input().split()))
# b=int(input())
# a.remove(b)
# print(a)

#18

# a=list(map(int,input().split()))
# b=int(input())
# c=int(input())
# a.insert(b,c)
# print(a)