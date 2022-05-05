import sqlite3

conn = sqlite3.connect('database.db')
print("Banco de Dados Criado com Sucesso")

conn.execute('CREATE TABLE users (nome TEXT, email TEXT, endereco TEXT)')
print("Tabelas Criadas com Sucesso")
conn.close()