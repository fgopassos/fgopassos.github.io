from flask import Flask, request, render_template
app = Flask(__name__)

def verificaLogin(username, password):

    if username == "pedro" and password == "123456":
        return True
    return False

@app.route("/login", methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        if verificaLogin(request.form['username'], 
                request.form['password']):
            return 'Login bem sucedido!'
        else:
            return 'Nome de usuário ou palavra-passe inválidos!'
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=False)
    