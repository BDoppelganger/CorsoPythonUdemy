"""Scrivere script che apre il file isolamisteriosa.txt con un context manager:
- in sola lettura
- come file di testo.
Poi usare un loop for-in per scorrere le line di file una linea alla volta
Poi Visualizza la linea di codice del loop a terminale
Utilizza anche un contatore per numerare le linee"""

with open("isolamisteriosa.txt", "rt") as f:
    
    counter = 0
    
    for line in f:
        counter += 1
        line = f.readline()
        print(f"{counter}: {line}")
        