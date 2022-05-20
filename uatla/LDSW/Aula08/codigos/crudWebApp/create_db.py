import sqlite3 as sql

#Liga-se à base de dados do SQLite
con = sql.connect('db_web.db')

#Cria o cursor para se fazer as queries SQL
cur = con.cursor()

#Remove a tabela utilizadores se já existir.
cur.execute("DROP TABLE IF EXISTS utilizadores")

#Cria a tabela utilizadores do zero.
sql ='''CREATE TABLE utilizadores (
	"Id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"Nome"	TEXT,
	"Email"	TEXT
)'''
cur.execute(sql)

#'Comita' as mudanças
con.commit()

#Fecha a conexão com a base
con.close()