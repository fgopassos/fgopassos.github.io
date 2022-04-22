from flask import Flask, request, session
app = Flask(__name__)
app.secret_key = b'((s23e__#i54e/*!'
cestos = {}
@app.route("/adicionaAoCesto")
def adicionaAoCesto():

    prodID = request.args.get('prodID')
    userID = session['userID']
    cestos[userID].append(prodID)
    return f"Produto adicionado! Cesto agora tem:<br> {cestos[userID]}"

@app.route("/atribuiID")
def atribuiID():

    novoID = 'ab5bc01'
    cestos[novoID] = []
    session['userID'] = novoID
    return 'ID atribuído!'

if __name__ == "__main__":
    app.run(debug=False)
    