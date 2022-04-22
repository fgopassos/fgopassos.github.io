from flask import Flask, request, make_response
app = Flask(__name__)

cestos = {}
@app.route("/adicionaAoCesto")
def adicionaAoCesto():

    prodID = request.args.get('prodID')
    userID = request.cookies.get('userID')
    cestos[userID].append(prodID)
    return f"Produto adicionado! Cesto agora tem:<br> {cestos[userID]}"

@app.route("/atribuiID")
def atribuiID():

    novoID = 'ab5bc01'
    cestos[novoID] = []
    resp = make_response('ID atribuído!')
    resp.set_cookie('userID', novoID)
    return resp

if __name__ == "__main__":
    app.run(debug=False)
    