#!/usr/bin/python

import requests
import json

class GitlabAPI:
    def __init__(self):
        self.token = "y5BAhu9Tdmi84XjSY2yR"

    def _make_get(self,recurso,dados=""):
        servidor = "http://192.168.201.123/api/v3/%s%s?private_token=%s" % \
                    (recurso,dados, self.token)
        try:
            response = requests.get(servidor)
            return response


        except Exception as e:
            print "Falhou ao fazer request:", e

        print self.servidor

    def _make_post(self,recurso,dados):
        servidor = "http://192.168.201.123/api/v3/%s?private_token=%s"%\
                   (recurso,self.token)
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
            print "Projeto criado com sucesso!"
        else:
            print "Falhou ao criar o projeto"
            print response.content


    def _get_user(self,user):
        response = self._make_get("users")
        response = json.loads(response.content)
        usuario = [u for u in response if u.get("username") == user][0]
        return usuario

    def _get_project(self, name):
        response = self._make_get("projects")
        response = json.loads(response.content)
        project = [u for u in response if u.get("name") == name][0]
        return project


    def add_project_member(self,user,project):
        user_id = self._get_user(user).get("id")
        project_id = self._get_project(project).get("id")
        data = {"id":project_id,"user_id":user_id,"access_level":40}
        response = self._make_post("projects/%s/members"%project_id,data)
        if response.status_code == 201:
            print "Membro adicionado ao projeto"
        else:
            print "Falhou ao adicionar"
            print response.status_code


    def add_project_hook(self, url, project):
        project_id = self._get_project(project).get("id")
        data = {"url": url, "push_events": True}
        response = self._make_post("projects/%s/hooks" % project_id, data)
        if response.status_code == 201:
            print "Web hook add com sucesso MAN"
        else:
            print "Falhou a hook MAN"
            print response.status_code



if __name__ == '__main__':
    gitlab = GitlabAPI()
    novo  ={"name":"vandy",
            "username":"vandy",
            "email":"vandy@dexter.com.br",
            "password":"4linux123"}
    #gitlab.create_user(novo)
    #gitlab.create_project("XupisS2Osasco")
    #gitlab._get_user("vandy")
    #gitlab.add_project_member("vandy","Kamehameha")
    #gitlab.add_project_hook("http://jenkins.com.br","Kamehameha")
    gitlab.add_project_hook("http://jenkins.com.br","Kamehameha")