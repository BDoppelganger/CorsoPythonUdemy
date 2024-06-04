from enum import Enum

class StatoSemaforo(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

print(StatoSemaforo.RED == StatoSemaforo.RED) #True: per confronto identità ottenuto tramite operatori
print(StatoSemaforo.RED == StatoSemaforo.GREEN) #False: per confronto identità ottenuto tramite operatori
print(StatoSemaforo.RED is StatoSemaforo.RED) #True: per confronto con operatore is per vedere se si punta allo stesso oggetto in memoria
print(StatoSemaforo.RED is StatoSemaforo.GREEN) #False: per confronto con operatore is per vedere se si punta allo stesso oggetto in memoria
print(StatoSemaforo.RED == 1) #False: confronto tra membro con un valore perché non c'è corrispondenza tra identità