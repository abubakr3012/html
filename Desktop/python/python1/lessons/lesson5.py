# a=int(input())
# name={}
# for i in range(a):
#     k=input()
#     v=int(input())
#     name[k]=v
# for k,v in name.items():
#     print(f"|key ==> {k} | value ==> {v}|")

# st=int(input())
# arr=list(map(int,input().split()))
# mx=-9999
# mn=9999
# j,t = 0,0
# for i in range(st):
#     if arr[i]>mx:
#         mx=arr[i]
#     if arr[i]<mn:
#         mn=arr[i]
#     if arr[i]%2==0:
#         j+=1
#     if arr[i]%2!=0:
#         t+=1
# print("Max =",mx)
# print("Min =",mn)
# print("Juftho =", j)
# print("Toqho =", t)

#4

# st=set(map(str,input().split()))
# nums='0123456789'
# for i in st:
#     if i.isdigit():
#         print(i, end=" ")