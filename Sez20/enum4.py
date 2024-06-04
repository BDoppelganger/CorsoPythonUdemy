from enum import Enum

class Stagione(Enum):
    PRIMAVERA = 1
    ESTATE = 2
    AUTUNNO = 3
    INVERNO = 4
    
    def descrizione(self): #metodo di istanza descrizione che combina un dizionario con un'istruzione di accesso a un elemento del dizionario per restituire descrizione di membri
        return {
            Stagione.PRIMAVERA: "Il tempo si riscalda", #le chiavi sono i membri e i valori la descrizione
            Stagione.ESTATE: "Tempo di spiaggia",
            Stagione.AUTUNNO: "le foglie cadono",
            Stagione.INVERNO: "neve e ghiaccio"
        }[self] #questo self serve ad accedere al valore del dizionario e rappresenta l'istanza su cui il metodo descrizione viene chiamato
        
stagione_corrente = Stagione.ESTATE
print(stagione_corrente.descrizione()) #invoca il metodo descrizione, che deve essere invocato su un'istanza specifica
