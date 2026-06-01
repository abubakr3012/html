from colorama import Fore, Style, Back
user_info = []
def add_new_user():
    new=dict()
    print(f'{Style.BRIGHT}')
    phone=input(f'{Fore.LIGHTYELLOW_EX} Enter your phone  or email ==> ')
    fio=input(f'{Fore.LIGHTMAGENTA_EX} Enter username ==> ')
    print(f'{Style.RESET_ALL}') 

    for i in user_info:
        if phone in i:
            print(f"\n{Style.BRIGHT}{Back.YELLOW}{Fore.RED} This number or email is already exists! ")
            print(Style.RESET_ALL)
            return
    
    new[phone] = fio
    user_info.append(new)
    print(f"\n{Style.BRIGHT}{Back.GREEN}{Fore.WHITE} A new user added succsessfully ")
    print(Style.RESET_ALL)

def read_user_by_id():
    phone=input(f"\n {Fore.LIGHTYELLOW_EX} Enter a phone or email ==> ")
    for i in user_info:
        if phone in i:
            print(f"\n{Style.BRIGHT}{Back.GREEN}{Fore.BLACK} Phone ==> {str(list(i.keys())[0])} \n Name ==> {str(list(i.values())[0])}")
            return
    print(f"\n{Style.BRIGHT}{Back.YELLOW}{Fore.RED} THIS NUMBER  OR EMAIL ISN'T FOUND! ")
    print(Style.RESET_ALL)
    return

def read_user_by_name():
    fio=input(f"\n {Fore.LIGHTYELLOW_EX} Enter a username ==> ")
    for i in user_info:
        phone=list(i.keys())[0]
        name=list(i.values())[0]
        if name in fio:
            print(f"\n{Style.BRIGHT}{Back.GREEN}{Fore.BLACK} Phone ==> {str(list(i.keys())[0])} \n Username ==> {str(list(i.values())[0])}")
            return
    print(f"\n{Style.BRIGHT}{Back.YELLOW}{Fore.RED} THIS USERNAME ISN'T FOUND! ")
    print(Style.RESET_ALL)
    return

def get_all_user():
    if len(user_info)==0:
        print(f"\n{Style.BRIGHT}{Back.BLACK}{Fore.RED} USERS ISN'T FOUND! ")
        print(Style.RESET_ALL)
    else:
        for i in user_info:
            print(f"\n{Style.BRIGHT}{Back.GREEN}{Fore.BLACK} |Phone : {str(list(i.keys())[0])}| \n |Name : {str(list(i.values())[0])}|")
    print(Style.RESET_ALL)
    print()

def update_user_by_name():
    fio=input(f'{Fore.LIGHTMAGENTA_EX} Enter name ==> ')
    
    for i in user_info:
        phone = list(i.keys())[0]
        name = list(i.values())[0]
        if name == fio:
            print(f"\n {Style.BRIGHT}{Back.LIGHTBLUE_EX}{Fore.BLACK} Enter a new username ==> ")
            new_name=input()
            i[phone]=new_name
            print(f"{Style.RESET_ALL} Username updated succsessfully! ")
            return
    print(f"{Fore.RED}User isn't found!")
    print(Style.RESET_ALL)

def update_user_by_id():
    phone=input(f"{Fore.LIGHTCYAN_EX} Enter a number or email ==> ")

    for i in user_info:
        phne = list(i.keys())[0]
        name = list(i.values())[0]
        if phne == phone:
            print(f"\n{Style.BRIGHT}{Back.LIGHTGREEN_EX}{Fore.BLACK} Enter a new number or email ==> ")
            new_phone=input()
            del i[phne]
            i[new_phone]=name
            print(f"{Style.RESET_ALL} Phone number or email updated succsessfully! ")
            return
    print(f"{Fore.RED} Number or email isn't found!")
    print(Style.RESET_ALL)
    
def update_all():
    fio=input(f'{Fore.LIGHTMAGENTA_EX} Enter username ==> ')
    phone=input(f"{Fore.LIGHTCYAN_EX} Enter a number or email ==> ")

    for i in user_info:
        phone = list(i.keys())[0]
        name = list(i.values())[0]
        if name == fio:
            print(f"\n {Style.BRIGHT}{Back.LIGHTBLUE_EX}{Fore.BLACK} Enter a new username ==> ")
            new_name=input()
            i[phone]=new_name
    for i in user_info:
        phne = list(i.keys())[0]
        name = list(i.values())[0]
        if phne == phone:
            print(f"\n{Style.BRIGHT}{Back.LIGHTBLUE_EX}{Fore.BLACK} Enter a new number or email ==> ")
            new_phone=input()
            del i[phne]
            i[new_phone]=name
            print(f"{Back.LIGHTBLUE_EX}{Style.RESET_ALL} Informations are updated succsessfully! ")
            return
    print(f"{Fore.RED}{Style.BRIGHT} Error!")
    print(Style.RESET_ALL)
def delete_user_by_name():
    fio=input(f"{Fore.CYAN} Enter a username ==> ")
    for i in user_info:
        name=list(i.values())[0]
        if name==fio:
            user_info.remove(i)
            print(f"{Style.BRIGHT}{Back.GREEN}{Fore.BLACK} User deleted successfully!")
            print(Style.RESET_ALL)
            return

    print(f"{Fore.RED}User isn't found!")

def delete_user_by_id():
    phne=input(f"{Fore.LIGHTRED_EX} Enter a phone number or email ==> ")
    for i in user_info:
        phone=list(i.keys())[0]
        if phone==phne:
            user_info.remove(i)
            print(f"{Style.BRIGHT}{Back.GREEN}{Fore.BLACK} User deleted successfully!")
            print(Style.RESET_ALL)
            return
    print(f"{Fore.RED}User isn't found!")

def clear_users():
    num=input(f"{Fore.LIGHTGREEN_EX} Do you want to delete all of users? Enter y/n ")
    for i in user_info:
        if num=='y' or num=='Y' or num=='yes' or 'YES':
            user_info.clear()
            print(f"{Style.BRIGHT}{Back.GREEN}{Fore.BLACK} Users are deleted successfully!")
            print(Style.RESET_ALL)
            return
    print(f"{Fore.RED}{Style.BRIGHT}Users isn't found!")

def exit():
    print()
    print(f"{Fore.WHITE}{Style.BRIGHT}{Fore.RED}Good bye 👋🏻 {Style.RESET_ALL}") 


def main():
    while True:
        print(f'''{Fore.WHITE}{Style.BRIGHT}{Back.LIGHTBLACK_EX}
------------------------------
|        CRUD MENU           |
|1. Add New user.            |
|2. Get by id                |
|3. Get by username          |
|4. Get all users            |
|5. Update user by name      |
|6. Update user by phone     |
|7. Update all informations  |
|8. Delete user by name      |
|9. Delete user by phone     |
|10. Clear all users         |
|11. Exit                    |
------------------------------
{Style.RESET_ALL}''')
    
        choose = input(f'{Fore.LIGHTCYAN_EX} Select options ==> ')
        match choose:
            case "1":
                add_new_user()
            case "2":
                read_user_by_id()
            case "3":
                read_user_by_name()
            case "4":
                get_all_user()
            case "5":
                update_user_by_name()
            case "6":
                update_user_by_id()
            case "7":
                update_all()
            case "8":
                delete_user_by_name()
            case "9":
                delete_user_by_id()
            case "10":
                clear_users()
            case "11":
                exit()
                return
            case _:
                print(f"\n{Fore.RED}{Style.BRIGHT}{Back.YELLOW}Error options {Style.RESET_ALL}")

main()