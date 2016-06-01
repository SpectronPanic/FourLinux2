#!/usr/bin/python

from paramiko import SSHClient
import paramiko

class SSHModule:
    def __init__(self,server="192.168.0.2"):
        try:
            self.server = server
            self.client = SSHClient()
            self.client.load_system_host_keys()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(user='forlinux',self.server)
            print "[+] Abrindo conexao com o servidor por ssh"
        except Exception as e:
            print "Erro: %s"%e
            raise

    def execCommand(self,com):    
        try:
            stdin,stdout,stderr = self.client.exec_command(com)
            if stderr.channel.recv_exit_status() != 0:
                return stderr.read()
            else:
                return stdout.read()
        except Exception as e:
            print "Nao conseguiu conectar ao servidor %s"%e
            raise
