#!/usr/bin/python

#4linux.com.br/usuarios/
from flask import Flask, request
from Views.GruposView import grupos
from Views.UsuariosView import usuarios

app = Flask(__name__)
app.register_blueprint(grupos)
app.register_blueprint(usuarios)

@app.route("/")
def index():
    return "Debug ativado"



if __name__ == '__main__':
    app.run(port=3000,host="0.0.0.0",debug= True)