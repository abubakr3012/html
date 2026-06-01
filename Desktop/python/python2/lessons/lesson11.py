# lst=['Hello','World','Abubakr']
# ln=lambda i: len(i)
# m=map(ln,lst)
# print(*list(m))

# lst=[1,2,2,3]
# l=lambda i:i%2!=0
# m=map(l,lst)
# print(list(m))

# lst=[1,2,0,-3]
# l=lambda i: 'positive' if i>0 else('zero' if i==0 else 'negative')
# m=map(l,lst)
# print(list(m))

# lst=['hello','world']
# fun=lambda i: i[::-1]
# m=map(fun,lst)
# print(list(m))

# lst=[i for i in range(1,10) if i%2==0]
# print(lst)

# lst=['hello','Abubakr','Umar']
# fun=[i for i in lst if len(i)>5]
# print(fun)

# lst=['hello',1,12,'world']
# fun=[len(i) if type(i)==str else None for i in lst]
# print(fun)