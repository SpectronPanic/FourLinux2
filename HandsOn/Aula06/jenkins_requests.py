#!/usr/bin/python

import jenkins
from lxml import etree
import yaml

class JenkinsAPI:
    def __init__(self):
        try:
            with open("temp.xml", "r") as f:
                xml = f.read()
            self.server = jenkins.Jenkins("http://192.168.201.127:8080")
            print self.server.get_version()
        except Exception as e:
            print "Falhou ao conectart com o servidor: ",e


    def create_job(self,nome):
        try:
            xml = self._generate_job_steps()
            self.server.create_job(nome,xml)
            print "Job criada com sucesso"
        except Exception as e:
            print "Falhou ao criar job: ",e

    def _generate_job_steps(self):
        # lendo arquivo XML
        with open("Templates/base.xml") as f:
            base_xml = f.read()
        # convertendo em objeto do ElementTree
        base_xml = etree.XML(base_xml)
        # procura por elemento builders dentro do XML
        for element in base_xml.findall("builders"):
            builders = element
        # le arquivo no formato YAML e converte pra dicioario
        with open("Templates/deploy_wordpress.yml","r") as f:
            arquivo_yaml = yaml.load(f.read())
        # pega a lista de comandos do yaml e gera o xml
        for c in arquivo_yaml.get("command"):
            # cria Step do tipo Shell
            step = etree.Element("hudson.tasks.Shell")
            # cria comando do Step do Jenkins
            command = etree.Element("command")
            # adiciona o comando do arquivo yaml dentro da tag command do xml
            command.text = c
            # adiciona o elemento como filho do elento hudson.tasks.Shell
            step.append(command)
            # adiciona o elemento hudson.tasks.Shell como filho do elemento builders
            builders.append(step)
        return etree.tostring(base_xml)

    def execute_job(self,nome):
        try:
            self.server.build_job(nome)
            print "Job criado com sucesso"
        except Exception as e:
            print "Falhou ao executar job", e





if __name__ == '__main__':
    j = JenkinsAPI()
    j.create_job("Harry_Python_JOB4_")
#    j.create_job("Harry_Python_JOB4")
    #j.generate_job_steps()
