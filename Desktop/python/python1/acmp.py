USERS_WALET = []


class ShowView:
    def shwo_users(self):
        print("*"*30)
        for i in range(len(USERS_WALET)):
            print(USERS_WALET[i])
        print("*"*30)  

    def show_balance(self):
        print("*"*30)
        for i, v in enumerate(USERS_WALET):
            print(i, USERS_WALET[i].get("Full name"))
        print("*"*30)

        index = int(input("Select Cart --> "))
        print(USERS_WALET[index].get("Balance"))
        

class Utils:
    def check_full(self, fio, num):
        cnt1, cnt2 = 0, 0
        for i in range(len(USERS_WALET)):
            if USERS_WALET[i].get("Full name") == fio:
                cnt1+=1
        
        for i in range(len(USERS_WALET)):
            if USERS_WALET[i].get("Wallet Number") == num:
                cnt2 += 1
            
        if cnt1 < 2 and cnt2 == 0:
            return True
        return False   
 
    def check_pasport_info(self, param):
        if param == True:
            return "Confirm request"
        return "Reject request"


class CreateNewUserBankAccount(Utils):
    def __init__(self, pasport_info,  full_name, bank_name, wallet_number):
        self.pasport_info = pasport_info
        self.full_name = full_name
        self.bank_name = bank_name
        self.wallet_number = wallet_number
    
    def add_user(self):
        if self.check_full(self.full_name, self.wallet_number) and self.check_pasport_info(self.pasport_info):
            wallet = {
                "Balance" : 0.0,
                "Full name" : self.full_name,
                "Bank Name" : self.bank_name,
                "Wallet Number" : self.wallet_number,
            }
            USERS_WALET.append(wallet)
            print("Crea Wallet Successfully")
            return

        return "Reject request"



def main():
    while True:
        balance = ShowView()

        print('*'*20)
        print('''
            1. Open New Wallet
            2. Transaction
            3. View Balance
            4. Exit
        ''')
        print('*'*20)
        
        chose = input("Select your options --> ")
        match chose:
            case '1':
                pasport = input("Have you pasport (yes/no) --> ").lower()
                pasport = True if pasport == "yes" else False
                object = CreateNewUserBankAccount(
                pasport,
                input("Enter full name --> "),
                input("Enter your favourite bank --> "),
                input("Enter walet number --> ")
            )
                print(object.add_user())

            case '2':
                print("*" * 30)
                for i, v in enumerate(USERS_WALET):
                    print(i, v.get("Full name"))
                print("*" * 30)

                if len(USERS_WALET) == 0:
                    print("No wallets found")
                    continue

                index = int(input("Select Wallet --> "))

                if index < 0 or index >= len(USERS_WALET):
                    print("Invalid index")
                    continue

                print("""
1. Deposit
2. Withdraw
""")

                action = input("Choose --> ")

                amount = float(input("Enter amount --> "))

                if amount <= 0:
                    print("Invalid amount")
                    continue

                if action == '1':
                    USERS_WALET[index]["Balance"] += amount
                    print("Deposit successful")

                elif action == '2':
                    if USERS_WALET[index]["Balance"] >= amount:
                        USERS_WALET[index]["Balance"] -= amount
                        print("Withdraw successful")
                    else:
                        print("Not enough balance")

                else:
                    print("Invalid option")

            case '3':
                balance.show_balance()

            case '4':
                print('Good bye')
                break

def show_balance(self):
    for i, v in enumerate(USERS_WALET):
        print(f"{i} -> {v['Full name']}")

    index = int(input("Select Wallet --> "))
    
    print("*"*30)
    print("Full Name:", USERS_WALET[index]["Full name"])
    print("Bank Name:", USERS_WALET[index]["Bank Name"])
    print("Balance:", USERS_WALET[index]["Balance"])
    print("*"*30)