from flask import Flask, request, render_template, session, redirect, url_for
app = Flask(__name__)
app.secret_key = b'((s23e__#i54e/*!'
def verificaLogin(username, password):

    if username == "pedro" and password == "123456":
        return True
    return False

@app.route("/login", methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        if verificaLogin(request.form['username'], 
                request.form['password']):
            session['username'] = request.form['username']
            return redirect(url_for('principal'))
        else:
            return 'Nome de usuário ou palavra-passe inválidos!'
    return render_template('login.html')

@app.route("/")
def principal():

    if 'username' in session:
        return f"Seja bem-vindo, {session['username']}"
    else:
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=False)
