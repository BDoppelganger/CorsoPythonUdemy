"""partendo da conto1.2.py inserisci la superclasse Conto che passa
nome e conto alla sottoclasse ContoCorrente"""

class Conto:
    def __init__(self, nome, conto):
        self.nome = nome
        self.conto = conto

class ContoCorrente(Conto):
    def __init__(self, nome, conto, importo):
        super().__init__(nome, conto)
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

c2 = ContoCorrente("Monica", 00000, 80000)
c2.descrizione()

print(c1.saldo)
c1.saldo = 3000
print(c1.saldo)

print(c2.saldo)
c2.saldo = 5000
print(c2.saldo)



