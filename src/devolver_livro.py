from loading_animation import loadingAnimation
from time import sleep
from mysql.connector import connect
from os import system
from linha_function import linha

def devolverLivro(id_user):
    id_user_tupla = (id_user,)
    system('clear')

    print('===== DEVOLVER LIVRO =====')
    linha(50, '-')
    print('Seu(s) livro(s)')
    try:
        with connect(
            host="localhost",
            port=3306,
            username="felipe",
            password="1234",
            database="Biblioteca"
        ) as connector:
            select_table_guarda_query = """
            select id_book from Guarda where id_user = %s
            """
            with connector.cursor() as cursor:
                cursor.execute(select_table_guarda_query, id_user_tupla)
                #continuar daqui...

    except: