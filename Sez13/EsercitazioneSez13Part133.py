"""Aprire file isolamisteriosa.txt in lettura
Aprire un file di testo in scrittura chiamato output.txt
Leggere il file isolamisteriosa.txt usando readlines() e usa for-in per scorrere la lista
prima di iniziare il loop inizializza un contatore = 1
ad ogni iterazioni scrivi nel secondo file le linee di codice dispari del primo file
aggiungi ad ogni riga dispari il contatore
"""

with open("isolamisteriosa.txt", "rt") as f1, open("output.txt", "w") as f2:
    lines = f1.readlines()
    counter = 1
    for line in lines:
        if counter%2 != 0:
            f2.write(f"{counter}: {line}")
        counter += 1