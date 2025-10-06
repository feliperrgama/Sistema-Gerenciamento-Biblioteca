#Menu principal content

from src.login_page import login
# from src.register_page import ...
from src.loading_animation import loadingAnimation
from os import system

def main_menu():
    system('clear')
    print('===== Welcome to the SGB =====')
    print('< 1 > Login')
    print('< 2 > Cadastro')
    print('< 3 > ')
    opc = int(input('-> [ ]\b\b'))
    return opc

def switch_case(opc):
    match opc:
        case 1:
            #esperando a página de login ser feita
            system('clear')
            print('Message: Indo para a tela de login...')
            loadingAnimation()
            print('Esperando a tela de login ser feita...')
            login()
        case 2:
            #esperando a tela de ergistros ser feita
            system('clear')
            print('Message: Indo para a tela de cadastro...')
            loadingAnimation()
            print('Esperando a tela de Registros ser feita...')
        case _:
            system('clear')
            print('Message: Opção inválida! Tente outra vez...')
            loadingAnimation()
            main_menu()
            opc = 0
    

switch_case(main_menu())
