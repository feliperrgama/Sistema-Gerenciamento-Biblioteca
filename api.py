from flask import Flask, render_template, request, jsonify
from mysql.connector import connect, Error

app = Flask(__name__) # Recomensação da documentação

# 1 - Criar a 1ª página do site
# toda página tem um route e uma função
# route -> O caminho que vem depois do meu domínio ex: youtube.com/route, route = usuarios. Qual link vai abrir qual página
# função -> O que eu quero exibir em tal route.
# template -> front

#decorator -> uma linha de código que atribui uma nova funcionalidade para a a função que vem logo em baixo dela.
@app.route('/') 
def homepage():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("/src-front/login.html")

@app.route('/register')
def register():
    return render_template('/src-front/register.html')

@app.route('/registrar_user')
def registrar():
    data = request.get_json()

    if not data:
        return jsonify({'message': 'Requisição inválida'}), 400
    
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    select = data.get('select')

    if not all([username, email, password, select]):
        return jsonify({'message': 'Estão faltando campos obrigatórios'}), 400
    
    try:
        with connect(
            host="localhost",
            username="felipe",
            password="1234",
            database="Biblioteca"
        ) as connector:
            register_user_query = """
            insert into Usuario (_name, email, _password) values (%s, %s, %s)
            """
            with connector.cursor() as cursor:
                cursor.execute(register_user_query, (username, email, password))
                
                if select == 1:
                    select_user_atual_query = """
                    select id_user from Usuario where username = %s and email = %s and password = %s
                    """
                    register_aluno_query = """
                    insert into Aluno (id_user) values (%s) 
                    """

                    cursor.execute(select_user_atual_query, (username, email, password))
                    result = cursor.fetchone()

                    cursor.execute(register_aluno_query, result)

                    cursor.commit()
                elif select == 2:
                    select_user_atual_query = """
                    select id_user from Usuario where username = %s and email = %s and password = %s
                    """
                    register_prof_query = """
                    insert into Aluno (id_user) values (%s) 
                    """

                    cursor.execute(select_user_atual_query, (username, email, password))
                    result = cursor.fetchone()

                    cursor.execute(register_prof_query, result)

    except Error as err:
        print(f'Erro em relação ao banco de dados:\n{err}\n\n')

@app.route('/usuarios/<nome_do_usuario>')
def users(nome_do_usuario):
    return render_template("/src-front/home_page_user.html", nome_do_usuario=nome_do_usuario)

@app.route('/<string:nome>')
def error(nome):
    return f'Página ({nome}) não encontrada!'


# Colocar site no ar
if __name__ == "__main__":
    app.run(debug = True)



