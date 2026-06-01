arr = list(map(int,input().split()))
i=0
b=int(input())
while i<len(arr):
    if arr[i]==b:
        print(i)
        break
    i+=1

#arr = list(map(int,input().split()))
#i=0
#b=int(input())
#print(arr.index(b))