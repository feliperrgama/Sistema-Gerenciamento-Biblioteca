from flask import Flask, request, jsonify
from src.bd_connection import conectar # se você já tem esse módulo

app = Flask(__name__)

@app.route("/register_user", methods=["POST"])
def register_user():
    data = request.get_json()
    nome = data.get("nome")
    email = data.get("email")
    senha = data.get("senha")

    try:
        conn = conectar()
        cursor = conn.cursor()

        sql = "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, email, senha))
        conn.commit()

        return jsonify({"message": "Usuário cadastrado com sucesso!"}), 201

    except Exception as e:
        print("Erro ao inserir no banco:", e)
        return jsonify({"message": "Erro ao cadastrar usuário."}), 500

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
        app.run(debug=True)