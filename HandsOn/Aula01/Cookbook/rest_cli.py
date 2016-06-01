#!/usr/bin/python

import requests
import json
import sys

# Listando todos os usuarios cadastrados na base da API
def listar_usuarios():
    response = json.loads(requests.get("http://127.0.0.1:5000/usuarios/")._content)    
    for r in response.get("usuarios"):
        print r["id"],r["nome"],r['email']

# Atualizando informacoes de um usuario
def atualizar_usuario(novos_dados):
    novos_dados = json.dumps(dados)
    content_type = {"Content-Type":"application/json"}
    response = json.loads(
                        requests.put("http://127.0.0.1:5000/usuarios/%s/"%usuario_id,
                        data=novos_dados,
                        headers=content_type        
            
                    )._content)
    print response

# Inserindo novo usuario
def inserir_usuario(dados):
    content_type = {"Content-Type":"application/json"}
    email = dados.get("nome").replace(" ",".").lower()
    email += "@dexter.com.br"
    dados["email"] = email
    dados = json.dumps(dados)
    response = json.loads(
                        requests.post("http://127.0.0.1:5000/usuarios/",
                        data=dados,
                        headers=content_type)._content
                    )
    print response


def buscar_usuario(email):
    response = json.loads(
                        requests.get("http://127.0.0.1:5000/usuarios/")._content
                     )
    usuario_id = min(
                        [ u.get("id") for u in response.get("usuarios") \
                          if u.get("email") == email ]
                    )

    response = json.loads(
                        requests.get("http://127.0.0.1:5000/usuarios/%s/"%usuario_id)._content
                    )

    return response.get("id")

def deletar_usuario(id):
    response = json.loads(requests.delete("http://127.0.0.1:5000/usuarios/%s/"%id)._content)
    print response



if __name__ == '__main__':
    listar_usuarios()
    #inserir_usuario({"nome":"Bruce Wayne"})
    #id = buscar_usuario("bruce.wayne@dexter.com.br")
    #deletar_usuario(id)



