#!/usr/bin/python

from flask import Blueprint,jsonify
from Model import Grupos
import json

grupos = Blueprint("grupos",__name__)

@grupos.route("/grupos/")
def list_grupos():
    lista_grupos = json.loads(Grupos.objects.to_json())
    data = {"grupos":lista_grupos}
    return jsonify(data)
    
@grupos.route("/grupos/",methods=["POST"])
def inserir_grupos():
    data = {"message":"Aqui serao cadastrados os novos grupos"}
    return jsonify(data)

@grupos.route("/grupos/<int:id>/",methods=["GET"])
def select_grupos(id):
    data = {"message":"Mostrando grupo cujo o ID e igual a %s"%id}
    return jsonify(data)

@grupos.route("/grupos/<int:id>/",methods=["PUT"])
def update_grupos(id):
    data = {"message":"Atualizando o grupo cujo o ID e igual a %s"%id}
    return jsonify(data)

@grupos.route("/grupos/<int:id>/",methods=["DELETE"])
def delete_grupos(id):
    data = {"message":"Deletando grupo cujo o ID e igual a %s"%id}
    return jsonify(data)
