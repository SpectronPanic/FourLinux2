#!/usr/bin/python

from flask import Blueprint,jsonify

usuarios = Blueprint("usuarios",__name__)

@usuarios.route("/usuarios/",methods=["GET"])
def index_usuarios():
    data = {"message":"Aqui serao listados todos os usuarios cadastrados"}
    return jsonify(data)

@usuarios.route("/usuarios/",methods=["POST"])
def inserir_usuarios():
    data = {"message":"Aqui serao cadastrados os novos usuarios"}
    return jsonify(data)

@usuarios.route("/usuarios/<int:id>/",methods=["GET"])
def select_usuarios(id):
    data = {"message":"Mostrando usuario cujo o ID e igual a %s"%id}
    return jsonify(data)

@usuarios.route("/usuarios/<int:id>/",methods=["PUT"])
def update_usuarios(id):
    data = {"message":"Atualizando o usuario cujo o ID e igual a %s"%id}
    return jsonify(data)

@usuarios.route("/usuarios/<int:id>/",methods=["DELETE"])
def delete_usuarios(id):
    data = {"message":"Deletando usuario cujo o ID e igual a %s"%id}
    return jsonify(data)
