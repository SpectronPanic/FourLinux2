#!/usr/bin/python

import gitlab

class Gitlab:
    def __init__(self):
        try:
            self.servidor = "gitlab.dexter.com.br"
            self.admin = "devops@dexter.com.br"
            self.pass = "4linux123"
            self.git = gitlab.Gitlab("http://%s"%self.servidor,verify_ssl=False)
            self.git.login(user=self.admin,password=self.pass)
            print "conectou com sucesso!"
        except Exception as e:
            print "Falhou ao conectar %s"%e

    def criarUsuario(self):
        try:
            status = self.git.createuser("joao","joao","joao@dexter.com.br","alterarsenha")
            if status:  
                print "Usuario criado com sucesso"
            else:
                print "Falhou ao criar o usuario"
        except Exception as e:
            print "Falhou ao criar o usuario %s"%e

    def criarProjeto(self):
        try:
            self.git.createproject(self.projeto,path=self.projeto)
            print "Projeto criado com sucesso!"
        except Exception as e:
            print "Falhou ao criar projeto %s"%e

    def adicionarMembroProjeto(self,projeto,membro):
        try:
            status = self.git.addmemberproject(projeto['id'],membro,'developer')
            if status:
                print "Usuario adicionado ao projeto"
            else:
                print "Nao foi possivel adicionar o usuario ao projeto %s"%status
        except Exception as e:
            print "Falhou ao adicionar membro %s"%e

if __name__ == '__main__':
    g = Gitlab()
