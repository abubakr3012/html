import random
from datetime import datetime

ln=int(input('How manu student you want to add --> '))
print()

students=[]

for i in range(ln):
    name=input(f'Enter name of student {i+1} --> ')
    grades=list(map(int,input(f'Enter a grades of student {name} --> ').split()))
    now=datetime.now()
    students.append({
        'name':name,
        'grades':grades,
        'added_date':now.strftime('%Y/%m/%d'),
        'added_time':now.strftime('%H:%M')
    })
while students:
    print('Selection starting\n')
    mn_ave=sum(students[0]['grades'])/len(students[0]['grades'])
    lw_grp=[
        i for i in students
        if sum(i['grades'])/len(i['grades'])==mn_ave
    ]
    std=random.choice(lw_grp)
    selected_time=datetime.now()
    print(f"\nSelected student: {std['name']}")
    print(f'Average grades: {mn_ave}')
    print(f'Added date: {std['added_date']}')
    print(f'Added time: {std['added_time']}')
    print(f'Selected at: {selected_time.strftime('%Y/%m/%d %H:%M')}')

    students.remove(std)
    
    print()
    input('Press Enter to continue...\n')

print('All students have been selected')
print()