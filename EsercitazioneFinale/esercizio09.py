"""Design Pattern Composite.
Definizione Tutto-Parti: è un principio di design architetturale del software che permette di trattare in maniera uniforme un insieme di oggetti individuali insieme alle loro composizioni.
Utile per strutture gerarchiche o ad albero, dove ogni nodo può essere un oggetto singolo o un contenitore con più oggetti.
Ad esempio la struttura di directory del PC sfrutta il concetto tutto-parti. Le directory sono i compositi e i file sono i nodi foglia (oggetti singoli).

Modello ad oggetti del pattern composite.
Client: oggetto che manipola oggetti che fanno parte di una composizione gerarchica tutto-parti.
Component: interfaccia di programmazione unica e specifica (classe atratta) utilizzata dal client che consente di interagire con gli oggetti della struttura composita. Gestisce operazioni comuni a oggetti primitivi e agli oggetti compositi.
Leaf e Composite: Entrambi sottoclassi concrete di Component:
    Leaf: componente di ultimo livello
    Composite: tipo composito. Presenta un attributo di nome children che rappresenta gli oggetti che lo compongono che derivano dalla superclasse atratta component (può contenere sia leaf che composite).

Metodi astratti usati da Component: 
Operation() gestisce in modo astratto il comportamento dei componenti. La classe Leaf e Composite devono fornirne un'implementazione concreta. Nei Composite bsogna scorrere la lista children per scandagliare tutti gli oggetti a cascata scatenando le operazioni concrete di operation().
Add(Component) aggiunge un singolo componente all'elenco children ed è presente nella classe Composite in versione concreta ma non in Leaf.
Remove(component) inverso di quella di sopra.
GetChild(int) che accede e ritorna uno dei children usando un numero intero come indice all'interno della lista dei children. Questo metodo viene implmentato solo in Composite.

Obiettivi:
Sviluppa sistema che implementa design pattern composite per mappare e utilizzare una struttura gerarchica dei sistemi dell'astronave.

1. Dichiara classe astratta ComponenteAstronave che rappresenta la classe Component e definire il metodo operazione() come metodo astratto che sarà implementata dalle varie sottoclassi.
2. Fornire implementazione vuota dei metodi aggiungi(), rimuovi() e getChild(), decidere se devono essere astratti o no
3. Implementa classe Sistema (leaf) e SistemaCompesso (Composite) come sottoclassi della classe ComponenteAstronave che dovranno sovrascrivere il metodo operazione()
4. Decidere dove e come implementare i tre metodi della gestione dei children e come implementarne l'elenco.
5. Ogni componente dell'astronave deve avere un nome che viene fornito quando vengono create le istanze. Il nome dell'astronave deve essere inizializzato nella superclasse astratta (vedere come gestirlo nelle due sottoclassi concrete).
6. il metodo operazione() concreto deve mostrare a terminale un messaggio  con il nome del componente o foglia. nel caso dei compositi operazione deve invocare i metodi operazione degli elementi della classe children a cascata fino gli oggetti foglia.
7. Nel test crea sistemi individuali (Sistema), raggruppali in moduli complessi (SistemaComplesso) e organizza tutti i moduli in una struttura gerarchica. Il modulo di livello più alto è l'astronave e qua dovrò invocare operazione() che a cascata andrà su tutti gli oggetti che ne fanno parte fino alle foglie.
"""

from abc import ABC, abstractmethod

class ComponenteAstronave(ABC):
    def __init__(self, nome):
        self.nome = nome
    
    @abstractmethod
    def operazione(self):
        pass
    
    def aggiungi(self, componente):
        pass
    
    def rimuovi(self, componente):
        pass
    
    def getChild(self, i):
        pass
    

class Sistema(ComponenteAstronave):
    def operazione(self):
        print(f"Sistema {self.nome} in operazione")
    
    
class SistemaComplesso(ComponenteAstronave):
    def __init__(self, nome):
        super().__init__(nome)
        self._componenti = []
        
    def operazione(self):
        print(f"Sistema complesso {self.nome} in operazione")
        for componente in self._componenti:
            componente.operazione()
        
    def aggiungi(self, componente):
        self._componenti.append(componente)
        
    def rimuovi(self, componente):
        self._componenti.remove(componente)
    
    def getChild(self, i):
        if i < 0 and i >= len(self._componenti):
            return None
        return self._componenti[i]
    
a = SistemaComplesso('Astronave')
m = SistemaComplesso('Motori')
p = Sistema('Propulsori')
sg = SistemaComplesso('Sistema di guida')
pu = SistemaComplesso('Pulsantiera')
f = Sistema('Freno')
ac = Sistema('Acceleratore')

m.aggiungi(p)
sg.aggiungi(pu)
pu.aggiungi(f)
pu.aggiungi(ac)
a.aggiungi(m)
a.aggiungi(sg)

a.operazione()