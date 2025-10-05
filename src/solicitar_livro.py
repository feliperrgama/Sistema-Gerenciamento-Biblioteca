from db_connection import db_connection

def solicitar_livro(usuario_id, titulo, autor):
    conexao = db_connection()
    if conexao:
        try:
            cursor = conexao.cursor()
            query = """
            INSERT INTO solicitacoes_livros (usuario_id, titulo_livro, autor_livro)
            VALUES (%s, %s, %s)
            """
            cursor.execute(query, (usuario_id, titulo, autor))
            conexao.commit()
            print("\nSolicitação registrada com sucesso!")

        except Exception as e:
            print(f"\nErro ao registrar solicitação: {e}")

        finally:
            cursor.close()
            conexao.close()
    else:
        print("Falha na conexão com o banco de dados.")

if __name__ == "__main__":
    usuario_id = int(input("Digite o ID do usuário: "))
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor do livro: ")
    solicitar_livro(usuario_id, titulo, autor)