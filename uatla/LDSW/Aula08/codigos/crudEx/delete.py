import sqlite3

con = sqlite3.connect('minhaBase.db')

cur = con.cursor()

# Insere uma linha na tabela
cur.execute("DELETE FROM lp WHERE id=0")

# Guarda (commit) as mudanças
con.commit()

# Ao final, fechar a conexão com a base.
# Assegure-se de que todos os commits tenham sido feitos.
con.close()

print("Remoção concluída...")