from flask import Flask, render_template
app = Flask(__name__)

@app.route("/todas/<float:x>/<float:y>")
def todas(x, y):
    if y == 0:
        return render_template('calculadora.html', x=x, y=y, 
                            multiplicacao=x*y, 
                            soma=x+y, 
                            subtracao=x-y)
    else:
        return render_template('calculadora.html', x=x, y=y, 
                            multiplicacao=x*y, 
                            divisao=x/y, 
                            soma=x+y, 
                            subtracao=x-y)

if __name__ == "__main__":
    app.run(debug=False)
    