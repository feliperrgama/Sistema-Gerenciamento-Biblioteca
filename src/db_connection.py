import mysql.connector
import getpass

def db_connection():
    try:
        with mysql.connector.connect(
            host="localhost",
            user="felipe",
            password="1234",
            database="Biblioteca"
        ) as connection:
            print('Esperando o que irá fazer aqui...')

    except:
        print('erro')