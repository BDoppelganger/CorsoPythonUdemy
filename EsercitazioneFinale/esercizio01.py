'''1. Creare classe \"Astronave\" che ha come attributi di istanza le sue coordinate x e y nel piano cartesiano 2D, che rappresentano la posizione attuale dell'astronave
   2. Implementare un metodo \"muovi_a(dest_x, dest_y)\" che accetta in input le coordinate di una destinazione e aggiorna la posizione corrente dell'astronave a quella destinazione
   3. Implementare un metodo \"distanza_da(dest_x, dest_y)\" che calcola e restituisce la distanza euclidea tra la posizione attuale e un punto di destinazione specificato'''


import math
  
class Astronave:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def muovi_a(self, dest_x, dest_y):
        self.x = dest_x
        self.y = dest_y
        print(f"Posizione attuale dell'atronave: ({self.x}, {self.y})")
    
    def distanza_da(self, dest_x, dest_y):
        print(f"La distanza tra la posizione attuale dell'astronave e il tuo goal è: {math.dist([self.x, self.y], [dest_x,dest_y])}")

x = 0
y = 0

A1 = Astronave(x, y)

A1.muovi_a(5,5)
A1.distanza_da(0,0)