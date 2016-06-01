#!/usr/bin/python

from flask import Blueprint,jsonify,request
from Model import Usuarios
import json

usuarios = Blueprint("usuarios",__name__)

@usuarios.route("/usuarios/",methods=["GET"])
def index_usuarios():
    lista_usuarios = json.loads(Usuarios.objects.to_json())
    return jsonify({"usuarios":lista_usuarios})

@usuarios.route("/usuarios/",methods=["POST"])
def inserir_usuarios():
    try:
        dados = request.get_json()
        u = Usuarios()
        for key in dados.keys():
            setattr(u,key,dados[key])
        u.save()
        return jsonify({"message":"Usuario cadastrado com sucesso"})
    except Exception as e:
        return jsonify({"message":"Falhou ao cadastrar: %s"%e})

@usuarios.route("/usuarios/<id>/",methods=["GET"])
def select_usuarios(id):
    u = json.loads(Usuarios.objects(id=id).to_json())
    data = {"usuario":u}
    return jsonify(data)

@usuarios.route("/usuarios/<id>/",methods=["PUT"])
def update_usuarios(id):
    try:
        dados = request.get_json()
        u = Usuarios.objects(id=id).first()
        for key in dados.keys():
          setattr(u,key,dados[key])
        u.save()
        data = {"message":"Atualizando o usuario cujo o ID e igual a %s"%id}
        return jsonify(data)
    except Exception as e:
        return jsonify({"message":"Falhou ao atualizar: %s"%e})

@usuarios.route("/usuarios/<id>/",methods=["DELETE"])
def delete_usuarios(id):
    u = Usuarios.objects(id=id)
    u.delete()
    data = {"message":"Deletando usuario cujo o ID e igual a %s"%id}
    return jsonify(data)

