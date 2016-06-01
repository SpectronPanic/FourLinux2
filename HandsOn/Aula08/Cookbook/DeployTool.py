#!/usr/bin/python
import argparse
from Modules.DexterbookParser import DexterbookParser
from Modules.DockerModule import DockerModule
class DeployTool:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-i",help="Define o caminho do dexterbook da aplicacao")
    
    def getArgs(self):
        return self.parser.parse_args()

    def make(self,deploy_params):
       d = DockerModule()
       d.createContainer(deploy_params.get("application"))
       d.startContainer(deploy_params.get("application"))
       for c in deploy_params.get("deploy-sequence").get("commands"):
            print d.exec_command(deploy_params.get("application"),c)

if __name__ == '__main__':
    dt = DeployTool()
    args = dt.getArgs()
    dbp  = DexterbookParser(args.i)
    dt.make(dbp.get())
