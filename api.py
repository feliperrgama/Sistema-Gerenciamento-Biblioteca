from flask import Flask, render_template
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

@app.route('/usuarios/<nome_do_usuario>')
def users(nome_do_usuario):
    return render_template("/src-front/home_page_user.html", nome_do_usuario=nome_do_usuario)

@app.route('/<string:nome>')
def error(nome):
    return f'Página ({nome}) não encontrada!'


# Colocar site no ar
if __name__ == "__main__":
    app.run(debug = True)



