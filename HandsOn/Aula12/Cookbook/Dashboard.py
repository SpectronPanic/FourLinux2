from flask import Flask,render_template,jsonify,request
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/provisionar/",methods=["POST"])
def provisionar():
    recv_json = json.loads(request.get_json())
    with open("fila/%s.json"%recv_json.get("application"),'w') as f:
        f.write(json.dumps(recv_json))
    return jsonify({"message":"Servico enviado para o privisionamento"})


if __name__ == '__main__':
    app.run(debug=True)
