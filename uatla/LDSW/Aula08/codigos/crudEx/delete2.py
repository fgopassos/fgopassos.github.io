import sqlite3
from markupsafe import escape # Usado para impedir ataque de injeção de código html ou js

con = sqlite3.connect('minhaBase.db')

try:
    cur = con.cursor()

    # Insere uma linha na tabela
    id_input = input("Entre com o id: ")
    cur.execute("DELETE FROM lp WHERE id=?", (id_input,))

    # Guarda (commit) as mudanças
    con.commit()
except Exception as m:
    print(m)
finally:
    # Ao final, fechar a conexão com a base.
    # Assegure-se de que todos os commits tenham sido feitos.
    con.close()

print("Remoção concluída...")