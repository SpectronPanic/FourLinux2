#!/usr/bin/python

from paramiko import SSHClient
import paramiko

class SSHModule:
    def __init__(self):
        try:
            self.server = "192.168.0.2"
            self.client = SSHClient()
            self.client.load_system_host_keys()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(hostname=self.server,username="forlinux")
        except Exception as e:
            print "Falhou ao conectar com o servidor: ",e

    def execCommand(self,cmd):
        try:
            stdin,stdout,stderr = self.client.exec_command(cmd)
            if stderr.channel.recv_exit_status != 0:
                return stderr.read()
            else:
                return stdout.read()
        except Exception as e:
            print "Falhou ao executar comando: ",e
