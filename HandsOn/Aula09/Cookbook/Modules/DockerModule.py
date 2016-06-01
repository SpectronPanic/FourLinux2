#!/usr/bin/python

from docker import Client
from Modules.SSHModule import SSHModule

class DockerModule(SSHModule):
    def __init__(self):
        try:
            self.cli = Client(base_url="tcp://192.168.0.2:2376")
            SSHModule.__init__(self)
        except Exception as e:
            print "Falhou ao conectar com o servidor ",e

    def createContainer(self,name):
        try:
            print "[+] Criando o container ",name
            container = self.cli.create_container(
                                                  name=name,
                                                  image="ubuntu",
                                                  command="/bin/bash",
                                                  tty=True,
                                                  detach=True,
                                                  stdin_open=True)
            self.cli.start(container=container.get("Id"))
            print "[+] Container criado e sendo executado "
        except Exception as e:
            print "Falhou ao criar o container",e


    def getIPContainer(self,name):
        try:
            container_id = [ c.get("Id") for c in self.cli.container(all=True) if c.get("Names") == "/"+name ][0]
            container = self.cli.inspect_container(container_id)
            print "IP Address: ",container.get("NetworkSettings").get("Networks").get("bridge").get("IPAddress")
        except Exception as e:
            print "Falhou ao buscar informacoes do container: ",e


    def exec_command(self,container,cmd):
        try:
            print "[+] Running command: ",cmd
            command = "docker exec %s %s"%(container,cmd)
            print self.execCommand(command)
        except Exception as e:
            print "Falhou ao executar o comando: ",e
