#!/usr/bin/python

from Modules.GitlabModule import GitlabModule
from Modules.JenkinsModule import JenkinsModule
from Modules.DockerModule import DockerModule
import json

class DeployTool:
    def __init__(self):
        pass
    
    def make(self):    
        try:  
            jm = JenkinsModule()
            gm = GitlabModule()
            dm = DockerModule()
            with open("application.json",'r') as f:
                j = json.loads(f.read())       
            gm.createProject({"name":j.get("application")})
            for d in j.get("developers"):
                gm.createUser(d.split("@")[0],d)
                gm.addProjectMember(j.get("application"),d)
            gm.addWebHook(j.get("application"),"http://jenkins.dexter.com.br:8080/gitlab/build_now")
            jm.createJob(j.get("application"),gm.getProjectRepo(j.get("application")))
            dm.createContainer(j.get("application"))
            dm.startContainer(j.get("application"))
        except Exception as e:
            print "Falhou %s"%e

if __name__ == '__main__':
    dt = DeployTool()
    dt.make()
