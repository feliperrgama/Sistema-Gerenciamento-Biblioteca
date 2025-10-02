def register():
    print('Who are you?')
    print('< 1 > The administrator')
    print('< 2 > A Student')
    print('< 3 > A teacher')
    option = int(input('-> '))

    if option == 1:
        name_admin = input('Your name: ')
        email_admin = input('Your best email: ')
        cpf_admin = input('CPF: ') #Put a regex here to take the cpf from admin

        admin = {
            "_name": name_admin,
            "email": email_admin,
            "cpf":  
        }

