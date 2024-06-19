'''La Linked List è una struttura dati lineare in cui gli elementi non sono memorizzati in posizione di memoria contigue ma sono collegati tra loro con dei puntatori
ogni elemento di una linked list è rappresentato da un nodo composto dal dato e dal puntatore al prossimo nodo. Il primo nodo viene detto head. L'ultimo nodo punta a None
L'eliminazione e l'aggiunta dei nodi nelle linked list si fa aggiornando i puntatori.

Creare una struttura dati chiamandola LinkedListPianeti per mantenere la registrazione dei pianeti via via che vengon scoperti:
1. Implementa classe Pianeta che abbia un attributo nome e un attributo successivo che rappresenta il puntatore al nodo successivo. Quando viene creata un'istanza il puntatore al prossimo nodo deve essere impostato a None, negli altri casi punterà al nodo successivo
2. Implementa la classe LinkedListPianeti in modo che abbia un attributo testa che rappresenta il primo nodo, un metodo AggiungiPianeta che aggiunge un nodo (occhio a qualdo la lista è vuota; None) e un metodo VisualizzaPianeti che scorre la linked list
3. Genera un certo numero di nodi per la linked list, crea un'istanza della linked list e usa il metodo AggiungiPianeta per aggiungere nodi e infine visualizza la linked list
'''

class Pianeta:
    def __init__(self, nome, successivo = None):
        self.nome = nome
        self.successivo = successivo

class LinkedListPianeti:
    def __init__(self):
        self.testa = None #non ci pianeti visitati
        
    def AggiungiPianeta(self, nome_pianeta):
        pianeta_aggiunto = Pianeta(nome_pianeta) #creo un'istanza del nuovo pianeta che voglio aggiungere che avrà il nome dato da me è un puntatore successivo None
        if self.testa is None: #se la lista è vuota
            self.testa = pianeta_aggiunto #ovvero aggiorno la testa mettendoci questo nuovo pianeta aggiunto che manterrà il suo puntatore None
        else: #se la lista non è vuota
            ultimo_pianeta = self.testa #inizializzo una variabile ultimo_pianeta come testa (ovvero che prende l'ultimo pianeta con puntatore None) 
            while ultimo_pianeta.successivo: #finché la variabile ultimo_pianeta non ha un None come puntatore (quindi da quando si hanno almeno 2 pianeti in lista si attiva il ciclo)
                ultimo_pianeta = ultimo_pianeta.successivo #aggiorna la variabile ultimo_pianeta con il puntatore del nodo precedente
            ultimo_pianeta.successivo = pianeta_aggiunto #aggiorna il puntatore del pianeta corrente con il nuovo pianeta aggiunto
    
    def VisualizzaPianeti(self):
        pianeta_corrente = self.testa
        while pianeta_corrente: #finché pianeta corrente non è None
            print(pianeta_corrente.nome)
            pianeta_corrente = pianeta_corrente.successivo
            

lista_pianeti = LinkedListPianeti()

lista_pianeti.AggiungiPianeta('Saturno')
lista_pianeti.AggiungiPianeta('Venere')
lista_pianeti.AggiungiPianeta('Marte')
lista_pianeti.AggiungiPianeta('Giove')
lista_pianeti.AggiungiPianeta('Locorotondo')

lista_pianeti.VisualizzaPianeti()