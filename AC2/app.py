from flask import Flask, render_template, request
import conectar

app = Flask(__name__)

@app.route('/create')
def create():
    conectar.estrutura_banco()
    return 'Estrutura criada'

@app.route('/')
def main():
    return render_template('page.html')

@app.route('/gravar', methods=['POST', 'GET'])
def gravar():
    nome = request.form['nome']
    email = request.form['email']
    endereco = request.form['endereco']
    
    conectar.gravar(nome, email, endereco)

    dados = conectar.consulta()

    return 'Dados foram Gravados'

@app.route('/consultar')
def consultar():
    dados = conectar.consulta()
    return dados.to_html()

app.run(debug=True)