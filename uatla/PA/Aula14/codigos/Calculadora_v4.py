from flask import Flask, request
app = Flask(__name__)

@app.route("/calc")
def calculadora():
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))
    op = request.args.get('op')

    if op == '+':
        res = x + y
    elif op == '-':
        res = x - y
    elif op == '*':
        res = x * y
    else:
        res = x / y

    return f"{x} {op} {y} = {res}"

if __name__ == "__main__":
    app.run(debug=False)
    