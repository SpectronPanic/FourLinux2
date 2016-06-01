#!/usr/bin/python

import jenkins

from lxml import etree

class JenkinsManager:
    def __init__(self):
        try:
            self.server = jenkins.Jenkins("http://jenkins.dexter.com.br:8080")
            self.server.get_version()
        except Exception as e:
            print "Falhou ao conectar com o jenkins ",e

    def createJob(self):
        try:
            with open("job_template.xml",'r') as f:
                template = f.read() \
                           .replace("repositorio_do_gitlab","meu_projeto_do_gitlab")

            print type(template)
            root = etree.XML(template)
            for b in root.findall("builders"):
                builder = b
            shell_step = etree.Element("hudson.tasks.Shell")            
            comando = etree.Element("command")
            comando.text = "echo comando1"
            shell_step.append(comando)
            builder.append(shell_step)

            shell_step = etree.Element("hudson.tasks.Shell")            
            comando = etree.Element("command")
            comando.text = "echo comando2"
            shell_step.append(comando)
            builder.append(shell_step)
            shell_step = etree.Element("hudson.tasks.Shell")            
            comando = etree.Element("command")
            comando.text = "echo comando3"
            shell_step.append(comando)
            builder.append(shell_step)
            #print self.server.create_job("Job-Template4",etree.tostring(root))
        except Exception as e:
            print "Falhou ao criar a job ",e

    def buildJob(self):
        try:
            print self.server.build_job("Job-Template4",{"mensagem":"executando job via python"})
        except Exception as e:
            print "Falhou ao executar a job ",e

if __name__ == '__main__':
    j = JenkinsManager()
#    j.createJob()
    j.buildJob()
