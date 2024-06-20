'''Stack: struttura di dati immaginabile come una pila dove per eliminare e aggiungere si parte sempre dalla sommità della pila.
Su uno stack si possono usare tre operazioni fondamentali: push (aggiungere sulla pila), pop (rimuovere dalla sommità della pila) e peek (esamina l'elemento in cima alla pila senza rimuoverlo)
La struttura stack funziona quindi con una logica LIFO (last in first out) il primo ad entrare è il primo a uscire.
Quando usando push raggiungo la capacità di uno stack si ha l'overflow --> eccesso di dati.
Quando usando pop raggiungo uno stack vuoto si ha l'underflow --> carenza di dati.

1. Definire classe di nome Comunicazione che rappresenta i messaggi che arrivano che avrà due attrbuti: mittente e messaggio (due stringhe)
2. Definire classe di nome StackComunicazioni che implementa uno stack per gestire i messaggi. La classe deve avere un attributo di istanza capacita e un ulteriore attributo che dovrà essere usato internamente per memorizzare i messaggi dello stack
3. Definire i metodi di istanza push (deve restituire messaggio di avviso se si ha overflow), pop (deve restituire messaggio di avviso se si ha underflow) e peek
4. Crea un'istanza di StackComunicazioni e aggiungi e rimuovi messaggi per testare la struttura dati
'''

from dataclasses import dataclass, field

@dataclass(init=True, repr=True, order=True, frozen=False) 
class Comunicazione:
    mittente: str
    messaggio: str

@dataclass(init=True, repr=True, order=True, frozen=False) 
class StackComunicazioni:
    capacita: int
    dictionary: dict = field(default_factory=dict) #utilizzo una factory function chen crea un dizionario vuoto per far si che sia diverso da ogni istanza (infatti i dict sono mutabili)
    
    def push(self, message):
        if len(self.dictionary) >= self.capacita:
            print(f"Overflow: Message from {message.mittente}: {message.messaggio} CANNOT BE SAVED")
        else:
            self.new_message = {message.mittente: message.messaggio}
            self.temp_dict = self.new_message.copy()
            self.temp_dict.update(self.dictionary)
            self.dictionary = self.temp_dict
        print(self.dictionary)
    
    def pop(self):
        if len(self.dictionary) < 1:
            print("Underflow")
        else:
            self.first_key = next(iter(self.dictionary))
            self.first_value = self.dictionary.pop(self.first_key)
            print(f"Message from {self.first_key}: {self.first_value} REMOVED!")
            print(self.dictionary)
    
    def peek(self):
        if len(self.dictionary) < 1:
            print("No message found!")
        else:
            self.first_key = next(iter(self.dictionary))
            self.first_value = self.dictionary[self.first_key]
            print(f"Message from {self.first_key}: {self.first_value}")
            
    
stack = StackComunicazioni(3)

m1 = Comunicazione("Gino", "ciao")
m2 = Comunicazione("Gianni", "ciaooo")
m3 = Comunicazione("Giorgio", "ciao!")
m4 = Comunicazione("Giannalberto", "ciao!!!")

stack.push(m1)
stack.push(m2)
stack.push(m3)
stack.push(m4)

stack.pop()

stack.peek()

