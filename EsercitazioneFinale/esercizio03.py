'''Il Pattern Singleton funziona generalmente nascondendo il costruttore della classe e fornendo un metodo statico che restituisce una sola istanza di questa classe (vedendo se esiste già un'istanza della classe e altrimenti creandone una)

   Crea una classe ComputerCentrale che implementa il pattern Singleton, cioè creando più istanze della stessa classe esse si riferiscano allo stesso oggetto:
   1. La classe deve avere un attributo di classe privato _istanza = None e dovrei implementare __new__() che crea un'istanza nuova se non esiste già (basandosi sul valore _istanza)
   2. Impostare due attributi di istanza stato = "in attesa" motori = "spenti", non è necessario usare __init__ tutto si svolgerà in __new()__
   3. Implementa metodo di istanza StatoAstronave(self) che visualizza il valore corrente stato e motori
   4. Implementa un metodo di istanza AvviaMotori(self) che imposta motori = "accesi" e stato = "in movimento" e un metodo di istanza SpegniMotori che fa il contrario
   5. Creare due istanze e verifica che sono la stessa cosa
   5.1 visualizza lo stato del primo computer centrale
   5.2 avvia i motori sul primo
   5.3 analizza lo stato del secondo computer centrale
   5.4 spegni i motori sul secondo computer
   5.5 visualizza lo stato del primo
   '''

class ComputerCentrale:
    _istanza = None
    
    def __new__(cls):
        if cls._istanza is None: #si usa cls._instance perché è un attributo di classe
            cls._istanza = super().__new__(cls)
            cls._istanza.stato = "in attesa"
            cls._istanza.motori = "spenti"       
        return cls._istanza #se l'istanza è stata creata si bypassa l'if e si ritorna l'istanza già creata
    
    def StatoAstronave(self):
        print(f"stato: {self.stato}, motori: {self.motori}")
        
    def AvviaMotori(self):
        self.stato = "in movimento"
        self.motori = "accesi"
        
    def SpegniMotori(self):
        self.stato = "in attesa"
        self.motori = "spenti"
        
    
c1 = ComputerCentrale()
c2 = ComputerCentrale()

print(c1.stato)
print(c2.stato)
print(c1.motori)
print(c2.motori)
print(c1.stato == c2.stato)
print(c1.motori == c2.motori)

c1.StatoAstronave()
c2.StatoAstronave()

c1.AvviaMotori()

c2.StatoAstronave()
c1.StatoAstronave()

c1.SpegniMotori()

c2.StatoAstronave()
c1.StatoAstronave()