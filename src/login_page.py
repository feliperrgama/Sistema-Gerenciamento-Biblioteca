import mysql.connector
from db_connection import db_connection  #Importa a função de conexão com o banco
from os import system  #Importa a função para limpar a tela
from loadgin_animation import loadingAnimation
from home_page_adm import adm_home_page
from home_page_aluno import home_aluno
from home_page_professor import home_profesor


def login():
    #Solicita email e senha do usuário
    system ('cls')
    print("escolha o seu tipo de usuário")
    print("1 - Administrador")
    print("2 - professor")
    print("3 - aluno")
    opc=int (input("Digite a opção desejada: "))


    if opc==1:
        email_adm= input("Digite seu email: ")
        senha_adm= input("Digite sua senha: ")
        conexao = db_connection()

        if conexao:
            cursor = conexao.cursor(dictionary=True)
            try:
                adm_try="select*from Administrador where _user=%s and _password=%s"
                cursor.execute(adm_try,(email_adm,senha_adm))
                adm=cursor.fetchone()
                if adm:
                    loadingAnimation()
                    system('cls')
                    print(f"\nLogin bem-sucedido! Bem-vindo(a)")
                    loadingAnimation()
                    switch_case(adm_home_page())
                else:
                    loadingAnimation()
                    print("\nEmail ou senha incorretos. Tente novamente.")
                    loadingAnimation()
                    login()
            except mysql.connector.Error as err:
                print(f"Erro ao realizar login: {err}")
    elif opc==2:
        email_prof= input("Digite seu email: ")
        senha_prof= input("Digite sua senha: ")
        conexao = db_connection()

        if conexao:
            cursor = conexao.cursor(dictionary=True)
            try:
                prof_try="select*from Usuario where email=%s and _password=%s"
                cursor.execute(prof_try,(email_prof,senha_prof))
                prof=cursor.fetchone()
                prof_life=[]
                for linha in prof:
                    prof_life.append(linha)
                
                if prof:
                    loadingAnimation()
                    system('cls')
                    print(f"\nLogin bem-sucedido! Bem-vindo(a)")
                    loadingAnimation()
                    home_professor(prof_life[0])
                else:
                    loadingAnimation()
                    print("\nEmail ou senha incorretos. Tente novamente.")
                    loadingAnimation()
                    login()
            except mysql.connector.Error as err:
                print(f"Erro ao realizar login: {err}")
    elif opc==3:
        email_aluno= input("Digite seu email: ")
        senha_aluno= input("Digite sua senha: ")
        conexao = db_connection()

        if conexao:
            cursor = conexao.cursor(dictionary=True)
            try:
                aluno_try="select*from Usuario where email=%s and _password=%s"
                cursor.execute(aluno_try,(email_aluno,senha_aluno))
                aluno=cursor.fetchone()
                aluno_life=[]
                for linha in aluno:
                    aluno_life.append(linha)
                if aluno:
                    loadingAnimation()
                    system('cls')
                    print(f"\nLogin bem-sucedido! Bem-vindo(a)")
                    loadingAnimation()
                    home_aluno(aluno_life[0])
                else:
                    loadingAnimation()
                    print("\nEmail ou senha incorretos. Tente novamente.")
                    loadingAnimation()
                    login()
            except mysql.connector.Error as err:
                print(f"Erro ao realizar login: {err}")


if __name__ == "__main__":
    login()