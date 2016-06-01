#!/usr/bin/python

import ConfigParser
import os
import jenkins
from lxml import etree
import json

class JenkinsModule:
    def __init__(self):
        try:
            cf = ConfigParser.ConfigParser()
            cf.read(os.path.dirname(os.path.abspath(__file__))+"/../config.cfg")
            self.server = jenkins.Jenkins(cf.get("jenkins","server"))
            print "Versao do Jenkins: ",self.server.get_version()
        except Exception as e:
            print "Falhou ao conectar com o servidor do Jenkins: ",e

    def createJob(self,application,repo):
        try:
            print application
            print repo

            job_dir = os.path.dirname(os.path.abspath(__file__))+"/../Templates/job.xml"
            with open(job_dir,'r') as f:
                job_xml = f.read().replace("REPO",repo)
            
            xml = etree.tostring(self.generateJobSteps(job_xml,application))
            print "[+] Criando Job"
            self.server.create_job(application,xml)
            print "[+] Job criada com sucesso"
        except Exception as e:
            print "Falhou ao criar job: ",e

    def generateJobSteps(self,xml,application):
        try:
            application_file = os.path.dirname(os.path.abspath(__file__))+"/../application.json"
            with open(application_file,'r') as f:
                application_json = json.loads(f.read())

            root = etree.XML(xml)
            for b in root.findall("builders"):
                builder = b
            print "[+] Gerando Job Steps"
            for c in application_json.get("deploy-sequence").get("commands"):
                command = etree.Element("command")
                command.text = "ssh forlinux@192.168.0.2 \"docker exec %s bash -c '%s'\""%(application,c)
                step = etree.Element("hudson.tasks.Shell")
                step.append(command)
                builder.append(step)
            return root
        except Exception as e:
            print "Falhou ao gerar Steps da Job: ",e


if __name__ == '__main__':
    j = JenkinsModule()
    j.createJob("Terminus","https://github.com/AlissonMMenezes/Terminus.git")
