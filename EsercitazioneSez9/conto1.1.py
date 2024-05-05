"""Crea una classe ContoCorrente:
1. con tre attributi d'istanza nome, conto e saldo
2. con tre metodi di istanza, uno per prelevare, uno per depositare e uno che dia la descrizione dei parametri del conto
e poi testa il codice creando istanze e compiendo operazioni su di esse"""

#prova per commit e pull su github

class ContoCorrente:
    def __init__(self, nome, conto, importo):
        self.nome = nome
        self.conto = conto
        self.saldo = importo
    
    def preleva(self, importo):
        self.saldo -= importo
        
    def deposita(self, importo):
        self.saldo += importo
        
    def descrizione(self):
        print(f"{self.nome}, {self.conto}, {self.saldo}")

c1 = ContoCorrente("Giuseppe", 12345, 20000)
c1.descrizione()

c1.preleva(1000)
c1.descrizione()

c1.deposita(2000)
c1.descrizione()

c2 = ContoCorrente("Monica", 678910, 80000)
c2.descrizione()
