from colorama import Fore, Style, Back


# Create Read Update Delet
USERS_INFO = []


def add_new_user():
    new = dict()
    print(f'{Style.BRIGHT}')
    phone = input(f'{Fore.LIGHTYELLOW_EX} Enter Phone number --> ')
    fio = input(f'{Fore.LIGHTCYAN_EX} Enter full name --> ')
    print(f"{Style.RESET_ALL}")

    for i in USERS_INFO:
        if phone in i :
            print(f"\n{Style.BRIGHT}{Back.YELLOW}{Fore.RED} This number already exists!  ")
            print(Style.RESET_ALL)
            return
        
    new[phone] = fio
    USERS_INFO.append(new)
    print(f"\n{Style.BRIGHT}{Back.GREEN}{Fore.WHITE} Add new user successfully!  ")
    print(Style.RESET_ALL)


def read_user_by_id():
    phone = input(f'\n{Fore.LIGHTYELLOW_EX} Enter Phone number --> ')
    for i in USERS_INFO:    
        if phone in i:
            print(f"\n{Style.BRIGHT}{Back.GREEN}{Fore.BLACK}Phone --> {str(list(i.keys())[0])} \n  Name --> {str(list(i.values())[0])}")
            print(Style.RESET_ALL)
            return
    print(f"\n{Style.BRIGHT}{Back.YELLOW}{Fore.RED} This number not found!  ")
    print(Style.RESET_ALL)
    return
        
def get_all_user():
    if len(USERS_INFO) == 0:
        print(f"\n{Style.BRIGHT}{Back.YELLOW}{Fore.RED} USERS NOT FOUND!  ")
        print(Style.RESET_ALL) 
    else:
        for i in USERS_INFO:
            print(f"\n{Style.BRIGHT}{Back.GREEN}{Fore.BLACK}Phone --> {str(list(i.keys())[0])} \n  Name --> {str(list(i.values())[0])}")
    print(Style.RESET_ALL) 

def update_by_id():
    pass

def delet_by_id():
    pass

def delet_all():
    pass

def exit():
    print()
    print(f"{Fore.WHITE}{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}Good bye 👋🏻 {Style.RESET_ALL}") 


def main():
    while True:
        print(f'''{Fore.WHITE}{Style.BRIGHT}{Back.LIGHTBLACK_EX}
------------------------------
|        CRUD MENU           |
|1. Add New user.            |
|2. Get by id                |
|3. Get all users            |
|8. Exit.                    |
------------------------------
{Style.RESET_ALL}''')
    

        choose = input(f'{Fore.LIGHTCYAN_EX} Select options --> ')
        match choose:
            case "1":
                add_new_user()
            case "2":
                read_user_by_id()
            case "3":
                get_all_user()
            case "8":
                exit()
                return
            case _:
                print(f"\n{Fore.RED}{Style.BRIGHT}{Back.YELLOW}Error options {Style.RESET_ALL}")

main()
