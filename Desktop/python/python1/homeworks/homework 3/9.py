arr = list(map(int,input().split()))
i=0
while i<len(arr):
    arr.sort(reverse=True)
    i+=1
print(arr)