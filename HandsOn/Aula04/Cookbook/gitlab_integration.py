#!/usr/bin/python

import requests
import json

token = "y5BAhu9Tdmi84XjSY2yR"
recurso = "users"
url = "http://gitlab.dexter.com.br/api/v3/%s?private_token=%s"%(recurso,token)

def createuser(dados):
    token = "y5BAhu9Tdmi84XjSY2yR"
    recurso = "users"
    url = "http://gitlab.dexter.com.br/api/v3/%s?private_token=%s"%(recurso,token)
    response = requests.post(url,data=dados).status_code
    print "Status Code: ",response               
    if response == 201:
        print "Usuario criado com sucesso"
    else:
        print "Falhou ao criar usuario"

def getusers():
    token = "y5BAhu9Tdmi84XjSY2yR"
    recurso = "users"
    url = "http://gitlab.dexter.com.br/api/v3/%s?private_token=%s"%(recurso,token)
    response = json.loads(
                        requests.get(url)._content
                    )
    return response

def getprojects():
    token = "y5BAhu9Tdmi84XjSY2yR"
    recurso = "projects"
    url = "http://gitlab.dexter.com.br/api/v3/%s?private_token=%s"%(recurso,token)
    response = json.loads(
                        requests.get(url)._content
                    )
    return response

def createprojects(dados):
    token = "y5BAhu9Tdmi84XjSY2yR"
    recurso = "projects"
    url = "http://gitlab.dexter.com.br/api/v3/%s?private_token=%s"%(recurso,token)
    response = json.loads(
                        requests.post(url,data=dados)._content
                    )
    print response

def addprojectsmember(project_id,user_id):
    token = "y5BAhu9Tdmi84XjSY2yR"
    url = "http://gitlab.dexter.com.br/api/v3/projects/%s/members?private_token=%s"%(project_id,token)
    
    membro = {"project_id":project_id,"user_id":user_id,"access_level":30}
    
    response = json.loads(
                        requests.post(url,data=membro)._content
                    )
    print response

def addprojectshook(project_id,hook_url):
    token = "y5BAhu9Tdmi84XjSY2yR"
    url = "http://gitlab.dexter.com.br/api/v3/projects/%s/hooks?private_token=%s"%(project_id,token)
    
    hook = {"url":hook_url,"push_events":True}
    
    response = json.loads(
                        requests.post(url,data=hook)._content
                    )
    print response



if __name__ == '__main__':    
    user_id = [ u for u in getusers() if u.get("email") == "bruce.wayne@dexter.com.br" ]
#    createprojects({"name":"Projeto_API"})
    project_id = [ p for p in getprojects() if p.get("name") == "Projeto_API"]
    addprojectshook(project_id[0].get("id"),"http://go.cd/")



