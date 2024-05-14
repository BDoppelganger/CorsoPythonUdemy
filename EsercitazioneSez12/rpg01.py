'''Supponiamo di dover lavorare a un progetto per la 
realizzazione di un gioco di ruolo. 
Quindi avremo varie classi che rappresentano categorie di personaggi
differenti e ogni classe ha diversi metodi di attacco.
Tuttavia, la modalità specifica di attacco dipende dalla specifica classe del personaggio'''

from abc import ABC, abstractmethod #importo dal modulo abc la metaclasse ABC e abstractmethod che ci serve come decoratore dei metodi astratti

class Personaggio(ABC):
    def __init__(self, nome): #inizializzatore della classe Personaggio per creare un attributo di istanza che contiene il nome del personaggio. Questo perché alla fine tutti i personaggi avranno un nome
        self.nome = nome
    
    @abstractmethod #abbiamo creato un metodo astratto per l'attacco ma non abbiamo passato nessuna informazione 
    def attacco(self):
        pass


#passiamo adesso a creare le classi concrete

class Guerriero(Personaggio):
    def attacco(self): #il metodo concreto richiama il metodo astratto
        return f"{self.nome} sferza un colpo di spada!"
    
class Mago(Personaggio):
    def attacco(self): #il metodo concreto richiama il metodo astratto
        return f"{self.nome} lancia un incantesimo!"
    
class Assassino(Personaggio):
    def attacco(self): #il metodo concreto richiama il metodo astratto
        return f"{self.nome} attacca furtivamente con un pugnale!"
   
    
#introduciamo un codice per testare le classi create

if __name__ == "__main__": #utilizzato per capire se lo script è stato importato come programma principale o se è stato portato come modulo all'interno di un altro script. __name__ è il nome del modulo corrente. Quando uno script viene eseguito direttamente __name__ viene impostato sul valore "__main__" 
    aragorn = Guerriero("Aragorn")
    gandalf = Mago("Gandalf")
    bilbo = Assassino("Bilbo")
    
    print(aragorn.attacco())
    print(gandalf.attacco())
    print(bilbo.attacco())
