from flask import Flask 	# Importa-se a biblioteca do Flask
app = Flask(__name__)		# Cria-se uma "Aplicação Flask"

@app.route("/")				# O decorator app.route() associa a função ao caminho "/" no servidor
def hello():
    return "Hello World"	# Valor retornado é simplesmente uma string enviada como (corpo) da resposta HTTP.

if __name__ == "__main__":
    app.run(debug=False)
    