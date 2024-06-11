'''1.1 Crea la classe Astronave con attributi capacita_carico, carico_attuale e risorse_raccolte (dizionario contente i nomi delle risorse come chiavi e le quantità come valori)
   1.2 Crea la classe Pianeta con attributi nome e risorse (dizionario contenente i nomi delle risorse come chiavi e quantità come valori)
   2. Implementa nella classe Astronave un metodo statico messaggio_esplorazione() che prende in input il nome di un pianeta e che ritorna in una stringa il messaggio che indica che l'astronave sta esplorando un particolare pianeta (usando il suo nome)
   3. Implementa nella classe Astronave un metodo di classe astronave_standard() che crea e ritorna un'istanza di Astronave con una capacità di carico pari a 150 tonnellate
   4. Implementa nella classe Astronave un metodo di istanza capacità_rimanente() che ritorna la differenza tra la capacità totale di carico dell'astronave e il carico attuale presente sull'astronave
   5. Implementa nella classe Astronave un metodo di istanza che verifica se l'astronave ha una capacità di carico residua sufficiente a ospitare un nuovo carico il cui peso viene passato in input. Il metodo dà un valore booleano e deve essere privato per la classe Astronave
   6. Implementa nella classe Astronave un metodo di istanza esplora() che prende in input un oggetto della classe Pianeta (pianeta da esplorare) che:
   6.1 Invoca il metodo statico messaggio_esplorazione() sulla classe Astronave e non sull'istanza
   6.2 Per ogni risorsa presente sul pianeta usa il metodo del carico residuo e se ritorna True aggiunge la risorsa all'astronave
   6.3 Aggiorna il carico attuale con il peso della risorsa appena aggiunta
   6.4 Aggiorna il dizionario dell'astronave con nome risorsa e suo peso
   7. Testa il codice:
   7.1 Cre una serie di pianeti con una serie di risorse
   7.2 Crea un'astronave standard
   7.3 esplora() i pianeti raccogliendo le risorse disponbili. Attenzione al caso in cui il carico residuo viene superato
   7.4 Visualizza sul terminale tutte le risorse caricate a bordo dell'astronave
   '''
   
from dataclasses import dataclass, field

@dataclass(init=True, repr=True, order=True, frozen=False) 
class Astronave:
    capacita_carico: float = 150
    carico_attuale: float = 0
    risorse_raccolte: dict = field(default_factory=dict) #utilizzo una factory function chen crea un dizionario vuoto per far si che sia diverso da ogni istanza (infatti i dict sono mutabili)
    
    
    @staticmethod
    def messaggio_esplorazione(nome_pianeta: str):
        print(f"Stai esplorando il pianeta {nome_pianeta}.")
    
    
    @classmethod
    def astronave_standard(cls):
        return cls()
    
    
    def capacita_rimanente(self):
        return self.capacita_carico - self.carico_attuale

    
    def _check_capacita_residua(self, carico):
        return self.capacita_carico >= carico + self.carico_attuale
    
    
    def esplora(self, pianeta):
        Astronave.messaggio_esplorazione(pianeta.nome)
        for key, value in pianeta.risorse.items():
            if self._check_capacita_residua(value):
                self.risorse_raccolte[key] = self.risorse_raccolte.get(key, 0) + value
                self.carico_attuale += value
            else:
                print(f"Limite raggiunto: impossibile raccogliere {key}")
                


@dataclass(init=True, repr=True, order=True, frozen=False) 
class Pianeta:
    nome: str
    risorse: dict
    


pianeta1 = Pianeta('Marte', {'acqua':150, 'terra': 20})
pianeta2 = Pianeta('Giove', {'vino': 20, 'birra':30, 'acqua':2})

astro = Astronave.astronave_standard()
astro.esplora(pianeta2)

for key, value in astro.risorse_raccolte.items():
    print(f"{key}: {value}")