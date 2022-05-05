import sqlite3 as sql
import os
from flask import Flask, jsonify, request, render_template
import backend

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('page.html')


@app.route('/gravar', methods=['POST', 'GET'])
def gravar():
    nome = request.form['nome']
    email = request.form['email']
    endereco = request.form['endereco']

    if nome and email and endereco:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute(
                "INSERT INTO usuarios (nome, email, endereco) VALUES (?,?,?)", (nome, email, endereco))

            con.commit()
            msg = "Informações inseridas com sucesso"
            return render_template("page.html", msg=msg)
            con.close()
    else:
        return("Informações não inseridas")


@app.route('/listar')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from usuarios")

    rows = cur.fetchall()
    return render_template("listar.html", rows=rows)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)