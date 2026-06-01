from colorama import Back,Style,Fore
PRODUCTS = {
    1 : {"Milk" : 10},
    2 : {"Bread" : 5},
    3 : {"ChocoPie" : 12},
    4 : {"RC" : 13},
    5 : {"FuseTea" : 6}
}

BOX = [{"RC" : 13},{"FuseTea" : 6}]
SUM = 0
SUM_LIST = []


def show_products():
    print('\n---------------------------------')
    print('| № |    Name  |     Price      |')
    print('|___|__________|________________|')

    for k, v in PRODUCTS.items():
        for i, j in v.items():
            print(f"|{k : > 2} | {i:>8} | {j :> 7} сомонӣ!|")
    print('|___|__________|________________|')


def buy_product(number):
    product_number = list(PRODUCTS.keys())
    if number not in product_number:
        print("\nThis Product not found!\n")
        return
    
    BOX.append(PRODUCTS.get(number))
    print("\nOrder Confirm!\n")


def confirmation_order(conf):
    if conf.lower() in ['y', 'yes', 'ok']:
        global SUM, SUM_LIST
        SUM = 0
        for i in BOX:
            SUM_LIST  = list(i.items())
            SUM += int(SUM_LIST[0][1])
            SUM_LIST.clear()
        return SUM 
    else:
        BOX.clear()
        return "Order cancel!"


def show_box():
    LST = []
    for i in BOX:
        LST += list(i.items())
        print(f'Product {LST[0][0]}   price {LST[0][1]}')
        LST.clear()

def rem_box(name):
    for i in BOX:
        if name in i:
            BOX.remove(i)
            print(f"{Style.BRIGHT}{Fore.GREEN}Product added !{Style.RESET_ALL}")
            return
        print(f"{Style.BRIGHT}{Fore.RED}Product is not found !{Style.RESET_ALL}")


def cls_box():
    BOX.clear()
    print(f"{Style.BRIGHT}{Fore.GREEN} Products are removed! {Style.RESET_ALL}")

def summ():
    cnt=0
    for i in BOX:
        cnt+=list(i.values())[0]
        print(f"{Style.BRIGHT}You must pay ==> {cnt}{Style.RESET_ALL}")

def exit():
    print(f"{Style.BRIGHT}GOOD BYE!{Style.RESET_ALL}")
    return
def main():
    while True:
        print(
"""
______________________________
|           CRUD MENU        |
|1.SHOW PRODUCTS             |
|2.BUY PRODUCT FROM LIST     |
|3.SHOW BOX                  |
|4.REMOVE FROM BOX           |
|5.ClEAR BOX                 |
|6.SHOW ALL SUM              |
|7.CONFIRM ORDER             |
|8.EXIT                      |
------------------------------
""")
        x=input('Enter a number ==> ')
        match x:
            case '1':
                show_products()
            case '2':
                buy_product()
            case '3':
                show_box()
            case '4':
                rem_box()
            case '5':
                cls_box()
            case '6':
                summ()
            case '7':
                confirmation_order()
            case '8':
                exit()
                return
            case _:
                print(f"{Style.BRIGHT}{Fore.RED} ERROR! {Style.RESET_ALL}")
                exit()
                return
main()