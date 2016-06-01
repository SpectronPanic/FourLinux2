#!/usr/bin/python

from flask import Blueprint,jsonify, request
from Models.Model import Usuarios as UsuariosModel
import json

usuarios = Blueprint("usuarios", __name__)

@usuarios.route("/usuarios/")
def index():
    response = json.loads(UsuariosModel.objects.to_json())
    return jsonify({"usuarios":response})


@usuarios.route("/usuarios/", methods=["POST"])
def add_usuarios():
    u = UsuariosModel()
    print request.get_json()
    u.nome = request.get_json().get("nome")
    u.email = request.get_json().get("email")
    u.save()
    return jsonify({"message":"Usuario cadastrado com sucesso!"})

@usuarios.route("/usuarios/<id>/", methods=["PUT"])
def update_usuarios(id):
    u = UsuariosModel.objects(id=id).first()
    u.nome = request.get_json().get("nome")
    u.email = request.get_json().get("email")
    u.save()
    return jsonify({"message":"Dados atualizados com sucesso!"})

@usuarios.route("/usuarios/<id>/", methods=["GET"])
def get_usuarios(id):
    u = UsuariosModel.objects(id=id).first().to_json()
    response = json.loads(u)
    return jsonify({"usuarios":response})

@usuarios.route("/usuarios/<id>/", methods=["DELETE"])
def delete_usuarios(id):
    u = UsuariosModel.objects(id=id).first()
    u.delete()
    return jsonify({"message": "Usuario deletando com sucesso!"})