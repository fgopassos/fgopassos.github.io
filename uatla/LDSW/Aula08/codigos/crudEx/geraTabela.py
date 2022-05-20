import sqlite3
con = sqlite3.connect('minhaBase.db')

# Criar cursor para realizar operações SQL
cur = con.cursor()

# Comando SQL para criar a tabela de linguagens de programação.
sql_create_table = '''CREATE TABLE lp (
    'id' INTEGER PRIMARY KEY AUTOINCREMENT,
    'nome' TEXT,
    'anoCriacao' INTEGER,
    'percUso' REAL
    )'''

# Cria uma tabela para guardar...
cur.execute(sql_create_table)

# Guarda (commit) as mudanças
con.commit()

# Ao final, fechar a conexão com a base.
# Assegure-se de que todos os commits tenham sido feitos.
con.close()