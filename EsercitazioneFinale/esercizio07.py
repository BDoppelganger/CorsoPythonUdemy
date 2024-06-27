'''Un Grafo è una struttura di dati costrituita da nodi connessi da archi.
I grafi possono avere varie caratteristiche:
- Grafo non orientato in cui un arco tra due nodi non ha una direzione (A,B) = (B,A)
- Grafo orientato (digrafo) in cui l'arco ha una direzione ben definita.
- Grafo pesato in cui ogni arco ha un valore numerico associato, detto peso.
- Grafo connesso in cui esiste sempre un percorso tra qualsiasi coppia di vertici del grafo.
- Grafo non connesso in cui ci possono essere nodi non collegati tra loro.
- Grafo completo se ogni coppia di vertici è collegata, cioè si ha un numero di archi massimo.

I grafi possono essere rappresentati da tecniche differenti:
- Lista di adiacenza: ogni nodo ha una lista di nodi con i quali è collegato da archi insieme ai relativi pesi.
- Matrice di adiacenza: matrice bidimensionale nelle quali le celle rappresentano l'assenza o la presenza di archi tra loro.

La mappa stellare da costruire è rappresentata da un grafo.
Ogni nodo è un singolo corpo celeste e ogni arco rappresenta un percorso che l'astronave può percorrere tra due corpi celesti.
Ogni arco rappresenta un peso che rappresenta la distanza tra due corpi celesti in UA.
Non è detto che tutti i corpi celesti siano tra loro raggiungibili.

Questa mappa permetterà di:
- Modificare, aggiungere e rimuovere nuovi corpi celesti alla mappa.
- Stabilire nuovi percorsi tra i corpi celesti.
- Assegnare una distanza a ciascun percorso tra due corpi celesti, espresso in UA.
Fare ciò implementando un grafo pesato non connesso con liste di adiacenza.
Facciamo l'ipotesi che in questo caso la distanza tra due corpi dovrà apparire nelle liste di adiacenza di entrambi i corsi e coinciderà.

1. Crea una classe CorpoCeleste con un attributo nome ed un attributo adiacenti (una struttura dati tipo lista o altro) adatto a rappresentare l'elenco di percorsi presenti per ogni corpo celeste assieme alla distanza.
2. Implementa i metodi di istanza aggiungi_collegamento() e rimuovi_collegamento() che prendono in input il nome di un altro corpo celeste e la distanza del nodo attuale da questo nodo.
3. Implementa il metodo di visualizzazione automatica delle stringhe __str__() che deve rappresentare a terminale l'elenco di tutti i nodi adiacenti al nodo attuale visualizzando nome e distanza
4. Crea una classe MappaStellare
5. In questa classe crea attributo di istanza corpi_celesti che deve essere una struttura dati che contiene l'elenco dei corpo celesti presenti nella mappa (i nodi) rappresentati come istanza della classe CorpoCeleste e deve essere possibile accedere a un qualunque corpo celeste tramite il suo attributo nome.
6. Implementa un metodo aggiungi_corpo_celeste() che prende in input il nome e crea un'istanza di CorpoCeleste e la aggiunge all'elenco nella mappa (il nome del corpo celeste deve essere una chiave mentre l'oggetto del corpo celeste un valore).
7. Implementa un metodo rimuovi_corpo_celeste() che prende in input il nome di un corpo celeste e lo rimuove dalla mappa stellare, rimuovendo anche tutti i collegamente verso questo nodo presenti negli altri nodi.
8. Implementa un metodo aggiungi_percorso() che prende in input il nome del nodo di partenza e del nodo di arrivo e la distanza tra i due nodi. Se entrambi i nodi appartengono già alla mappa, per ognuno dei due nodi utilizza il metodo aggiungi_collegamento() sulle istanze per il collegamento fonendo in ntrambi i casi il nome della destinazione e la distanza.
9. Aggiungi il metodo __str__() che deve rappresentare a terminale l'elenco di tutti i corpi celesti presenti nella mappa e per ogni corpo celeste visualizzare la lista di adiacenza.
Si può usare il metodo join() su un iterabile (lista, tuple, dict, etc..) per unire in una stringa tutti gli elementi di un iterabile con un separatore: 'separatore'.join(iterabile)
Si può usare join() anche con una generator expression oltre con gli iterabili. Facciamo questo per il punto 9. e il punto 3 per creare il valore di ritorno.
10. Genera un certo numero di istanze di corpi celesti.
11. Crea una mappa stellare e aggiungi i corpi celesti.
12. Crea manualmente una serie di connessione tra questi pianeti con le distanze.
13. Esegui il print sulla mappa stellare provocando la sequenza di esecuzione dei metodi __str__() sulla mappa e sui singoli corpi celesti.
14. Elimina un pianeta e visualizza il contenuto della mappa stellare.
'''

from dataclasses import dataclass, field

@dataclass(init=True, repr=True, order=True, frozen=False) 
class CorpoCeleste:
    nome: str
    adiacenti: dict = field(default_factory=dict)
    
    def aggiungi_collegamento(self, nodo_altro, distanza):
        self.adiacenti[nodo_altro] = distanza
    
    def rimuovi_collegamento(self, nodo_altro):
        if nodo_altro in self.adiacenti:
            del self.adiacenti[nodo_altro]
        else:
            raise KeyError
            
    def __str__(self):
        return f"{self.nome} è collegato con:\n" +  ",\n".join(f"{k} con distanza {v}" for k, v in self.adiacenti.items())


@dataclass(init=True, repr=True, order=True, frozen=False)
class MappaStellare:
    corpi_celesti: dict = field(default_factory=dict)
    
    def aggiungi_corpo_celeste(self, nome):
        self.corpi_celesti[nome] = CorpoCeleste(nome)
    
    def rimuovi_corpo_celeste(self, nome):
        if nome in self.corpi_celesti:
            for corpo in self.corpi_celesti.values():
                corpo.rimuovi_collegamento(self.corpi_celesti[nome])
            del self.corpi_celesti[nome]
        else:
            raise KeyError
    
    def aggiungi_percorso(self, partenza, arrivo, distanza):
        if partenza in self.corpi_celesti and arrivo in self.corpi_celesti:
            self.corpi_celesti[partenza].aggiungi_collegamento(self.corpi_celesti[arrivo], distanza)
            self.corpi_celesti[arrivo].aggiungi_collegamento(self.corpi_celesti[partenza], distanza)
            
    def __str__(self):
        return f"\n".join(str(nome) for nome in self.corpi_celesti.values())
            

ms = MappaStellare()

ms.aggiungi_corpo_celeste("cc1")
ms.aggiungi_corpo_celeste("cc2")
ms.aggiungi_corpo_celeste("cc3")

ms.aggiungi_percorso("cc1", "cc2", 3)
ms.aggiungi_percorso("cc1", "cc3", 4)

print(ms)

