#1 lst=[1,2,3,4]
# fun=[i*2 if i%2==0 else i*i for i in lst]
# print(fun)

#2 lst1=[2,5,7]
# lst2=[3,6,2]
# fun=list(map(lambda a,b: a+b if a+b>10 else a*b,lst1,lst2))
# print(fun)

#3 lst=["hi","python","cat"]
# fun=[i.upper() if len(i)>3 else i for i in lst]
# print(fun)

#4 lst=[1,None,3,None]
# fun=[i**2 if i is not None else 0 for i in lst]
# print(fun)

#5 lst=["hi","python","cat"]
# fun=[i[-1] if len(i)>4 else i[0] for i in lst]
# print(fun)

#6 lst=[-2,3,0,4]
# fun=[i**3 for i in lst if i>0]
# print(fun)

#7 lst=[[1,2],[3,4]]
# fun=[sum(j**2 for j in i) for i in lst]
# print(fun)

#10 lst=[-1,0,2,3]
# fun=lambda i: ('A' if i%2==0 and i>0
# else 'B' if i>0 and i%2!=0
# else 'C' if i<0
# else 'D')
# m=map(fun,lst)
# print(list(m))