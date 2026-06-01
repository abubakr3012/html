import random
lst=[i for i in range(1,11)]
lst2=random.choices(lst,k=7)
dct={}
for i in lst2:
    dct[i]=lst2.count(i)

for k,v in dct.items():
    print(k,v)