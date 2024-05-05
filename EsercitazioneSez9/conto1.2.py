"""partendo da conto1.1.py inserisci una property per l'attributo saldo,
rendendolo accessibile solo tramite la property
con getter e setter impostati con decoratori
usando in setter i metodi preleva e deposita per azzerare il conto e riaggiornarlo con l'importo scelto
"""

#prova per commit e pull su github

class ContoCorrente:
    def __init__(self, nome, conto, importo):
        self.nome = nome
        self.conto = conto
        self.__saldo = importo
    
    def preleva(self, importo):
        self.__saldo -= importo
        
    def deposita(self, importo):
        self.__saldo += importo
        
    def descrizione(self):
        print(f"{self.nome}, {self.conto}, {self.__saldo}")
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, importo):
        self.preleva(self.__saldo) #per richiamare metodi di istanza nella classe deve precedere il self
        self.deposita(importo) #per richiamare metodi di istanza nella classe deve precedere il self

c1 = ContoCorrente("Giuseppe", 12345, 20000)
c1.descrizione()

print(c1.saldo)
c1.saldo = 3000
print(c1.saldo)



