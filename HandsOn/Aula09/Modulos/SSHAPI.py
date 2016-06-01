#!/usr/bin/python

from paramiko import SSHClient
import paramiko
import ConfigParser

class SSHAPI:
    def __init__(self):
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            config = ConfigParser.ConfigParser()
            config.read("deploy.cfg")
            self.ssh.connect(config.get("docker","server"))
        except Exception as e:
            print "Falhou ao conectar por ssh: ",e


    def exec_ssh_command(self,cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        if stderr.channel.recv_exit_status() != 0:
            return stderr.read()
        else:
            return stdout.read()









