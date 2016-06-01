import jenkins
from lxml import etree
import ConfigParser
import os
import json

class JenkinsModule:
    def __init__(self):
        try:
            cf = ConfigParser.ConfigParser()
            cf.read(os.path.dirname(os.path.abspath(__file__))+"/../config.cfg")
            self.server = jenkins.Jenkins(cf.get("jenkins","server")+":8080")
        except Exception as e:
            print "Falhou ao conectar com o jenkins"        

    def createJob(self,application,repo):
        with open(os.path.dirname(os.path.abspath(__file__))+"/../Templates/job.xml","r") as f:
            job_xml = f.read().replace("REPO",repo)
        xml = etree.tostring(self.generateJobSteps(job_xml,"Terminus"))
        print self.server.create_job(application,xml)

    def generateJobSteps(self,xml,application):
        try:
            with open(os.path.dirname(os.path.abspath(__file__))+"/../application.json","r") as f:
                deploy = json.loads(f.read())
            root = etree.XML(xml)
            for b in root.findall("builders"):
                builder = b
            for c in deploy.get("deploy-sequence").get("commands"):
                command = etree.Element("command")
                command.text = "ssh forlinux@192.168.0.2 \"docker exec %s bash -c '%s'\""%(application,c)
                step = etree.Element("hudson.tasks.Shell")
                step.append(command)
                builder.append(step)
            return root 
        except Exception as e:
            print "Erro: %s"%e
