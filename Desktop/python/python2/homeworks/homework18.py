with open('main.md','r') as file:
    data=file.readlines()
    print(len(data))

cnt=0
with open('main.md','r') as file:
    for i in file:
        cnt+=len(i)
    print(cnt)

with open('main.md','r') as file:
    data=file.read()

with open('hello2.txt','w') as f:
        f.write(data)

lst2=[]
with open('main.md','r') as file:
    lst=file.readlines()

for i in range(1,len(lst),2):
    lst2.append(lst[i].strip())

with open('hello2.txt','w') as file2:
    file2.writelines(lst2)

with open('main.md','r') as file:
    lst=file.readlines()

print(max(lst))

with open('main.md','r') as file:
    data=file.readlines()

data.reverse()
with open('hello2.txt','w') as file:
    file.writelines(data)

with open('main.md','r') as file:
    data=file.readlines()

lst=[]
for i in data:
    if i.strip()!="":
        lst.append(i)

with open('hello2.txt','w') as file2:
    file2.writelines(lst)


with open('main.md','r') as file:
    date=file.readlines()

lst=[]
for i in date:
    i=i.strip()
    if i.isdigit():
        lst.append(int(i))

print(sum(lst))

with open('main.md','r') as file:
    date=file.readlines()

with open('hello2.txt','w') as file:
    for i in range(len(date)):
        l=date[i].strip()
        file.write(f'{i+1} {l}\n')