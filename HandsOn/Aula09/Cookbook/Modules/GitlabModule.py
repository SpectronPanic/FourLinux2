#!/usr/bin/python

import ConfigParser
import json
import requests
import os

class GitlabModule:
    def __init__(self):
        try:
            cf = ConfigParser.ConfigParser()
            cf.read(os.path.dirname(os.path.abspath(__file__))+"/../config.cfg")
            self.server = cf.get("gitlab","server")
            self.token = cf.get("gitlab","token")
        except Exception as e:
            print "Falhou no construtor ",e


    def make_post(self,url,data):
        try:
            response = requests.post(
                                     "http://%s/api/v3/%s?private_token=%s"%(self.server,url,self.token),
                                     data=data)
            return response
        except Exception as e:
            print "Falhou ao realizar o post ",e

    def make_get(self,url,data=""):
        try:
            response = requests.get(
                                     "http://%s/api/v3/%s%s?private_token=%s"%(self.server,url,data,self.token)
                                    )
            return response
        except Exception as e:
            print "Falhou ao realizar o get request ",e


    def createUser(self,name,email):
        try:
            resource = "users"
            data = {"name":name,
                    "username":name,
                    "email":email,
                    "password":"4linux123",
                    "confirm":False}

            response = self.make_post(resource,data)
            if response.status_code == 201:
                print "Usuario Criado com Sucesso"
            else:
                print "Status Code: ",response.status_code
                print "Falhou ao criar usuario: ",response.text
        except Exception as e:
            print "Falhou ao criar usuario: ",e

    def createProject(self,application):
        try:
            resource = "projects"
            data = {"name":application}
            response = self.make_post(resource,data)
            if response.status_code == 201:
                print "Projeto criado com sucesso"
            else:
                print "Status Code: ",response.status_code
                print "Falhou ao criar projeto: ",response.text            
        except Exception as e:
            print "Falhou ao criar projeto: ",e

    def addProjectMember(self,project,member):
        try:
            response = self.make_get("projects","/all")
            project_id = [ r.get("id") for r in response.json() if r.get("name") == project ][0]
            
            response = self.make_get("users")
            user_id = [ r.get("id") for r in response.json() if r.get("email") == member ][0]

            data = {"id":project_id,
                    "user_id":user_id,
                    "access_level":30}

            response = self.make_post("projects/%s/members"%(project_id),data)
            if response.status_code == 201:
                print "Membro foi adicionado ao projeto com sucesso"
            else:
                print "Status Code: ",response.status_code
                print "Falhou ao adicionar membro ao projeto: ",response.text

        except Exception as e:
            print "Falhou ao adicionar membro ao projeto ",e    

    def addWebHook(self,project,url):
        try:
            response = self.make_get("projects","/all")
            project_id = [ r.get("id") for r in response.json() if r.get("name") == project ][0]

            data = {"url":url,"push_events":True}
            response = self.make_post("projects/%s/hooks"%(project_id),data)
            
            if response.status_code == 201:
                print "WebHook foi adicionada com Sucesso!"
            else:
                print "Status Code: ",response.status_code
                print "Falhou ao adicionar WebHook: ",response.text
        
        except Exception as e:
            print "Falhou ao adicionar webhook: ",e

    def getProjectRepo(self,project):
        try:
            response = self.make_get("projects","/all")
            repo_url = [ r.get("ssh_url_to_repo") for r in response.json() if r.get("name") == project ][0]
            if repo_url:
                return str(repo_url)
            
        except Exception as e:
            print "Falhou ao buscar url do repositorio: ",e

if __name__ == '__main__':
    g = GitlabModule()
#    g.createUser("alisson","alisson@dexter.com.br")
#    g.addProjectMember("RepoRest","alisson@dexter.com.br")
#    g.addWebHook("RepoRest","http://webhook.teste.com.br")
#    g.getProjectRepo("RepoRestzxczxczxc")

