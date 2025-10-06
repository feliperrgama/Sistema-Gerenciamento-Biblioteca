from db_connection import db_connection

conexao = db_connection()

if conexao:
    print("Teste concluído — conexão funcionando.")
    conexao.close()
else:
    print("Falha ao conectar.")