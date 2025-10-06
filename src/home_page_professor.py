import mysql.connector
import time

# ==========================================
#  Função 1 – Solicitar livro
# ==========================================
def solicitar_livro(usuario_logado):
    print("\n=== SOLICITAR LIVRO ===")

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Asm693693.",  
        database="Biblioteca20"
    )
    cursor = conexao.cursor(dictionary=True)

    # Mostra livros disponíveis
    cursor.execute("SELECT id_livro, titulo, autor FROM Livro WHERE status = 'Disponível';")
    livros = cursor.fetchall()

    if not livros:
        print("Nenhum livro disponível para empréstimo.")
    else:
        print("\nLivros disponíveis:")
        for livro in livros:
            print(f"{livro['id_livro']} - {livro['titulo']} ({livro['autor']})")

        try:
            id_escolhido = int(input("\nDigite o ID do livro que deseja solicitar: "))

            # Verifica se o ID é válido
            cursor.execute("SELECT * FROM Livro WHERE id_livro = %s AND status = 'Disponível';", (id_escolhido,))
            livro = cursor.fetchone()

            if livro:
                # Marca o livro como emprestado
                cursor.execute("UPDATE Livro SET status = 'Indisponível' WHERE id_livro = %s;", (id_escolhido,))
                cursor.execute("INSERT INTO Emprestimo (id_livro, id_user) VALUES (%s, %s);",
                               (id_escolhido, usuario_logado["id_user"]))
                conexao.commit()
                print(f"\n📖 Você solicitou o livro: {livro['titulo']}")
            else:
                print("ID inválido ou livro não disponível.")

        except ValueError:
            print("Entrada inválida. Digite apenas números.")

    cursor.close()
    conexao.close()
    time.sleep(2)


# ==========================================
#  Função 2 – Ver lista de livros disponíveis
# ==========================================
def ver_livros_disponiveis(usuario_logado):
    print("\n=== LISTA DE LIVROS DISPONÍVEIS ===")

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sua_senha",
        database="Biblioteca20"
    )
    cursor = conexao.cursor(dictionary=True)

    cursor.execute("SELECT titulo, autor, ano, categoria FROM Livro WHERE status = 'Disponível';")
    livros = cursor.fetchall()

    if not livros:
        print("Nenhum livro disponível.")
    else:
        print(f"\n{'Título':<35} {'Autor':<25} {'Ano':<6} {'Categoria':<20}")
        print("-" * 90)
        for livro in livros:
            print(f"{livro['titulo']:<35} {livro['autor']:<25} {livro['ano']:<6} {livro['categoria']:<20}")

    cursor.close()
    conexao.close()
    input("\nPressione ENTER para voltar ao menu...")


# ==========================================
#  Função 3 – Devolver livro
# ==========================================
def devolver_livro(usuario_logado):
    print("\n=== DEVOLVER LIVRO ===")

    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sua_senha",
        database="Biblioteca20"
    )
    cursor = conexao.cursor(dictionary=True)

    # Mostra livros emprestados ao professor
    cursor.execute("""
        SELECT E.id_emprestimo, L.titulo, L.autor
        FROM Emprestimo E
        JOIN Livro L ON E.id_livro = L.id_livro
        WHERE E.id_user = %s;
    """, (usuario_logado["id_user"],))
    emprestimos = cursor.fetchall()

    if not emprestimos:
        print("Você não possui livros emprestados.")
    else:
        print("\nSeus livros emprestados:")
        for emp in emprestimos:
            print(f"{emp['id_emprestimo']} - {emp['titulo']} ({emp['autor']})")

        try:
            id_emprestimo = int(input("\nDigite o ID do empréstimo que deseja devolver: "))

            cursor.execute("""
                SELECT id_livro FROM Emprestimo WHERE id_emprestimo = %s AND id_user = %s;
            """, (id_emprestimo, usuario_logado["id_user"]))
            registro = cursor.fetchone()

            if registro:
                cursor.execute("UPDATE Livro SET status = 'Disponível' WHERE id_livro = %s;", (registro["id_livro"],))
                cursor.execute("DELETE FROM Emprestimo WHERE id_emprestimo = %s;", (id_emprestimo,))
                conexao.commit()
                print(" Livro devolvido com sucesso!")
            else:
                print("ID inválido ou empréstimo não encontrado.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

    cursor.close()
    conexao.close()
    time.sleep(2)


# ==========================================
#  HOME PAGE DO PROFESSOR
# ==========================================
def home_professor(usuario_logado):
    while True:
        print("\n==============================")
        print(" HOME PAGE - PROFESSOR")
        print("==============================")
        print("1️⃣ Solicitar Livros")
        print("2️⃣ Ver Lista de Livros Disponíveis")
        print("3️⃣ Devolver Livro")
        print("0️⃣ Sair")
        print("==============================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            solicitar_livro(usuario_logado)
        elif opcao == "2":
            ver_livros_disponiveis(usuario_logado)
        elif opcao == "3":
            devolver_livro(usuario_logado)
        elif opcao == "0":
            print("Saindo da Home Page...")
            time.sleep(1)
            break
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(1)


# ==========================================
#  Simulação de Login
# ==========================================
usuario_logado = {
    "id_user": 2,
    "nome": "Professor Carlos",
    "perfil": "Professor"
}

# Se o login for de um professor, vai direto para a Home Page
if usuario_logado["perfil"] == "Professor":
    home_professor(usuario_logado)
else:
    print("Acesso negado. Apenas professores podem acessar esta página.")
