#!/usr/bin/python
import requests
import json

lista = [
    "Joao Mendes",
    "Joaquim Seferino",
    "Nicolas Farias",
    "Rodrigo Marcelo",
    "Maria Joana",
    "Abdias Moraes",
    "Eliana Sorriso",
    "Hellen Gonzaga",
    "Humberto Sales",
    "Benedito da Silva"
]

for l in lista:
    usuario = l.lower().replace(" ",".")
    email = usuario+"@dexter.com.br"
    dados = {"nome":usuario,"email":email}
    cabecalho = {"Content-Type":"application/json"}
    response = requests.post("http://localhost:5000/usuarios/",
                             data=json.dumps(dados),headers=cabecalho)
    print response.content