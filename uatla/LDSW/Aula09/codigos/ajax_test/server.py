from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/soma')
def soma():
    try:
        a = int(request.args['a'])
        b = int(request.args['b'])
        r = a + b
        print(a, "+", b, "=", r)
        return jsonify(resultado=r)
    except Exception as m:
        print(m)
        return(jsonify(resultado=str(m)))

@app.route('/')
def index():
    return render_template('index.html')

# Inicio do programa:
if __name__ == "__main__":
    app.run(debug=True)
