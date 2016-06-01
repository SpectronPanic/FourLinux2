#!/usr/bin/python

from pymongo import MongoClient

class MongoDB:
    def __init__(self):
        self.client = MongoClient("127.0.0.1")
        self.db = self.client['dexterops']

    def salvarProvisionamento(self,documento):
        try:
            self.db.provisionamento.insert(documento)
        except Exception as e:
            print "Falhou ao inserir servico no mongodb %s"%e

    def filaProvisionamento(self):
        try:
            return self.db.provisionamento.find({})
        except Exception as e:
            print "Falhou ao buscar servicos no mongodb %s"%e

    def atualizarStatusProvisionamento(self,provisionamento_id,status):
        try:
            self.db.provisionamento.update({"_id":provisionamento_id},{"$set":{"status":status}})
        except Exception as e:
            print "Falhou ao atualizar servico no mongodb %s"%e
