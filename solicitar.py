import mysql.connector
import os

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "1234"),
    "database": "Biblioteca20"
}

def solicitar_livro_sem_alterar_db(id_user: int, id_livro: int):
    try:
        with mysql.connector.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id_status FROM Livro WHERE id_book = %s", (id_livro,))
                resultado_livro = cursor.fetchone()

                if not resultado_livro:
                    print(f"❌ Erro: Livro com ID {id_livro} não encontrado.")
                    return

                if not resultado_livro[0]:
                    print(f"❌ Livro indisponível no momento.")
                    return
                
                sql_check = "SELECT COUNT(*) FROM Solicitacao WHERE id_user = %s AND id_book = %s"
                cursor.execute(sql_check, (id_user, id_livro))
                if cursor.fetchone()[0] > 0:
                    print("🔵 Você já enviou uma solicitação para este livro.")
                    return

                sql_insert = "INSERT INTO Solicitacao (id_user, id_book) VALUES (%s, %s)"
                cursor.execute(sql_insert, (id_user, id_livro))
                conn.commit()
                
                print(f"✅ Solicitação do livro ID {id_livro} enviada com sucesso!")

    except mysql.connector.Error as err:
        print(f"❌ Erro de banco de dados: {err}")

def ver_solicitacoes_admin_sem_alterar_db():
    print("\n--- VISUALIZAR SOLICITAÇÕES DE LIVROS ---")
    
    sql_query = """
        SELECT 
            s.id AS id_solicitacao, u.id_user, u._name AS nome_usuario, l.id_title AS titulo_livro,
            CASE 
                WHEN a.id_aluno IS NOT NULL THEN 'sr'
                WHEN p.id_professor IS NOT NULL THEN 'tr'
                ELSE '??'
            END AS tipo_usuario
        FROM Solicitacao s
        JOIN Usuario u ON s.id_user = u.id_user
        JOIN Livro l ON s.id_book = l.id_book
        LEFT JOIN Aluno a ON u.id_user = a.id_user
        LEFT JOIN Professor p ON u.id_user = p.id_user
        ORDER BY s.id ASC;
    """
    
    try:
        with mysql.connector.connect(**DB_CONFIG) as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(sql_query)
                solicitacoes = cursor.fetchall()
                
                if not solicitacoes:
                    print("🔵 Nenhuma solicitação encontrada.")
                    return
                
                print(f"{'ID Solic.':<12}| {'ID Usuário':<12}| {'Tipo':<6}| {'Nome do Solicitante':<25}| {'Título do Livro'}")
                print("-" * 90)
                
                for r in solicitacoes:
                    print(
                        f"{r['id_solicitacao']:<12}| "
                        f"{r['id_user']:<12}| "
                        f"{r['tipo_usuario']:<6}| "
                        f"{r['nome_usuario']:<25}| "
                        f"{r['titulo_livro']}"
                    )
                
    except mysql.connector.Error as err:
        print(f"❌ Erro de banco de dados ao buscar solicitações: {err}")

def menu_solicitacao_usuario():
    print("\n--- Portal do Usuário: Solicitar Livro ---")
    try:
        id_usuario = int(input("Digite o seu ID de usuário: "))
        id_livro = int(input("Digite o ID do livro que deseja solicitar: "))
        solicitar_livro_sem_alterar_db(id_usuario, id_livro)
    except ValueError:
        print("❌ Entrada inválida. IDs devem ser números.")

def main():
    while True:
        print("\n" + "="*15 + " SISTEMA DE BIBLIOTECA " + "="*15)
        print("1. Usuário (Aluno/Professor)")
        print("2. Administrador")
        print("3. Sair do programa")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            menu_solicitacao_usuario()
        elif opcao == '2':
            ver_solicitacoes_admin_sem_alterar_db()
        elif opcao == '3':
            print("\nSaindo do sistema. Até logo!")
            break
        else:
            print("❌ Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()