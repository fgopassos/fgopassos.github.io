from flask import Flask 
app = Flask(__name__)

@app.route("/cadeiras")				
def alunos():
    return "Programação avançada, Linguagem de Programação, Estatística, Redes de Computadores"	


@app.route("/alunos")				
def hello():
    return "Antônio, Carla, Daniel, João, Paula, Tiago"	

if __name__ == "__main__":
    app.run(debug=False)
    