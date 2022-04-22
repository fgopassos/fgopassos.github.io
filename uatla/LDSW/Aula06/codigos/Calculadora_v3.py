from flask import Flask, render_template
app = Flask(__name__)

@app.route("/todas/<float:x>/<float:y>")
def todas(x, y):

    resultados = {
        "x": x*y,
        "+": x+y, 
        "-": x-y
    }
    if y != 0:
        resultados["/"] = x/y
    return render_template('calculadora_v3.html', x=x, y=y, resultados=resultados) 

if __name__ == "__main__":
    app.run(debug=False)
    