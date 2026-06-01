arr=list(map(int,input().split()))
i=0
pw=[]
while i<len(arr):
    pw.append(arr[i]**2)
    i+=1
print(pw)