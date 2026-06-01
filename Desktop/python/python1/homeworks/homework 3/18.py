arr=list(map(int ,input().split()))
i=0
while i<len(arr):
    if arr[i]==0:
        break
    i+=1
print(arr[:i])