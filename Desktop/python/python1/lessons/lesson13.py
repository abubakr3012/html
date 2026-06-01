from colorama import Back,Style,Fore
# class Student:
#     def __init__(self,name,grade):
#         self.name=name
#         self.__grade=grade

#     @property
#     def edit(self):
#         return self.__grade
    
#     @edit.setter
#     def ch(self,gr):
#         if gr<=0 or gr>100:
#             print('Error!')
#         else:
#             self.__grade=gr
# name=str(input('Enter your name ==> '))
# grade=int(input('Enter your grade ==> '))
# s=Student(name=name,grade=grade)
# print(s.ch)



# class Student:
#     def __init__(self,name,age,grade):
#         self.__name=name
#         self.__age=age
#         self.__grade=grade
    
#     @property
#     def Name(self):
#         return self.__name
    
#     @property
#     def Age(self):
#         return self.__age
    
#     @property
#     def Grade(self):
#         return self.__grade
    
#     @Name.setter
#     def user_name(self,name):
#         if len(name)==0:
#             return 'Error'
#         else:
#             self.__name=name
    
#     @Age.setter
#     def user_age(self,age):
#         if age<=0 or age>120:
#             return 'Error'
#         else:
#             self.__age=age
    
#     @Grade.setter
#     def user_baho(self,baho):
#         if baho<=0 or baho>100:
#             return 'Error'
#         else:
#             self.__grade=baho

# name=str(input('Enter your name ==> '))
# age=int(input('Enter your age ==> '))
# grade=int(input('Enter your grade ==> '))
# s=Student(name=name,age=age,grade=grade)
# print(f'Your name ==> {s.Name}\nYour age ==> {s.Age}\nYour grade ==> {s.Grade}')


class Createreadupdatedelete:
    def __init__(self):
        self.tasks=[]
    def add_task(self,title,description,dedline):
        task={
            "Title":title,
            "Description":description,
            "Dedline":dedline,
            "Status": False
        }
        self.tasks.append(task)
        print(f"{Style.BRIGHT}{Fore.LIGHTGREEN_EX}Task Added{Style.RESET_ALL}")
    print()
    def read_task(self):
        if len(self.tasks)==0:
            print(f'{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Task is not found!{Style.RESET_ALL}')
            return
        print('-'*30)
        for i,t in enumerate(self.tasks,start=1):
            print(*{t["Title"]} | {t["Description"]} | {t["Title"]})
        print('-'*30)
    def update_task(self):
        if len(self.tasks)==0:
            print(f'{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}No task to update!{Style.RESET_ALL}')
            return
        self.read_task()
        
        i=int(input(f'{Style.BRIGHT}{Fore.CYAN}Enter number of task for updating: {Style.RESET_ALL}'))
        if 1<=i<=len(self.tasks):
            task=self.tasks[i-1]
            tit=input('Enter a new title: ')
            des=input('Enter a new description: ')
            ded=input('Enter a new dedline: ')
            if tit !='':
                task['Title']=tit
            if des !='':
                task['Description']=des
            if ded !='':
                task['Dedline']=ded
            print('Task updated!')
        else:
            print(f'{Style.BRIGHT}{Fore.RED}Error!{Style.RESET_ALL}')
    print()
    def delete_task(self):
        if len(self.tasks)==0:
            print(f'{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}No task to delete!{Style.RESET_ALL}')
            return
        i=int(input('Enter number of task for delete: '))
        ys=['y','yes','Y','YES']
        y=input(f'{Style.BRIGHT}{Fore.LIGHTGREEN_EX}Really you want to delete a task y/n {Style.RESET_ALL}')
        if 1<=i<=len(self.tasks) and y in ys:
            del self.tasks[i-1]
            print('Task Deleted!')
        else:
            print(f'{Style.BRIGHT}{Fore.RED}Error{Style.RESET_ALL}')
    print()
    def main(self):
        while True:
            print(f"""{Style.BRIGHT}{Back.LIGHTBLACK_EX}
{'-'*26} 
| 1.Add a new task        |
| 2.Show all tasks        |
| 3.Update task by number |
| 4.Delete task by number |
| 5.Exit                  |
{'-'*26} {Style.RESET_ALL}""")
            choose=str(input('Choose: '))
            print()
            match choose:
                case '1':
                    title=input('Title: ')
                    description=input('Description: ')
                    dedline=input('Dedline: ')
                    self.add_task(title,description,dedline)
                case '2':
                    self.read_task()
                case '3':
                    self.update_task()
                case '4':
                    self.delete_task()   
                case '5':
                    print(f'{Style.BRIGHT}{Fore.LIGHTYELLOW_EX}Good Bye!{Style.RESET_ALL}')
                    print()
                    return
                case _:
                    print(f'{Style.BRIGHT}{Fore.RED}Error{Style.RESET_ALL}')
x=Createreadupdatedelete()
x.main()     