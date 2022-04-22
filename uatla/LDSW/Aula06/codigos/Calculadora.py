from flask import Flask 
app = Flask(__name__)

from markupsafe import escape

@app.route("/mult/<int:x>/<int:y>")
def multiplicacao(x, y):
    return f"{x} * {y} = {x*y}"

if __name__ == "__main__":
    app.run(debug=False)
    