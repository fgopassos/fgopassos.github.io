from flask import Flask
app = Flask(__name__)

@app.route("/carro")
def carro():
    
	return {
			"Fabricante": "Fiat",
			"Modelo": "500",
			"Peso": 940
		}

if __name__ == "__main__":
    app.run(debug=False)
