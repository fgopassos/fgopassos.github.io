from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/primos")
def primos():
    lista = [2, 3, 5, 7, 11, 13, 17]
    return jsonify(lista)
		
if __name__ == "__main__":
    app.run(debug=False)
