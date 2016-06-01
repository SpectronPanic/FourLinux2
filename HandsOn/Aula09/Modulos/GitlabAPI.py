#!/usr/bin/python

import requests
import json
import ConfigParser

class GitlabAPI:
    def __init__(self):
        try:
            config = ConfigParser.ConfigParser()
            config.read("deploy.cfg")
            self.server = config.get("gitlab","server")
            self.token = config.get("gitlab","token")
        except Exception as e:
            print "Falhou ao conectar com o gitlab: ",e

    def _make_get(self,recurso,dados=""):
        servidor = "http://%s/api/v3/%s%s?private_token=%s"%(self.server,recurso,dados,self.token)
        try:
            response = requests.get(servidor)
            return response
        except Exception as e:
            print "Falhou ao fazer request: ",e
   
    def _make_post(self,recurso,dados):
        servidor = "http://%s/api/v3/%s?private_token=%s"%(self.server, recurso,self.token)
        try:
            content_type = {"Content-Type":"application/json"}
            dados = json.dumps(dados)
            response = requests.post(servidor,data=dados,headers=content_type)
            return response
        except Exception as e:
            print "Falhou ao fazer o post: ",e

    def create_user(self,dados):
        response = self._make_post("users",dados)
        if response.status_code == 201:
            print "Usuario criado com sucesso"
        else:
            print response.content
            print "Falhou ao criar usuario"

    def create_project(self,project):
        project = {"name":project}
        response = self._make_post("projects",project)
        if response.status_code == 201:
            print "Projeto criado com sucesso"
        else:
            print "Falhou ao criar o projeto"
            print response.content

    def _get_user(self,user):
        response = self._make_get("users")  
        response = json.loads(response.content)
        usuario = [ u for u in response if u.get("email") == user ]
        if usuario:
            return usuario[0]
        else:
            return False

    def _get_project(self,name):
        response = self._make_get("projects")  
        response = json.loads(response.content)
        project = [ u for u in response if u.get("name") == name ]
        if project:
            return project[0]
        else:
            return False

    def add_project_member(self,user,project):
        user_id = self._get_user(user).get("id")
        project_id = self._get_project(project).get("id")
        data = {"id":project_id,"user_id":user_id,"access_level":30}
        response = self._make_post("projects/%s/members"%project_id,data)
        if response.status_code == 201:
            print "Membro adicionado ao projeto"
        else:
            print "Falhou ao adicionar "
            print response.content

    def get_project_repo(self,name):
        project_repo = self._get_project(name).get("ssh_url_to_repo")
        return project_repo




    def add_project_hook(self,url,project):
        project_id = self._get_project(project).get("id")
        data = {"url":url,"push_events":True}
        response = self._make_post("projects/%s/hooks"%project_id,data)
        if response.status_code == 201:
            print "Webhook adicionada com sucesso"
        else:
            print "Falhou ao adicionar webhook"
            print response.content

if __name__ == '__main__':
    gitlab = GitlabAPI()
    novo = {"name":"Goku",
            "username":"goku",
            "email":"goku@dexter.com.br",
            "password":"4linux123"}
    #gitlab.create_user(novo)
    #gitlab.create_project("Kamehameha")
    #gitlab.add_project_member("goku","Kamehameha")
    gitlab.add_project_hook("http://jenkins.com.br","Kamehameha")






