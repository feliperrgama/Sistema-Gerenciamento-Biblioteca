import mysql.connector
from db_connection import db_connection  #Importa a função de conexão com o banco

def login():
    #Solicita email e senha do usuário
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    conexao = db_connection()
    if conexao:
        cursor = conexao.curscdor(dictionary=True)

        try:
            #Verifica se existe um usuário com o email e senha informados
            query = "SELECT * FROM usuarios WHERE email = %s AND senha = %s"
            cursor.execute(query, (email, senha))
            usuario = cursor.fetchone()

            if usuario:
                print(f"\nLogin bem-sucedido! Bem-vindo(a), {usuario['tipo']}!")
            else:
                print("\nEmail ou senha incorretos. Tente novamente.")

        except mysql.connector.Error as err:
            print(f"Erro ao realizar login: {err}")

        finally:
            cursor.close()
            conexao.close()
    else:
        print("Falha na conexão com o banco de dados.")


if __name__ == "__main__":
    login()