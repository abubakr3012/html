data=[{}]
id=1
while True:
    print(f'''
1.Add new user
2.Read all users
3.Update user by id
4.Delete user by id
5.Get user by id
6.Exit
''')
    a=int(input('Enter a option --> '))
    match a:
        case '1':
            name=input('Enter name of student --> ')
            age=int(input('Enter age of student --> '))
            gender=input('Enter gender of student --> ')
            dct={
                'id':id,
                'name':name,
                'age':age,
                'gender':gender
            }
            data.append(dct)
            id+=1
            print('New user added succsessfully')
        case '2':
            for i in data:
                print(f'''
                Id --> {id}
                Name --> {name}
                Age --> {age}
                Gender --> {gender}
                ''')
        case '3':
            a=int(input('Enter id for update --> '))
            found=False
            for i in data:
                if i['id']==a:
                    found=True
                    new_name=input('Enter new name of student --> ')
                    new_age=int(input('Enter new age of student --> '))
                    new_gender=input('Enter new gender of student --> ')
                    i['name']=new_name
                    i['age']=new_age
                    i['gender']=new_gender
                    print(f'Product with id {a} updated!')
            if found==False:
                print(f'Product with id {a} not found')
        
        case '4':
            a=int(input('Enter id for delete --> '))
            found=False
            for i in data:
                if i['id']==a:
                    data.remove(i)
                    found=True
                    print(f'Product with id {a} deleted!')
            if found==False:
                print(f'Product with id {a} not found')
        
        case '5':
            pass
