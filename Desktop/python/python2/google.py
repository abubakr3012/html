import random

current_user = None


def register(login, email, password):
    try:
        with open('users.txt', 'r') as users:
            us = users.readlines()
    except FileNotFoundError:
        us = []

    for user in us:
        user = user.strip().split(':')
        if login == user[0] or email == user[1]:
            print('this user already registered')
            return

    pass2 = input('enter your password one more time --> ')
    if pass2 != password:
        print('your passwords are not same')
        return

    with open('users.txt', 'a') as users:
        users.write(f'{login}:{email}:{password}\n')


def reset_password(email):
    try:
        with open('users.txt', 'r') as users:
            us = users.readlines()
    except FileNotFoundError:
        print('file not found')
        return

    found = False
    new_data = []

    for user in us:
        login, em, password = user.strip().split(':')

        if em == email:
            found = True

            code = random.randint(1000, 9999)
            print(f'Your code: {code}')  # имитация email

            user_code = int(input('enter code --> '))
            if user_code != code:
                print('wrong code')
                return

            new_pass = input('new password --> ')
            new_pass2 = input('repeat password --> ')

            if new_pass != new_pass2:
                print('passwords not same')
                return

            password = new_pass
            print('password changed')

        new_data.append(f'{login}:{em}:{password}\n')

    if not found:
        print('email not found')
        return

    with open('users.txt', 'w') as file:
        file.writelines(new_data)


def login(username, password):
    global current_user

    try:
        with open('users.txt', 'r') as file:
            us = file.readlines()
    except FileNotFoundError:
        print('no users')
        return

    for user in us:
        login, email, pas = user.strip().split(':')

        if login == username and pas == password:
            print(f'Welcome {username}')
            current_user = login
            return

    print('Invalid login or password')


while True:
    if not current_user:
        n = int(input('''
1 --> register
2 --> forget password
3 --> login
'''))

        if n == 1:
            register(input('username: '),
                     input('email: '),
                     input('password: '))

        elif n == 2:
            reset_password(input('email: '))

        elif n == 3:
            login(input("username: "),
                  input("password: "))

    else:
        print(f'You are logged in as {current_user}')
        break