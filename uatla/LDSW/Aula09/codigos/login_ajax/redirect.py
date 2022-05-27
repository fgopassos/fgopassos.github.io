from flask import Flask, request, jsonify, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = b'((s23e__#i54e/*!'

def verificaLogin(username, password):
    if username == "pedro" and password == "123456":
        return True
    return False

@app.route("/login", methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('principal'))
    # Trata mensagem AJAX:
    if request.method == 'POST':
        user = request.form['user']
        pwd = request.form['pwd']
        print(user, pwd)
        if verificaLogin(user, pwd):
            session['username'] = user
            return jsonify({'success':True, 'redirect':url_for('principal')})
        else:
            return jsonify({'success':False})
    return render_template('login.html')

@app.route("/")
def principal():

    print("Principal")
    if 'username' in session:
        return f"Seja bem-vindo, {session['username']}"
    else:
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
