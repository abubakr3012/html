arr = list(map(int,input().split()))
i=0
mn=9999
while i<len(arr):
    if mn>arr[i]:
        mn=arr[i]
    i+=1
print(mn)