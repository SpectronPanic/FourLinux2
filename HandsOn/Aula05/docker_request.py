#!/usr/bin/python

from docker import Client

class DockerAPI:
    def __init__(self):
        self.docker_client = Client("tcp://192.168.201.124:2376")

    def list_container(self):
        for c in self.docker_client.containers():
            print c.get("Names")



    def create_containers(self,nome,imagem):
        res = self.docker_client.create_container(name=nome,
                                                  image=imagem,
                                                  command="/bin/bas",
                                                  tty=True,
                                                  stdin_open=True,
                                                  detach=True)
        if res:
            return res
        else:
            print "falhou ao criar o container %s"%res



    def start_container(self,id):
        try:
            self.docker_client.start(container=id)
            print "Container executado"
        except Exception as e:
            print "Falhou ao iniciar o container %s"%e


    def inspect_container(self,id):
        try:
            res = self.docker_client.inspect_container(id)
            return res
        except Exception as e:
            print "Falhou ao busca informacoes do container", e


    def remove_container(self,id):
        try:
            self.docker_client.stop(id)
            self.docker_client.remove_container(id)
            print "Container removido com sucesso"
        except Exception as e:
            print "Falhou ao deletar o container ",e


    def get_container(self,nome):
        try:
            todos = self.docker_client.containers(all=True)
            nome = "/"+nome
            container = [c for c in todos if nome in c.get("Names")] [0]
            return container
        except Exception as e:
            print "Falhou ao buscar o container"


    def exec_command(self,id,cmd):
        try:
            create_id = self.docker_client.exec_create(id,cmd)
            print "Executando comando %s"%cmd
            print self.docker_client.exec_start(create_id)
        except Exception as e:
            print "Falhou ao executar o comando", e


if __name__ == '__main__':
    da = DockerAPI()
    #container_id = da.create_containers("carapicuiba_s2_Osasco_rs","centos")
    #da.start_container(container_id)
    #print da.inspect_container(container_id)
    #da.list_container()
    #da.remove_container(container_id)
    container_id = da.get_container("vandy").get("Id")
    da.exec_command(container_id,"apt-get update")
    da.exec_command(container_id, "apt-get install nginx -y")
    # da.remove_container(container_id)
