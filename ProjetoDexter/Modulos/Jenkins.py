#!/usr/bin/python

import jenkins

class Jenkins:
    def __init__(self):
        try:
            self.server = jenkins.Jenkins("http://jenkins.dexter.com.br:8080")
            self.version = self.server.get_version()
            print "Conectou com sucesso"
        except Exception as e:
            print "Falhou ao conectar com o jenkins %s"%e

if __name__ == '__main__':
    j  = Jenkins()
