#!/usr/bin/python

from flask import Flask
from flask.ext.mongoengine import MongoEngine
from datetime import datetime

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"db":"dexter-api"}

db = MongoEngine(app)

class Usuarios(db.Document):
    nome = db.StringField()
    email = db.StringField(unique=True)
    data_cadastro = db.DateTimeField(defaults=datetime.now())


class Grupos(db.Document):
    nome = db.StringField(unique=True)
    integrantes = db.ListField()

if __name__== '__main__':
    u = Usuarios()
    u.nome = "Vandy Rodrigues"
    u.email = "vandyrodrigues1@gmail.com"
    u.save()