from platform import python_branch
import sqlite3
con = sqlite3.connect('minhaBase.db')

cur = con.cursor()

# Insere linhas na tabela
cur.execute("INSERT INTO lp(nome, anoCriacao, percUso) VALUES ('Python',1991, 15.3)")
cur.execute("INSERT INTO lp(nome, anoCriacao, percUso) VALUES ('C',1972, 12.3)")
cur.execute("INSERT INTO lp(nome, anoCriacao, percUso) VALUES ('Java',1994, 11.8)")
cur.execute("INSERT INTO lp(nome, anoCriacao, percUso) VALUES ('Java',1994, 11.8)")
cur.execute("INSERT INTO lp(nome, anoCriacao, percUso) VALUES ('Java',1994, 11.8)")
cur.execute("INSERT INTO lp(nome, anoCriacao, percUso) VALUES ('Java',1994, 11.8)")
cur.execute("INSERT INTO lp(nome, anoCriacao, percUso) VALUES ('Java',1994, 11.8)")
cur.execute("INSERT INTO lp(nome, anoCriacao, percUso) VALUES ('Java',1994, 11.8)")
cur.execute("INSERT INTO lp(nome, anoCriacao, percUso) VALUES ('Java',1994, 11.8)")
cur.execute("INSERT INTO lp(nome, anoCriacao, percUso) VALUES ('Java',1994, 11.8)")
cur.execute("INSERT INTO lp(nome, anoCriacao, percUso) VALUES ('Java',1994, 11.8)")
cur.execute("INSERT INTO lp(nome, anoCriacao, percUso) VALUES ('Java',1994, 11.8)")

# Compromete (commit) as mudanças
con.commit()

# Ao final, fechar a conexão com a base.
# Assegure-se de que todos os commits tenham sido feitos.
con.close()