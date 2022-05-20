import sqlite3
con = sqlite3.connect('minhaBase.db')

cur = con.cursor()

# Para fazer consultas à base de dados lp em minhaBase.db
# Vamos ordenar as linguagens por ano de criação.
consulta = cur.execute('SELECT * FROM lp ORDER BY anoCriacao')

# 'consulta' é um objeto iterável e cada elemento é uma linha do
# resultado do select.
for i in consulta: print(i)

# Vamos ordenar as linguagens por percentual de uso. 
cur.execute('SELECT * FROM lp ORDER BY percUso')

# fetch all retorna uma lista com o resultado da consulta
lista_consulta = cur.fetchall()
print(lista_consulta)

con.close()