from flask import Flask, request 
app = Flask(__name__)

@app.route('/alunos', methods=['GET', 'POST'])
def alunos():
    if request.method == 'POST':	# Objeto build-in request contém informações sobre a requisição
        return "cadastro aluno"		# Se é um POST, cadastramos um novo aluno
    else:
        return "lista alunos"		# Se é um GET, listamos alunos cadastrados

@app.route('/alunos2', methods=['GET'])
def alunosGET():
    return "lista alunos"

@app.route('/alunos2', methods=['POST'])
def alunosPOST():
    return "cadastro aluno"

if __name__ == "__main__":
    app.run(debug=False)
    