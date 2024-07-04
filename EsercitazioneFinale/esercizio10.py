'''Design Pattern Factory Method

Una fabbrica di oggetti. Si creano oggetti differenti senza focalizzarsi su dettagli interni. Si usa una classe astratta.
Consente anche l'estendibilità usando nuovi metodi di fabbrica per creare nuovi oggetti aggiuntivi senza cambiare il codice.
Il Factory Method mantiene nascosti i dettagli degli oggetti. Cioè posso cambiare la logica degli oggetti già creati senza influenzare il resto del codice.
Una volta definiti i metodi di fabbrica per creare diversi oggetti questi possono essere utilizzati ovunque nel codice per creare nuovi oggetti.

Conviene usare il Factory Method quando una classe non può anticipare la classe di oggetti da creare e quando una classe vuole che siano le proprie sottoclassi a definire che tipo di oggetto creare.

Definizione del design pattern Factory Method:
- Definisce una classe (che può essere astratta) che rappresenta gli oggetti che verranno creati. Tutte le classi concrete erediteranno da questa classe detta Product.
- Le classi concrete create dal factory method si chiamano ConcreteProduct. Ogni ConcreteProduct rappresenta un tipo di oggetto che il factory method è in grado di creare.
- Il Creator è l'interfaccia/classe astratta che dichiara il factory method, che è un metodo astratto che è responsabile della creazione (return) degli oggetti di tipo Product. Può implementare altri metodi che utilizzano oggetti Product per implemntare particolari logiche applicative degli oggetti Product (facoltativo).
- ConcreteCreator classe concreta che implementa realmente il facotry method definito nella classe Creator. Definisce quale ConcreteProduct deve essere creato dal factory method. Ogni concretecreator può creare un solo tipo di ConcreteProduct nella sua forma generale, però ci sono modi per specificare che classe creare di ConcreteProduct.

Obiettivi esercitazione:
Utilizzare il pattern Factory Method per creare un sistema flessiibile di creazione di moduli spaziali.

1. Definisci classe concreta ModuloSpaziale, interfaccia comune a tutti i moduli spaziali (identificata come classe Product). Contiene 3 attributi (stringhe di testo): nome, tipo, funzione. Questi attributi devono essere inizializzati nella classe.
2. Definisci le classi concrete per i diversi tipi di moduli spaziale, come ModuloEsplorazione, ModuloDifesa, ModuloRicerca, ModuloSupportoVitale (rappresentano le classi ConcreteProduct), che derivano dalla classe ModuloSpaziale. Nell'inizializzazione delle classi bisogna invocare l'inizializzatore della classe ModuloSpaziale fornendo i tre valori per gli attributi adatti allo specifico modulo spaziale.
3. Dichiara la classe astratta Creator che deve avere un solo metodo astratto crea_modulo() che prende in input un parametro tipo_modulo (stringa) che servirà a scegliere dinamicamente quale modulo fabbricare nelle invocazioni delle sottoclassi concrete di Creator.
4. Dichiara la classe FactoryModuliSpaziali (che rappresenta il concrete creator) come sottoclasse di creator. Questa classe deve contenere l'implementazione di crea_modulo() che usando il parametro tipo_modulo deve scegliere la classe adeguata tra quelle che rappresentano i ConcreteProduct, deve istanziarla e ritornare l'istanza appena creata.
5. Nella classe FactoryModuliSpaziali inserisci una condizionione di errore, cioè se il valore fornito per il parametro tipo_modulo non è uno di quelli previsti, allora solleva un'exception con il messaggio "Tipo di modulo non valido: {tipo_modulo}".
6. Crea un'istanza della classe FactoryModuliSpaziali poi usa l'istanza della factory per creare tre moduli spaziali (Esplorazione, Difesa, Ricerca) provando anche a creare un modulo inesistente così da sollevare l'eccezione.
'''

from abc import ABC, abstractmethod

class ModuloSpaziale:
    def __init__(self, nome, tipo, funzione):
        self.nome = nome
        self.tipo = tipo
        self.funzione = funzione

class ModuloEsplorazione(ModuloSpaziale):
    def __init__(self):
        super().__init__("Modulo Esplorazione", "Esplorazione", "Esplorare")
        
class ModuloDifesa(ModuloSpaziale):
    def __init__(self):
        super().__init__("Modulo Difesa", "Difesa", "Difendere")

class ModuloRicerca(ModuloSpaziale):
    def __init__(self):
        super().__init__("Modulo Ricerca", "Ricerca", "Ricercare")
        
class Creator(ABC):
    @abstractmethod
    def crea_modulo(self, tipo_modulo: str):
        pass
    
class FactoryModuliSpaziali(Creator):
    def crea_modulo(self, tipo_modulo: str):
        if tipo_modulo == "Esplorazione":
            return ModuloEsplorazione()
        elif tipo_modulo == "Difesa":
            return ModuloDifesa()
        elif tipo_modulo == "Ricerca":
            return ModuloRicerca()
        else:
            raise ValueError(f"Tipo di modulo non valido: {tipo_modulo}")
        

fabbrica = FactoryModuliSpaziali()
esplorazione = fabbrica.crea_modulo("Esplorazione")
print(esplorazione.funzione)
difesa = fabbrica.crea_modulo("Difesa")
print(difesa.funzione)
ricerca = fabbrica.crea_modulo("Ricerca")
print(ricerca.funzione)
cuorirossi = fabbrica.crea_modulo("Pinella")