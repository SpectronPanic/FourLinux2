#!/usr/bin/python

from docker import Client
import json
from Modules.SSHModule import SSHModule

class DockerModule(SSHModule):
    def __init__(self):
        try:
            self.cli = Client(base_url='tcp://192.168.0.2:2376')
            SSHModule.__init__(self)
        except Exception as e:
            print "Erro: %s" % e

    def startContainer(self, container):
        try:
            container = [ c.get("Id") for c in self.cli.containers(all=True)
                          if min(c.get("Names")) == "/"+container ]
            self.cli.start(container=min(container))
            print "[+] Endereco do Container %s"%(
                                                    self.cli.inspect_container(min(container)) \
                                                    .get("NetworkSettings") \
                                                    .get("Networks") \
                                                    .get("bridge") \
                                                    .get("IPAddress"))
        except Exception as e:
            print "Falhou ao iniciar o container %s"%e
            raise

    def createContainer(self, name):
        try:
            container = self.cli.create_container(
                                        image="ubuntu",
                                        command="/bin/bash",
                                        detach=True,
                                        name=name,
                                        tty=True,
                                        stdin_open=True)
        except Exception as e:
            print "Falhou ao criar container %s"%e
            raise

    def exec_command(self,container,cmd):
        try:
            print "[+] Running command: %s"%cmd
            command = "docker exec %s %s"%(container,cmd)
            print self.execCommand(command)
        except Exception as e:
            print "Falhou ao executar comando %s"%e
