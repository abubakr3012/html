arr = list(map(int,input().split()))
i=0
cnt=0
while i<len(arr):
    cnt+=arr[i]
    i+=1
print(cnt)