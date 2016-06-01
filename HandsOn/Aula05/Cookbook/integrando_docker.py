#!/usr/bin/python


from docker import Client

class DockerManager:
    def __init__(self):
        try:
            self.cli = Client(base_url="tcp://192.168.0.2:2376")            
        except Exception as e:
            print "Falhou %s"%e

    def createContainer(self,nome,hn):
        try:
            container = self.cli.create_container(name=nome,hostname=hn,image="debian",
                                            detach=True,stdin_open=True,tty=True)
            self.cli.start(container=container.get("Id"))
            return container
        except Exception as e:
            print "Falhou ao criar o container: ",e

    def listContainers(self):
        try:
            for c in self.cli.containers(all=True):
                rede = c.get("NetworkSettings").get("Networks").keys()[0]
                ip = c.get("NetworkSettings").get("Networks").get(rede).get("IPAddress")
                print c.get("Names")[0]," rede: ",rede,"IP: ",ip,"Status: ",c.get("Status")
                print "Removendo o container ",c.get("Names")
        except Exception as e:
            print "Falhou ao listar os containers: ",e

    def inspectContainer(self,container_id):
        try:
            container = self.cli.inspect_container(container_id)
            print container
        except Exception as e:
            print "Falhou ao criar o container: ",e

    def execContainer(self,container_id,command):
        try:
            exec_id = self.cli.exec_create(container_id,command)
            print exec_id
            log = self.cli.exec_start(exec_id.get("Id"))
            print log
        except Exception as e:
            print "Falhou ao criar o container: ",e

if __name__ == '__main__':
    d = DockerManager()
    #container = d.createContainer("ContainerAPT3","apt.dexter.com.br")
    d.listContainers()
    #d.inspectContainer(container.get("Id"))
    #print container.get("Id")
    #d.execContainer("d5142366c3e8d5489fc88a4c8a0d2972e1dbe7b19fc3b35f5315d4339b90e139","apt-get install apache2 -y")

    
