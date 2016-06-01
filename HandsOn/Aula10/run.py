#!/usr/in/python


from flask import Flask, render_template,jsonify, request
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/api/dexterops/", methods=["POST"])
def cad_app():
    recebido = json.loads(request.get_json())
    nome = recebido.get("app")
    recebido = json.dumps(recebido)
    with open("fila/%s.json"%nome,'w') as f:
        f.write(recebido)

    return jsonify({"message":"Dados enviados para a fila"})


if __name__ == '__main__':
    app.run(debug=True)
