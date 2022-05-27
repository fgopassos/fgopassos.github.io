from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        for ficheiros in request.files.getlist('ficheiros'):
            print("File", ficheiros.filename)
            if ficheiros.filename != '':
                ficheiros.save(ficheiros.filename)
        return jsonify(success=True)
    except Exception:
        return jsonify(success=False)


@app.route('/')
def index():
    return render_template('index.html')

# Inicio do programa:
if __name__ == "__main__":
    app.run(debug=True)
