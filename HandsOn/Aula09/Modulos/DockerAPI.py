#!/usr/bin/python

from docker import Client
import ConfigParser
import json
from Modulos.SSHAPI import SSHAPI

class DockerAPI(SSHAPI):
    def __init__(self):
        try:
            SSHAPI.__init__(self)
            config = ConfigParser.ConfigParser()
            config.read("deploy.cfg")
            self.docker_client = Client("tcp://%s:2376"%config.get("docker","server"))
        except Exception as e:
            print "Falhou ao conectar com o Docker: ",e

    def list_containers(self):
        for c in self.docker_client.containers():
            print c.get("Names")

    def create_container(self,nome,imagem="ubuntu"):
        res = self.docker_client.create_container(name=nome,
                                                  image=imagem,
                                                  command="/bin/bash",
                                                  tty=True,
                                                  stdin_open=True,
                                                  detach=True)
        if res:
            return res
        else:
            print "Falhou ao criar o container ",res

    def start_container(self,id):
        try:
            self.docker_client.start(container=id)
            print "Container executado"
        except Exception as e:
            print "Falhou ao iniciar o container ",e

    def inspect_container(self,id):
        try:
            res = self.docker_client.inspect_container(id)
            return res
        except Exception as e:
            print "Falhou ao buscar informacoes do container ",e

    def remove_container(self,id):
        try:
            self.docker_client.stop(id)
            self.docker_client.remove_container(id)
            print "Container removido com sucesso"
        except Exception as e:
            print "Falhou ao apagar o container ",e

    def get_container(self,nome):
        try:
            todos = self.docker_client.containers(all=True)
            nome = "/"+nome
            container = [ c for c in todos if nome in c.get("Names") ][0]
            return container
        except Exception as e:
            print "Falhou ao buscar container ",e

    def get_container_address(self,nome):
        address = self.get_container(nome)
        address = address.get("NetworkSettings").get("Networks") \
                         .get("bridge").get("IPAddress")
        return address

    def exec_command(self,id,cmd):
        try:
            create_id = self.docker_client.exec_create(id,cmd)
            print "Executando comando ",cmd
            print self.docker_client.exec_start(create_id)
        except Exception as e:
            print "Falhou ao executar o comando ",e

    def _exec(self,container,cmd):
        c = "docker exec %s %s"%(container,cmd)
        self.exec_ssh_command(c)


if __name__ == '__main__':
    da = DockerAPI()
    #container_id = da.create_container("new1_edmar","ubuntu")
    #da.start_container(container_id)
    #print da.inspect_container(container_id)
    #da.list_containers()
    container_id = da.get_container("alisson").get("Id")
    da.exec_command(container_id,"apt-get update")
    da.exec_command(container_id,"apt-get install nginx -y")
    #da.remove_container(container_id)
    




