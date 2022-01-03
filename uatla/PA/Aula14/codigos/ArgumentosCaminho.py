from flask import Flask 
app = Flask(__name__)

from markupsafe import escape

@app.route("/<name>/inbox")
def inbox(name):
	# conteudoInbox = ...
    return f"Conteudo do inbox do usuario {escape(name)}: ..."

@app.route("/<name>/spam")
def spam(name):
	# conteudoSpam = ...
    return f"Conteudo da caixa de spam do usuario {escape(name)}: ..."

@app.route("/login/<int:id>")
def login(id):
    return f"ID recebido foi: {escape(id)}"

if __name__ == "__main__":
    app.run(debug=False)
    