lst=[]
id=1
while True:
    print(f'''
1.Add new book
2.Filter by author
3.Filter by janre
4.Filter by max and min price
5.Read all books
6.Most expensive book
7.author with most books
8.Oldest book
9.Delete book by id
10.Get book by id
11.Exit
''')

    choose=int(input('Select option --> '))
    if choose==1:
        name=input('Enter name of book --> ')
        author=input('Enter name of author --> ')
        janre=input('Enter janre of book --> ')
        pages=int(input('Enter pages of book --> '))
        price=int(input('Enter price of the book --> '))
        year=int(input('Enter date of book --> '))
        book={
            'id':id,
            'name of book':name,
            'name of author':author,
            'janre of book':janre,
            'pages of book':pages,
            'price of book':price,
            'year':year
        }
        lst.append(book)
        id+=1
        print('New book added!')
    elif choose==2:
        name=input('Enter author name --> ')
        found=False
        for i in lst:
            if 'name of author' in i and i['name of author']==name:
                found=True
                print(f'''
Id --> {i['id']}
Name of book --> {i["name of book"]}
Author --> {i['name of author']}
Janre --> {i['janre of book']}
Pages --> {i['pages of book']}
Price --> {i['price of book']}
Year --> {i['year']}
''')
        if found==False:
            print(f'Author with name {name} is not found')
    elif choose==3:
        name=input('Enter janre name --> ')
        found=False
        for i in lst:
            if 'janre of book' in i and i['janre of book']==name:
                found=True
                print(f'''
Id --> {i['id']}
Name of book --> {i["name of book"]}
Author --> {i['name of author']}
Janre --> {i['janre of book']}
Pages --> {i['pages of book']}
Price --> {i['price of book']}
Year --> {i['year']}
''')
        if found==False:
            print(f'Janre with name {name} is not found')
    elif choose==4:
        mn=int(input('Enter min price --> '))
        mx=int(input('Enter max price --> '))
        found=False
        for i in lst:
            if 'price of book' in i and mn <= i['price of book'] <=mx:
                found=True
                print(f'''
Id of book --> {i['id']}
Name of book --> {i['name of book']}
Name of author --> {i['name of author']}
Janre of book --> {i['janre of book']}
Pages of book --> {i['pages of book']}
Price of book --> {i['price of book']}
Year of book --> {i['year']}
''')
        if found==False:
            print(f'Prices between {mn} and {mx} are not found')
    elif choose==5:
        found=False
        for i in lst:
            print(f'''
Id of book --> {i['id']}
Name of book --> {i['name of book']}
Name of author --> {i['name of author']}
Janre of book --> {i['janre of book']}
Pages of book --> {i['pages of book']}
Price of book --> {i['price of book']}
Year of book --> {i['year']}
''')
            found=True
        if found==False:
            print(f'The list is empty')
    elif choose==6:
        if lst==[]:
            print('List is empty')
        else:
            mx=0
            ex={}
            for i in lst:
                if 'price of book' in i:
                    if i['price of book']>mx:

                        mx=i['price of book']
                        ex=i
            print(f'''
Most expensive book
id of book {ex['id']}
name --> {ex['name of book']}
author --> {ex['name of author']}
price --> {ex['price of book']}
''')
    elif choose==7:
        author_book={}
        for i in lst:
            if 'name of author' in i:
                author=i['name of author']
                if author in author_book:
                    author_book[author]+=1
                else:
                    author_book[author]=1
        mx=0
        best=''
        for j in author_book:
            if author_book[j]>mx:
                mx=author_book[j]
                best=j
        print(f'Author with more books is {best}: {mx} books')   
                     
    elif choose==8:
        if lst==[]:
            print('List is empty')
        else:
            mx=999999
            ex={}
            for i in lst:
                if 'year' in i:
                    if i['year']<mx:
                        mx=i['year']
                        ex=i
            print(f'''
Most oldest book
id of book {ex['id']}
name --> {ex['name of book']}
author --> {ex['name of author']}
price --> {ex['price of book']}
year --> {ex['year']}
''')
    elif choose==9:
        id_del=int(input('Enter id for deleting --> '))
        found=False
        for i in lst:
            if i['id']==id_del:
                lst.remove(i)
                found=True
                print(f'Book with id {id_del} deleted succsessfully!')
        if found==False:
            print(f'Book with id {id_del} is not found!')
    
    elif choose==10:
        id_get=int(input('Enter id for get book --> '))
        found=False
        for i in lst:
            if i['id']==id_get:
                found=True
                print(f'''
    id of book {i['id']}
    name --> {i['name of book']}
    author --> {i['name of author']}
    janre --> {i['janre of book']}
    pages of book --> {i['pages of book']}
    price --> {i['price of book']}
    year --> {i['year']}
''')
        if found==False:
            print('Id is wrong!')
    elif choose==11:
        print('Good Bye')
        break