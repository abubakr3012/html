arr = list(map(int,input().split()))
i=0
mx=-9999
while i<len(arr):
    if mx<arr[i]:
        mx=arr[i]
    i+=1
print(mx)