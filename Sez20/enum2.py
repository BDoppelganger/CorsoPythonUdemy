from enum import Enum

class PuntoCardinale(Enum):
    NORD = 'N'
    SUD = 'S'
    EST = 'E'
    OVEST = 'W'
    
for direzione in PuntoCardinale:
    print(f"Nome: {direzione.name}, Valore: {direzione.value}")
    
# puntando agli attributi name e value posso iterare sulla enumeration

direzione_scelta = PuntoCardinale.NORD
if direzione_scelta == PuntoCardinale.NORD:
    print("stai andando verso nord")
    

# si può accedere a uno specifico membro puntando al suo nome come attributo

