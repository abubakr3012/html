import random

class Accaunt:
    def __init__(self) -> None:
        self.current_user=None
    
    def register(self,login,email,password):
        open('users.txt','a').close()

        with open('users.txt','r') as users:
            us=users.readlines()
        
        for user in us:
            user=user.strip().split(":")
            if login==user[0] or email==user[1]:
                print('this user already taken')
                return
            
        pass2=input('enter your passsword -> ')
        if pass2!=password:
            print('Passwords are not same')
            return

        with open('users.txt','a') as users:
            users.write(f'{login}:{email}:{password}\n')
    
    def login(self,username,password):
        with open('users.txt','r') as file:
            us=file.readlines()
        
        for user in us:
            user=user.strip().split(':')
            if user[0]==username and user[2]==password:
                print(f'Welcome {username}')
                self.current_user=user[0]
                return

        print('Invalid login or passwors')

    def reset_password(self,email):
        with open('users.txt','r') as file:
            us=file.readlines()

        found=False
        new_data=[]

        for user in us:
            user=user.strip().split(':')

            if user[1]==email:
                found=True
                code=random.randint(100000,999999)
                with open('random.txt','w') as file:
                    file.write(str(code))

                user_code=int(input('Enter code -> '))
                if user_code!=code:
                    print('Wrong code')
                    return

                new_pass=input('Enter new password -> ')
                new_pass2=input('Repeat password -> ')

                if new_pass!=new_pass2:
                    print('password are not same')
                    return

                user[2]=new_pass
                print('password changed')

            new_data.append(f'{user[0]}:{user[1]}:{user[2]}\n')

        if not found:
            print('email not found')
            return

        with open('users.txt','w') as file:
            file.writelines(new_data)

    def get_info(self,email,password):
        with open('users.txt','r') as file:
            us=file.readlines()
        
        for user in us:
            user=user.strip().split(':')
            if user[1]==email and user[2]==password:
                dct={
                    'login':user[0],
                    'email':user[1],
                    'password':user[2]
                }
                print(dct)
                return

        print('user not found')
    
    def update_info(self):
        with open('users.txt','r') as file:
            us=file.readlines()

        n=int(input('''
Which info you want update
1 Login
2 Email
3 Exit
Your choise -> '''))

        if n==3:
            return

        new_data=[]
        found=False

        if n==1:
            old_username=input('Enter your name -> ')
            new_username=input('Enter new login -> ')
        elif n==2:
            old_email=input('Enter your email -> ')
            new_email=input('Enter new email -> ')

        for user in us:
            user=user.strip().split(':')

            if n==1:
                if user[0]==old_username:
                    user[0]=new_username
                    found=True
            elif n==2:
                if user[1]==old_email:
                    user[1]=new_email
                    found=True

            new_data.append(f'{user[0]}:{user[1]}:{user[2]}\n')

        if not found:
            print('User not found')
            return

        with open('users.txt','w') as file:
            file.writelines(new_data)

    def delete_info(self,email,password):
        with open('users.txt','r') as file:
            us=file.readlines()

        new_data=[]
        found=False

        for user in us:
            user=user.strip().split(':')

            if user[1]==email and user[2]==password:
                found=True
                continue

            new_data.append(f'{user[0]}:{user[1]}:{user[2]}\n')

        if found:
            with open('users.txt','w') as file:
                file.writelines(new_data)
        else:
            print('user not found')


user=Accaunt()

while True:
    n=int(input('''
1 Register
2 Login
3 Reset password
4 get info 
5 update info
6 delete info
7 exit
Your choise -> '''))

    if n==1:
        login=input('Enter your login -> ')
        email=input('Enter your email -> ')
        password=input('Enter your password -> ')
        user.register(login,email,password)

    elif n==2:
        login=input('Enter your login -> ')
        pas=input('Enter your password -> ')
        user.login(login,pas)

    elif n==3:
        ema=input('Enter your email -> ')
        user.reset_password(ema)

    elif n==4:
        get_user=input('Enter your email -> ')
        get_pass=input('Enter your password -> ')
        user.get_info(get_user,get_pass)

    elif n==5:
        user.update_info()
    
    elif n==6:
        delete_user=input('Enter your email -> ')
        delete_pass=input('Enter your password -> ')
        user.delete_info(delete_user,delete_pass)
    
    elif n==7:
        print('Good Bye')
        break