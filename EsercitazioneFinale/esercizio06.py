'''Il pattern Observer è un design pattern che definisce una dipendenza 1:n tra gli oggetti: quando un oggetto cambia stato tutti gli oggetti dipendenti vengono notificati.
Gli Observers, oggetti che dipendono dall'oggetto che cambia (detto Subject), sono indipendenti tra loro e quando vengono notificati del cambiamento sul Subject rispondono ognuno a modo proprio.
Il tipo di interazione tra soggetto e osservatori viene detto Publish and Subscribe, dove il soggetto è pubblicatore e gli osservatori sono i sottoscrittori.

Oggetti del pattern Observer:
- Subject: classe astratta che non può essere instanziata. Deve offrire metodi che consentono di attaccare o staccare i sottoscrittori e uno per notificare del cambiamento.
- Observer: classe astratta che ha delle sottoclassi istanziabili che vedono il subject. Deve avere un metodo per aggiornare gli observer sottoscritti al subject.
- Concrete Subject: è una classe cosncreta sottoclasse di Subject. Deve mantenere lo stato di interesse per gli osservatori concreti (come attributo) e è in grado di inviare le notifiche agli osservatori concreti quando li prende dalla superclasse Subject.
- Concrete Observer: sono classi istanziabili di observer che mantiene attributi sul proprio stato e un metodo concreto simile al metodo astratto della classe astratta Observer

Creare un sistema di allarme (concrete subject) che notifica varie parti dell'astronave (concrete observers con varie istanze in base alla categorie delle parti) di una minaccia.
In accordo al pattern observer, deve essere introdotta una classe astratta subject e la classa astratta observer.
La classe observer astratta ha un metodo astratto di nome aggiorna che prende in imput uno status (parametro booleano) che rappresenta a livello completo lo stat di attivazione del sistema di allarme --> indica che tutte le sottoclassi concrete dovranno avere implementazione di questo metodo
La classe astratta subject contiene quello che serve per gestire il pattern observer: lista _observers[] inizialmente vuota, il metodo aggiungi_observer(observer), il metodo rimuovi_observer(observer) e notifica_observer(status) che per ciascun observer nella lista attiva metodo aggiorna per notificare ciascun observer a svolgere la sua funzione specifica
La classe SistemaDiAllarme (soggetto concreto) dovrà essere una sottoclasse di subject che ha uno stato attivo o non attivo gestito da valore booleano _is_active. Deve implemntare metodo attiva_allarme che attiva il sistema di allarme e notifica gli observers con notifica_observers(status). Deve avere disattiva allarme che fa il contrario
Creare 3 classi concrete di sottoscrittori PonteComando, SalaMotori, CabineEquipaggio che devono implemtare la versione cocncreta del metodo aggiorna(status) per intraprendere i prpri cambiamenti (per esempio stampando a terminale dei messaggi per farla più semplice)
Testare il codice creando un'istanza di SistemaDiAllarme e delle classi concrete dei sottoscrittori. Aggiungere queste istanze a SistemaDiAllarme col metodo aggiungi_observers. Attivare l'allarme con metodo attiva_allarme e disattiva l'allarme subito dopo. invoca il metodo rimuovi_observer togliendo la sala motori, attiva l'allarme e poi disattivalo
'''

from abc import ABC, abstractmethod
from dataclasses import dataclass

class Observer(ABC):
    
    @abstractmethod
    def aggiorna(status: bool):
        pass
    
class Subject(ABC):
    def __init__(self):
        self._observers = []
    
    def aggiungi_observer(self, observer: Observer):
        self._observers.append(observer)
        
    def rimuovi_observer(self, observer: Observer):
        self._observers.remove(observer)
        
    def notifica_observer(self, status: bool):
        for observer in self._observers:
            observer.aggiorna(status)
 
class SistemaDiAllarme(Subject):
    def __init__(self):
        super().__init__()
        self._is_active = False
    
    def attiva_allarme(self):
        self._is_active = True
        self.notifica_observer(self._is_active)
    
    def disattiva_allarme(self):
        self._is_active = False
        self.notifica_observer(self._is_active)
        
class PonteComando(Observer):
    def aggiorna(self, status: bool):
        if status == True:
            print("chiudi porte")
        else:
            print("apri porte")
            
class SalaMotori(Observer):
    def aggiorna(self, status: bool):
        if status == True:
            print("accelera")
        else:
            print("normale velocità")
            
class CabineEquipaggio(Observer):
    def aggiorna(self, status: bool):
        if status == True:
            print("chiudi porte")
        else:
            print("apri porte")
    
    
if __name__ == "__main__": #testing
    # Creazione del sistema di allarme
    allarme = SistemaDiAllarme()

    # Creazione delle varie sezioni (osservatori)
    ponte_comando = PonteComando()
    motori = SalaMotori()
    cabine = CabineEquipaggio()

    # Aggiunta degli osservatori al sistema di allarme
    allarme.aggiungi_observer(ponte_comando)
    allarme.aggiungi_observer(motori)
    allarme.aggiungi_observer(cabine)

    # Simulazione di un allarme
    print("\nSimulazione primo allarme:")
    allarme.attiva_allarme()

    # Simulazione della fine dell'allarme
    print("\nFine  primo allarme:")
    allarme.disattiva_allarme()

    allarme.rimuovi_observer(motori)

    # Simulazione di un allarme
    print("\nSimulazione secondo allarme:")
    allarme.attiva_allarme()

    # Simulazione della fine dell'allarme
    print("\nFine secondo allarme:")
    allarme.disattiva_allarme()
  