#!/usr/bin/python
from Modulos.MongoDB import MongoDB
class DexterOps:
    def __init__(self):
        prov = MongoDB()
        self.fila = prov.filaProvisionamento()

    def verFila(self):
      print  [ f["gitlab"] for f in self.fila ]


if __name__ == "__main__":
    do = DexterOps()
    do.verFila()
