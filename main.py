from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)'''


def load_key():
    with open('key.key', 'rb') as file:
        key = file.read()
        return key


master_pwd = input('What is the master password ?')
key = load_key() + master_pwd.encode()
fer = Fernet(key)


def add_password():
    user_name = input('User name: ')
    password = input('Password: ')
    with open('Password.txt', 'a') as f:
        f.write(user_name + '  |  ' +
                fer.encrypt(password.encode()).decode() + '\n')


def view_password():
    with open('Password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split('|')
            print('User: ', user, ', Password: ',
                  fer.decrypt(password.encode()).decode())


while True:
    mode = input('Would you like to add a new password(add) or'
                 'view existing one (view) or you want to out '
                 'type (q): ').lower()
    if mode == 'q':
        print('Out')
        quit()
    elif mode == 'add':
        add_password()
    elif mode == 'view':
        view_password()
    else:
        print('Invalid mode')
        continue
