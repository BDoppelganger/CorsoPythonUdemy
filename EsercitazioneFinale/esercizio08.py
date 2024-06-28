"""Design Pattern State.
Lo stato di un oggetto è rappresentato dai valori delle sue proprietà ad un certo istante di tempo.
Il comportamento di un oggetto è invece rappresentato dai metodi. Il comportmento è influenzato dallo stato di un oggetto in un determinato momento e può a sua volta influenzarlo.
Gli oggetti possono avere tante istruzioni condizionali al loro interno per gestire il comportamento in funzione dello stato. Questo approccio rende il codice difficile da gestire quando il numero degli stati aumenta.
Il design pattern State può aiutare a gestire queste casistiche. Il design pattern State ci consente di dividere gli stati e i comportamenti ad essi associati in classi differenti.
Invece di avere un unico oggetto si definiscono oggetti di stato, le istanze di questi oggetti rappresentano uno stato particolare dello stato di questo oggetto che va a regolare un comportamento specifico.
L'oggetto originale chiamato Context mantiene in qualsiasi momento memoria del suo stato attuale, ovvero a un solo oggetto stato.
Quando lo stato dell'oggetto cambia il riferimento viene spostato su un nuovo oggetto stato, permettendo al contesto di cambiare dinamicamente il proprio stato.

Per modellare il pattern State:
- Abbiamo una classe astratta detta State che ha un'interfaccia costituita di metodi astratti che permettono di gestire i vari oggetti stato che vengono definiti in modo concreto nelle sottoclassi degli oggetti stato.
- Abbiamo poi le sottoclassi concrete della classe astratta State che rappresentano gli oggetti stato ognuno che implementa a sua modo i metodi della classe astratta State.
- Abbiamo la classe Context che contiene un'istanza di una delle sottoclassi della classe astratta State che rappresenta in ogni momento il suo stato corrente. Contiene dunque la logica per istanziare a seconda dello stato; questa delega viene gestito dal metodo request() che richiama i metodi del suo oggetto stato corrente.

Obiettivi:
Sviluppare sistema che gestisca dinamicamente dei cambiamenti di stato dei moduli scientifici dell'astronave. Gli stati da utilizzare saranno:
- Analisi
- Raccoltà dati
- Stand by
- Manutenzione

1. Definisci una classe astratta di nome StatoModulo con un metodo astratto handle_request().
2. Implementa diverse classi concrete sottoforma di sottoclassi di StatoModulo di nome StatoAnalisi, StatoRaccoltaDati, StatoStandby e StatoManutenzione.
3. Ogni stato oggetto dovrà implementare un comportamento specifico per il particolare stato ridefinendo il metodo handle_request() con l'emissione di un semplice messaggio di testo che contiene anche il nome del modulo scientifico come parte del messaggio.
4. Crea una classe ModuloScientifico che rappresenta il Context. Dovrà contenere un attributo nome (str) e dovrà mantenere un riferimento allo stato corrente del modulo, cioè ad un'istanza di una delle classi derivate da StatoModulo.
5. Implementa un metodo SetState() nella classe ModuloScientifico per cambiare lo stato del modulo ricevendo in input l'istanza dello stato scelto che dovrà sostituire la precedenza, e un metodo richiesta() per delegare le azioni al suo stato corrente invocando al suo interno handle_request() dello stato in questione.
6. L'istanza del modulo scientifico deve avere uno stato di deafault StatoStandby.
7. Crea istanze multiple di ModuloScientifico assegnando a ciascun modulo uno stato iniziale.
8. Testa il comportamento del modulo con richiesta() per vedere come il comportamento di ciascun modulo si adegua a seconda del suo stato corrente.
9. Modifica lo stato dei moduli scientifici e richiama richiesta().
"""

from abc import ABC, abstractmethod

class StatoModulo(ABC):
    @abstractmethod
    def handle_request(self, contesto):
        pass
    
    
class StatoAnalisi(StatoModulo):
    def handle_request(self, contesto):
        print(f"Il modulo {contesto.nome} è in stato Analisi Dati")
    
    
class StatoRaccoltaDati(StatoModulo):
    def handle_request(self, contesto):
        print(f"Il modulo {contesto.nome} è in stato Raccolta Dati")
    
    
class StatoStandby(StatoModulo):
    def handle_request(self, contesto):
        print(f"Il modulo {contesto.nome} è in stato Standby")
    
    
class StatoManutenzione(StatoModulo):
    def handle_request(self, contesto):
        print(f"Il modulo {contesto.nome} è in stato Manutenzione")
        
        
class ModuloScientifico:
    def __init__(self, nome):
        self.nome = nome
        self.stato = StatoStandby()
        
    def SetState(self, stato):
        self.stato = stato
    
    def richiesta(self):
        self.stato.handle_request(self)
        

if __name__ == "__main__": #testing
    server = ModuloScientifico("Server")
    server.SetState(StatoRaccoltaDati())
    navigatore = ModuloScientifico("Navigatore")
    navigatore.SetState(StatoManutenzione()) 
    motori = ModuloScientifico("Motori")
    
    server.richiesta()
    navigatore.richiesta()
    motori.richiesta()
    
    motori.SetState(StatoManutenzione())
    motori.richiesta()
    
    