#!/usr/bin/python
#
# arquivo: DeployTool.py
import argparse
import yaml
from Modulos.DockerAPI import DockerAPI
from Modulos.GitlabAPI import GitlabAPI
from Modulos.JenkinsAPI import JenkinsAPI

class DeployTool:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-i",help="Indica o arquivo de deploy")
        self.args = self.parser.parse_args()

    def _yaml_to_dict(self):
        with open("%s"%self.args.i, 'r') as f:
            self.dexterbook = yaml.load(f.read())

    def _make_gitlab(self):
        gitlab = GitlabAPI()
        #se o projeto nao existe
        if not gitlab._get_project(self.dexterbook.get("name")):
            gitlab.create_project(self.dexterbook.get("name"))
        # percorre lista de desenvolvedores no arquivo yaml
        for d in self.dexterbook.get("developers"):
            user = gitlab._get_user(d)
            if not user:
                dados = {"name": d.split("@")[0],
                         "username":d.split("@")[0],
                         "email": d,
                         "password": "4linux123"}
                # Cria usuario
                gitlab.create_user(dados)
            #adiciona usuario como membro do projeto
            gitlab.add_project_member(d, self.dexterbook.get("name"))
        #adiciona webhook ao projeto
        gitlab.add_project_hook(self.dexterbook.get("webhook"),
        self.dexterbook.get("name"))
        return gitlab.get_project_repo(self.dexterbook.get("name"))


    def _make_jenkins(self,repo):
        jenkins = JenkinsAPI()
        try:
            jenkins.create_job(self.dexterbook.get("name"),
                               repo,
                               self.dexterbook.get("deploy-sequence"))
        except Exception as e:
            print "Falhou ao criar job: ",e


    def _make_docker(self):
        print "Criando container %s" % self.dexterbook.get("name")
        docker = DockerAPI()
        res = docker.get_container(self.dexterbook.get("name"))
        if res:
            print "Container ja existe"
            docker.start_container(res.get("Id"))
        else:
            res = docker.create_container(self.dexterbook.get("name"))
            docker.start_container(res)

        print "Endereco: ", docker.get_container_address(self.dexterbook.get("name"))




    def make(self):
        self._yaml_to_dict()
        self._make_docker()
        repo = self._make_gitlab()
        self._make_jenkins(repo)



if __name__ == "__main__":
    dt = DeployTool()
    dt.make()
    
