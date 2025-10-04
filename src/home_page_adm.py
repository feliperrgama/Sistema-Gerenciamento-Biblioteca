from os import system
from linha_function import linha
from loading_animation import loadingAnimation
from mysql.connector import connect, Error
import time
import re
from tabulate import tabulate


def adm_home_page():
    system('clear')
    print('===== HOME PAGE ADM =====')
    linha(50, '-')
    print('< 1 > Responder Solicitações')
    print('< 2 > Adicionar livros ao sistema')
    print('< 3 > Remover livros do sistema')
    print('< 4 > Ver lista de livros cadastrados no sistema')
    print('< 5 > Ver lista de livros disponíveis')
    opc = int(input('-> [ ]\b\b'))
    loadingAnimation()
    return  opc


def switch_case(opc):
    match opc:
        case 1:
            print('Do the dev here')
        case 2:
            addBook()
        case 3:
            removeBook()
        case 4:
            seeBooksInSistem()
        case 5:
            showBooks1()
        case _:
            print('Opção inválida!\nTente outra vez...')
            loadingAnimation()
            switch_case(adm_home_page())
    pass


def opc_more_book(string):
    string_copy = string

    system('clear')
    print(f'Deseja {string} mais um livro?')
    print('< 1 > Sim')
    print('< 2 > Não')
    opc = int(input('-> [ ]\b\b'))

    if opc == 1:
        loadingAnimation()
        if string == 'adicionar':
            addBook()
        elif string == 'remover':
            removeBook()
    elif opc == 2:
        system('clear')
        print('Message: Voltando para a home page...')
        time.sleep(2)
        loadingAnimation()
        switch_case(adm_home_page())
    else:
        print('Opção inválida, tente novamente...')
        loadingAnimation()
        opc_more_book(string_copy)



# RESPONDER SOLICITAÇÕES ================================



# RESPONDER SOLICITAÇÕES ================================

# ADICIONAR LIVROS ====================================
def addBook():
    system('clear')

    padrao_re = r'^\d{4}$'

    print('===== ADICIONAR LIVROS AO SISTEMA =====')
    linha(50, '-')
    title = input('Título do livro: ')
    autor = input('Autor: ')
    publish_age = int(input('Ano de publicação (AAAA): '))
    _status = int(input('Status\n< 1 > Disponível\n< 2 > Indisponível\n-> [ ]\b\b'))

    try:
        with connect(
            host="localhost",
            port=3306,
            user="felipe",
            password="1234",
            database="Biblioteca"
        ) as connector:
            add_livro_query = """
            insert into Livro(title, autor, publish_age, _status)
            values(%s, %s, %s, %s)
            """
            values = [title, autor, publish_age, _status]

            with connector.cursor() as cursor:
                cursor.execute(add_livro_query, values)
                connector.commit()
            
    except Error as e:
        print('Erro na conexão ao Banco da dados')
        print(f'Detalhes do erro:\n{e}\n\n')
        return False
    
    loadingAnimation()
        
    system('clear')

    print('Message: O livro foi adicionado com sucesso!')
        
    time.sleep(2.5)

    loadingAnimation()
    
    opc_more_book('adicionar')
# ADICIONAR LIVROS ====================================

# REMOVER LIVROS ====================================
def removeBook():
    system('clear')

    print('===== REMOVER LIVRO DO SISTEMA =====')
    linha(50, '-')
    title = input('Título do livro que deseja remover: ')
    autor = input('Autor do livro que deseja remover: ')
    publish_age = int(input('Ano de publicação do livro que deseja remover: '))

    loadingAnimation()

    try:
        with connect(
            host="localhost",
            port=3306,
            user="felipe",
            password="1234",
            database="Biblioteca"
        ) as connector:
            mostrar_livro_desejado_query = """
            select id_book, title, autor, publish_age from Livro where title = %s or autor = %s or publish_age = %s;
            """
            values = [title, autor, publish_age]

            with connector.cursor() as cursor:
                cursor.execute(mostrar_livro_desejado_query, values)
                resultado = cursor.fetchall()
                
                print()
                # print('ID\t|  Título\t|  Autor\t|  Ano de Publicação')
                # linha(70, '-')
                lista = []
                for row in resultado:
                    tupla = list(row)
                    lista.append(tupla)

                headers = ["Id", "Título", "Autor", "Ano de Publicação"]

                print(tabulate(lista, headers=headers, tablefmt="fancy_grid"))
                print()

                connector.commit()

            print('O livro que deseja remover está nesta lista?')
            print('< 1 > Sim')
            print('< 2 > Não')
            validation = int(input('-> [ ]\b\b'))
            loadingAnimation()
            print()

            if validation == 1:
                id = int(input('digite o id do livro que você deseja excluir: '))

                tupla_id = (id,)

                system('clear')
                warning = input('Alert: Certeza que deseja excluir este livro? (s/n): ')

                if warning == 's' or warning == 'S':
                    delete_book_query = """
                    delete from Livro where id_book = %s
                    """
                    with connector.cursor() as cursor:
                        cursor.execute(delete_book_query, tupla_id)
                        connector.commit()

                    loadingAnimation()
                    system('clear')

                    print('Message: O livro foi excluído com sucesso!')
                    time.sleep(2.5)

                    opc_more_book('remover')
                else:
                    system('clear')
                    print('Message: Voltando para a seleção do livro para a exclusão...')
                    loadingAnimation()
                    removeBook()
            elif validation == 2:
                system('clear')
                print('< 1 > Exluir um livro')
                print('< 2 > Voltar para a home page')
                select = int(input('-> [ ]\b\b'))

                if select == 1:
                    system('clear')
                    print('Message: Voltando para a seleção do livro para a exclusão...')
                    time.sleep(2)
                    loadingAnimation()
                    removeBook()
                elif select == 2:
                    system('clear')
                    print('Message: Voltando para a home page...')
                    time.sleep(2)
                    loadingAnimation()
                    switch_case(adm_home_page())


    except Error as e:
        print('Erro de conexão com o Banco de dados')
        print(f'Detalhe do erro:\n{e}\n\n')



#  REMOVER LIVROS ====================================



# VER LISTA DE LIRVOS CADASTRADOS NO SISTEMA =======================================

def seeBooksInSistem():
    system('clear')

    print('===== VER LIVROS CADASTRADOS =====')
    linha(60, '-')
    
    with connect(
        host="localhost",
        port=3306,
        username="felipe",
        password="1234",
        database="Biblioteca"
    ) as connector:
        see_books_query = """
        select * from Livro;
        """
        with connector.cursor() as cursor:
            cursor.execute(see_books_query)

            result = cursor.fetchall()
            dados = []

            for row in result:
                tupla = list(row)
                if tupla[1] == 1:
                    tupla[1] = 'Disponível'
                elif tupla[1] == 2:
                    tupla[1] = 'Indisponível'
                dados.append(tupla)

            headers = ["ID", "Status", "Título", "Autor", "Ano de Publicação"]

            print(tabulate(dados, headers=headers, tablefmt="fancy_grid"))

            connector.commit()

            print('\n\nDeseja remover algum desses livros?')
            print('< 1 > Sim')
            print('< 2 > Não')
            opc = int(input('-> [ ]\b\b'))

            if opc == 1:
                id = int(input('digite o id do livro que você deseja excluir: '))
                tupla_id = (id,)
                loadingAnimation()

                system('clear')
                alert = input('Alert: Certeza que deseja remover este livro? (s/n): ')
                loadingAnimation()

                if alert == 's' or alert == 'S':
                    delete_book_query = """
                    delete from Livro where id_book = %s
                    """
                    cursor.execute(delete_book_query, tupla_id)
                    connector.commit()

                    system('clear')
                    print('Message: Livro removido com sucesso!')
                    time.sleep(2.5)
                    loadingAnimation()

                    seeBooksInSistem()
                else:
                    print('\n\n< 1 > Voltar para a home page')
                    opc = int(input('-> [ ]\b\b'))

                    if opc == 1:
                        switch_case(adm_home_page())

            else:
                system('clear')
                print('Message: Voltando para a home page...')
                time.sleep(2)
                loadingAnimation()
                switch_case(adm_home_page())

# VER LISTA DE LIRVOS CADASTRADOS NO SISTEMA =======================================


# VER LISTA DE LIVROS DISPONÍVEIS ==================================================

def showBooks1():
    system('clear')
    print('===== VER LIVROS DISPONÍVEIS PARA EMPRÉSTIMO =====')
    linha(70, '-')
    
    with connect(
        host="localhost",
        username="felipe",
        port=3306,
        password="1234",
        database="Biblioteca"
    ) as connector:
        show_disponible_books_query = """
        select * from Livro;
        """
        with connector.cursor() as cursor:
            cursor.execute(show_disponible_books_query)
            result = cursor.fetchall()

            dados = []

            for row in result:
                tupla = list(row)
                if tupla[1] == 1:
                    tupla[1] = 'Disponível'
                    dados.append(tupla)
                elif tupla[1] == 2:
                    tupla[1] == 'Indisponível'
            
            headers = ["ID", "Status", "Título", "Autor", "Ano de Publicação"]

            print(tabulate(dados, headers=headers, tablefmt="fancy_grid"))
        
        print('\n\n< 1 > Voltar para a home page')
        opc = int(input('-> [ ]\b\b'))

        if opc == 1:
            system('clear')
            print('Message: Voltando para a home page...')
            time.sleep(2)
            loadingAnimation()
            switch_case(adm_home_page())


# VER LISTA DE LIVROS DISPONÍVEIS ==================================================


switch_case(adm_home_page())
