import mysql.connector

def db_connection():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",        
            password="Mavaba123456@",
            database="biblioteca20"
        )

        if conexao.is_connected():
            print("Conectado com sucesso!")
            return conexao

    except mysql.connector.Error as err:
        print(f"Erro ao conectar: {err}")
        return None

if __name__=="__main__":
    conexao = db_connection()
    if conexao:
        print("Teste concluído – conexão funcionando.")
        conexao.close()
    else:
        print("Falha na conexão.")

   