#!/usr/bin/python


import argparse
import yaml
from modulos.dockerapi import DockerAPI


class DeployTool:
    def __init__(self):
        self.parse = argparse.ArgumentParser()
        self.parse.add_argument('-i', help='Indica o arquivo de deploy')
        self.args = self.parse.parse_args()

    def _yaml_to_dict(self):
        with open('%s' % self.args.i, 'r') as f:
            self.dexterbook = yaml.load(f.read())

    def make(self):
        self._yaml_to_dict()
        print 'Criando container %s' % self.dexterbook.get('name')
        docker = DockerAPI()
        res = docker.get_container(self.dexterbook.get("name"))
        if res:
            print "Container ja existe"
            docker.start_container(res.get("Id"))
        else:
            res = docker.create_container(self.dexterbook.get("name"))
            docker.start_container(res)

        print "Endereco: ", docker.get_container_address \
            (self.dexterbook.get("name"))

        print 'Fazendo deploy da aplicacao %s' % self.dexterbook.get('name')
        for c in self.dexterbook.get('deploy-sequence'):
            print 'Executando o comando %s' % c
            docker._exec(self.dexterbook.get('name'), c)

if __name__ == '__main__':
    dt = DeployTool()
    dt.make()