# print(int(16**0.5)) # sqrt

# a=int(input())
# b=input()
# c=int(input())
# match b:
#     case '+':
#         print(a+c)
#     case '-':
#         print(a-c)
#     case '*':
#         print(a*c)
#     case '/':
#         print(a//c)
#     case '%':
#         print(a%c)
#     case _:
#         print('Error!')

# a=int(input())
# i=1
# while i<=a:
#     if i%2==0:
#         print(i,end=" ")
#     i+=1
# print()
# j=1
# while j<=a:
#     if j%2!=0:
#         print(j,end=" ")
#     j+=1

# a=int(input())
# b=int(input())
# i=1
# while i<=b:
#     print(a,end=" ")
#     i+=1

# a=int(input())
# i=1
# sm=0
# while i<=a:
#     sm+=i
#     i+=1
# print(sm)

sm=0
while True:
    n=int(input())
    if n==0:
        break
    sm+=n
print(sm)