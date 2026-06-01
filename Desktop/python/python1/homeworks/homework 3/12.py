arr = list(map(int,input().split()))
i=0
cnt=0
b=int(input())
while i<len(arr):
    if arr[i]==b: 
        cnt+=1
    i+=1
print(cnt)

#arr=list(map(int, input().split()))
#b=int(input())
#print(arr.count(b))