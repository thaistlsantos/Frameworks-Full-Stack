import os
from unicodedata import name
from flask import Flask, jsonify, request, render_template
from math import sqrt

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('calculadora.html')


@app.route('/calculadoraformulario', methods=['POST', 'GET'])
def calcular():
    numero1 = request.form['num1']
    numero2 = request.form['num2']
    operacao = request.form['operacao']
    num1 = int(numero1)
    num2 = int(numero2)


    if operacao == '+':
        return str(num1 + num2)
    elif operacao == '-':
        return str(num1 - num2)
    elif operacao == '*':
        return str(num1 * num2)
    elif operacao == '/':
        return str(num1 / num2)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='localhost', port=port)