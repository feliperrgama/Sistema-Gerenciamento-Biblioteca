#Menu principal content

from src.login_page import login
# from src.register_page import ...

def main_menu():
    print('===== Welcome to the SGB =====')
    print('< 1 > Login')
    print('< 2 > Cadastro')
    print('< 3 > doidura')
    opc = int(input('-> [ ]\b\b'))
    return opc

def switch_case(opc):
    match opc:
        case 1:
            #esperando a página de login ser feita
            print('Esperando a tela de login ser feita...')
            login()
        case 2:
            #esperando a tela de ergistros ser feita
            print('Esperando a tela de Registros ser feita...')
        case _:
            main_menu()
            opc = 0
    

switch_case(main_menu())
