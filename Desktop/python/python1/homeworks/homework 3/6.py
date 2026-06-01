arr = list(map(int,input().split()))
i=0
cnt=0
while i<len(arr):
    if arr[i]%2==0 and arr[i]!=0:
        cnt+=1
    i+=1
print(cnt)