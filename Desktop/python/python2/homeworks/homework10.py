lst=[]
id=1
mx=0
best=''
def add_new_book(name,author,janre,pages,price,year):
    global lst,id
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
    print(f'new book added')
def filter_by_author(name_of_author):
    found=False
    for i in lst:
        if 'name of author' in i and i['name of author']==name_of_author:
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
        print(f'Author with name {name_of_author} is not found')
def filter_by_janre(name_of_janre):
    found=False
    for i in lst:
        if 'janre of book' in i and i['janre of book']==name_of_janre:
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
        print(f'{name_of_janre} janre is not found')
def filter_by_min_max(mn,mx):
    found=False
    for i in lst:
        if "price of book" in i and mn<=i["price of book"]<mx:
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
def read_all_books():
    found=False
    for i in lst:
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
        print(f'The list is empty')
def expersive_book():
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
        
def author_most_books():
    global mx,best
    author_book={}
    for i in lst:
        if 'name of author' in i:
            author=i['name of author']
            if author in author_book:
                author_book[author]+=1
            else:
                author_book[author]=1
    for j in author_book:
        if author_book[j]>mx:
            mx=author_book[j]
            best=j
    print(f'Author with more books is {best}: {mx} books')

def ave_price_pages():
    if lst==[]:
        print('List is empty')
    else:
        sm_price=0
        sm_pages=0
        cnt=0
        for i in lst:
            sm_price+=i['price of book']
            sm_pages+=i['pages of book']
            cnt+=1
        print(f'''
Avereage of pages is {sm_pages/cnt})
Avereage of price is {sm_price/cnt}''')
def delete_by_id(a):
    found=False
    if lst==[]:
        print('List is empty')
    else:
        for i in lst:
            if i['id']==a:
                lst.remove(i)
                found=True
                print(f'Book with id {a} deleted')
        if found==False:
            print(f'Book with id {a} is not found')
def get_by_id(a):
    found=False
    if lst==[]:
        print('List is empty')
    else:
        for i in lst:
            if i['id']==a:
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
            print(f'Book with id {a} is not found')
def exit():
    print('Good Bye!')

while True:
    print(f'''
************************************
* 1. Add new book                  *
* 2. Filter by author              *
* 3. Filter by janre               *
* 4. Filter by max and min price   *
* 5. Read all books                *
* 6. Most expensive book           *
* 7. author with most books        *
* 8. avarage price + avarage pages *
* 9. Delete book by id             *
* 10.Get book by id                *   
* 11.Exit                          *
************************************
''')
    choose=int(input('Select option --> '))
    if choose==1:
        name=input('Enter name of book --> ')
        author=input('Enter name of author --> ')
        janre=input('Enter janre of book --> ')
        pages=int(input('Enter pages of book --> '))
        price=int(input('Enter price of the book --> '))
        year=int(input('Enter year of book --> '))
        add_new_book(name,author,janre,pages,price,year)
    elif choose==2:
        name=input('Enter author name --> ')
        filter_by_author(name)
    elif choose==3:
        name=input('Enter janre name --> ')
        filter_by_janre(name)
    elif choose==4:
        mn=int(input('Enter min price --> '))
        mx=int(input('Enter max price --> '))
        filter_by_min_max(mn,mx)
    elif choose==5:
        read_all_books()
    elif choose==6:
        expersive_book()
    elif choose==7:
        author_most_books()
    elif choose==8:
        ave_price_pages()
    elif choose==9:
        a=int(input('Enter id for deleting --> '))
        delete_by_id(a)
    elif choose==10:
        a=int(input('Enter id for get book --> '))
        get_by_id(a)
    elif choose==11:
        exit()
        break    