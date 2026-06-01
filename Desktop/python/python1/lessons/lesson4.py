# a=int(input())
# tpl=[]
# for i in range(a):
#     b=int(input())
#     tpl.append(b)
# for i in tpl:
#     if i%2==0:
#         print(i,end=" ")
# tpl=tuple(map(int, input().split()))
# sum=0
# for i in range(len(tpl)):
#     sum+=tpl[i]
# print(sum)
s=input()
nums='0123456789'
cnt,big,low=0,0,0
for i in range(len(s)):
    if s[i] in nums:
        cnt+=1
for i in range(len(s)):
    
    if s[i]==s.isupper() and s[i] not in nums:
        big+=1
    elif s[i]==s.islower():
        low+=1
print(f"big={big}, low={low}, num={cnt}")