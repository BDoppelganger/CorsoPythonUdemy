"""partendo da conto1.3.py inserisci la superclasse GestoriContiCorrenti
avente un metodo di classe statico bonifico con parametri sorgente, destinazione e importo.
Il metodo bonifico dovrà invocare il metodo preleva per prelevare sul conto sorgente e 
invocare deposita sul conto di destinazione dello stesso importo usato sul metodo releva.
Creare infine due istanze di conti correnti c1 e c2 e fare un bonifico da c1 a c2"""

#prova

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

class GestoreContiCorrenti:
    @staticmethod
    def bonifico(sorgente, destinazione, importo):
        sorgente.preleva(importo)
        destinazione.deposita(importo)

c1 = ContoCorrente("Giuseppe", 12345, 20000)
c1.descrizione()

c2 = ContoCorrente("Monica", 00000, 80000)
c2.descrizione()

GestoreContiCorrenti.bonifico(c1,c2,1000)

c1.descrizione()
c2.descrizione()



