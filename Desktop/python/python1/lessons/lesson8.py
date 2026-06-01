# a=list(map(str,input().split()))
# num='1234567890'
# lam=lambda lst: [i for i in lst if i not in num]
# b=set(lam(a))    
# print(*b)



# def fibonachi(n):
#     if n<=1:
#         return n
#     return fibonachi(n-1)+fibonachi(n-2)
# a=int(input())
# print(fibonachi(a))
# 1+1=2
# 2+1=3
# 2+3=5
# 5+3=8
# 8+5=13
# 13+8=21
# 21+13=34
def palindrome(n):
    if license(n,list):
        n="".join(map(str,n))
    if license(n,int):
        n=str(n)
    if len(n)<=1:
        return True
    if n[0]!=n[-1]:
        return False
    return palindrome(n[1:-1])
a=[111]
print(palindrome(a))