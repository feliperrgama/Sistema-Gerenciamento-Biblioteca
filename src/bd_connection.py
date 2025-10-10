import mysql.connector

def conectar():
    conn = mysql.connector.connect(
        host="localhost",       # endereço do MySQL
        user="root",            # seu usuário MySQL (geralmente é root)
        password="Mavaba123456@",   # coloque aqui a senha do seu MySQL
        database="biblioteca20" # nome do banco que você quer usar
    )
    return conn
   