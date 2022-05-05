import sqlite3

def consulta():

    con = sqlite3.connect('cadastro_dados.db')

    cur = con.cursor()

    cur.execute('select * from funcionarios')

    dados = cur.fetchall()

    cur.close()
    con.close()

    return dados

def gravar(nome, email, endereco):

    con = sqlite3.connect('cadastro_dados.db')

    cur = con.cursor()

    cur.execute("""INSERT INTO funcionarios (nome, email, endereco)VALUES (?,?,?)""", (nome, email, endereco))

    cur.execute('select * from funcionarios')

    dados = cur.fetchall()

    con.commit()
    cur.close()
    con.close()
