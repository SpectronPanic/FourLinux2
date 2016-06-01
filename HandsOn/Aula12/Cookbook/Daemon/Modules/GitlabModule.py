#!/usr/bin/python

import requests
import ConfigParser
import os
import json

class GitlabModule:
    def __init__(self):
        try:
            cf = ConfigParser.ConfigParser()
            cf.read(os.path.dirname(os.path.abspath(__file__))+"/../config.cfg")
            self.server = cf.get("gitlab","server")
            self.token = cf.get("gitlab","token")
        except Exception as e:
            print "Falhou ao conectar com o gitlab %s"%e

    def make_post(self,url,data):
        response = requests.post(
                                "http://%s/api/v3/%s?private_token=%s" \
                                %(self.server,url,self.token),
                                data=data)
        return response

    def make_get(self,url,data):
        response = requests.get(
                                "http://%s/api/v3/%s/%s?private_token=%s" \
                                %(self.server,url,data,self.token))
        return response

    def createUser(self,name,email):
        try:
            response = self.make_post(
                                        "users",
                                        {"name":name,
                                       "username":name,
                                       "email":email,
                                       "password":"4linux123",
                                       "confirm":False})
            if response.status_code == 201:
                print "Usuario criado com sucesso"
            else:
                print "Falhou ao criar usuario %s"%response.text
        except Exception as e:
            print "Falhou ao criar usuario %s"%e

    def createProject(self,application):
        try:
            response = self.make_post("projects",application)
            if response.status_code == 201:
                print "Projeto criado com sucesso"
            else:
                print "Falhou ao criar projeto %s"%response.text
        except Exception as e:
            print "Falhou ao criar projeto %s"%e

    def addProjectMember(self,project,member):
        try:
            response = self.make_get("projects","/all")
            project_id = min([ r.get("id") for r in response.json() if r.get("name") == project ])
            response = self.make_get("users","")
            user_id = min([ r.get("id") for r in response.json() if r.get("email") == member ])

            response = self.make_post(
                                    "projects/%s/members"%project_id,         
                                   {"id":project_id,
                                    "user_id":user_id,
                                    "access_level":30})            
            if response.status_code == 201:
                print "Membro adicionado ao projeto"
            else:
                print "Falhou ao adicionar membro %s"%response.text
        except Exception as e:
            print "Falhou ao adicionar membro ao projeto %s"%e
    
    def addWebHook(self,project,url):
        try:
            response = self.make_get("projects","/all")
            project_id = min([ r.get("id") for r in response.json() if r.get("name") == project ])
            response = self.make_post("projects/%s/hooks"%project_id,
                                      {"url":url,"push_events":True})
            if response.status_code == 201: 
                print "Hook adicionada com sucesso"
            else:
                print "Falhou %s"%response.text
        except Exception as e:
            print "Falhou ao adicionar webhook %s"%e

    def getProjectRepo(self,project):
        try:
            response = self.make_get("projects","/all")
            project = min([ r.get("ssh_url_to_repo") for r in response.json() if r.get("name") == project ])
            if project:
                return str(project)
            else:
                print "Projeto nao existe"
        except Exception as e:
            print "Falhou ao adicionar webhook %s"%e

if __name__ == '__main__':
    g = GitlabModule()
    #g.createUser('alisson','alisson@dexter.com.br')
    #g.createProject('Terminus')
    #g.addProjectMember('Terminus','alisson@dexter.com.br')
    #g.addWebHook('Terminus',"http://teste.com.br")
