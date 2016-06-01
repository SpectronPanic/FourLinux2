#!/usr/bin/python


import logging
from datetime import datetime
import sys

class Sistema:
    """
        Esse foi um sistema criado para testar o modulo de gerencia de logs do python.
    """
    def __init__(self):
        logging.basicConfig(filename='sistema.log', level=logging.INFO,
                            format='%(asctime)s %(message)s', datefmt='[ %d/%m/%Y %H:%M ]')
        self.user = 'spec'
        self.passwd = '4linux'
        self.is_logged = False
        logging.info('O sistema foi aberto')

    def autenticar(self):
        login = raw_input('Digite o seu login: ')
        passwd = raw_input('Digite a sua senha: ')
        if login == self.user and passwd == self.passwd:
            print 'Usuario autenticado com sucesso!'
            self.is_logged = True
            logging.info('Usuario %s foi autenticado' % login)
        else:
            print "Falhou ao autenticar"
            logging.warning('Foi negada a autenticacao do usuario %s' % login)
            sys.exit()

    def logar_servidor(self):
        servidores = ['web1', 'web2', 'web3', 'db1', 'db2', 'dns1', 'dns2']
        print 'Selecione o servidor que voce quer acessar: '
        for i, s in enumerate(servidores):
            print i, ' - ', s
        try:
            s = input('Digite so o numero do servidor: ')
            if not s in range(0, len(servidores)-1):
                raise
            print 'Acesso liberado ao servidor ', servidores[s]
            logging.info('Acesso liberado ao servidor %s' % servidores[s])
        except Exception as e:
            print 'Falhou ao acessar servidor'
            logging.error('Usuario tentou acessar servidor invalido: ')


if __name__ == '__main__':
    sistema = Sistema()
    sistema.autenticar()
    sistema.logar_servidor()
