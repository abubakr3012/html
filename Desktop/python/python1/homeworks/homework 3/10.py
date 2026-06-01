arr = list(map(int,input().split()))
i=0
while i<len(arr):
    arr.pop(0)
    i+=1
print(arr)