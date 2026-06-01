class Crud:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''

    def add_new_user(self):
        with open("my_file.txt", 'a', encoding='utf-8') as file:
            fname, lname = self.first_name, self.last_name
            a = file.write(f"\n{fname} {lname}\n")
            print("User added success!")
    
    def read_all_fiel(self):
        print('\n')
        with open("my_file.txt", 'r', encoding='utf-8') as file:
            print(file.read())
        print('\n')  

    def read_by_index(self):
        a = int(input("Enter index --> "))
        with open("my_file.txt", 'r', encoding='utf-8') as file:   
            lst = file.readlines()

            for i, v in enumerate(lst):
                if a == i+1:
                    print(v)
                    return
            print("Info not found")

    def change_by_index(self):
        a = int(input("Enter index --> "))
        with open("my_file.txt", 'r', encoding='utf-8') as file:   
            lst = file.readlines()
            lst[a-1] = input("Enter f name and l name --> ") + "\n"

        self.delet_all()
        with open("my_file.txt", 'a', encoding='utf-8') as file:
            for i in lst:
                file.write(i)
    def change_by_name(self):
        a=input('Enter name --> ')
        with open("my_file.txt", 'r', encoding='utf-8') as file:
            lst=file.readlines()
        
        for i in range(len(lst)):
            if lst[i].startswith(a+' '):
                lst[i]=input('Enter a new name --> ')+'\n'
                break
        else:
            print('User is not found!')
            return
        open('my_file.txt','w',encoding='utf-8').writelines(lst)
        print('Changed succsessfully!')

    def delet_by_index(self):
        a = int(input("Enter index --> "))
        with open("my_file.txt", 'r', encoding='utf-8') as file:   
            lst = file.readlines()
            lst.pop(a-1)

        self.delet_all()
        with open("my_file.txt", 'a', encoding='utf-8') as file:
            for i in lst:
                file.write(i)

    def delete_by_name(self):
        name=input('Enter name --> ')
        with open('my_file.txt','r',encoding='utf-8') as file:
            lst=file.readlines()

        new_list=[i for i in lst if not i.startswith(name+' ')]

        if len (lst)==len(new_list):
            print('User is not found!')
            return
        
        open('my_file.txt','w',encoding='utf-8').writelines(new_list)
        print('Deleted succsessfully!')
        

    def delet_all(self):
        open("my_file.txt", 'w').close()
        print("Clear successfull")


a = Crud()

a.change_by_index()

while True:
    print('*'*27)
    print('''
1.Add new user!           *
2.Read all files          *
3.Read by index           *
4.Chanhe by index         *
5.Change by name          *
6.Delete by index         *
7.Delete by name          *
8.Delete all information  *
9.Exit                    *
''')
    print('*'*27)
    choise=input('Select your option --> ')
    match choise:
        case '1':
            a.first_name=input('Enter first name --> ')
            a.add_new_user()
        case '2':
            a.read_all_fiel()
        case '3':
            a.read_by_index()
        case '4':
            a.change_by_index()
        case '5':
            a.change_by_name()
        case '6':
            a.delet_by_index()
        case '7':
            a.delete_by_name()
        case '8':
            a.delet_all()
        case '9':
            print('Good bye')
            break
        case _:
            print('Error')