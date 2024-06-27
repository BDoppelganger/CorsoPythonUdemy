class CorpoCeleste:
    def __init__(self, nome):
        self.nome = nome
        self.adiacenti = {}

    def aggiungi_collegamento(self, altro_corpo, distanza):
        self.adiacenti[altro_corpo] = distanza

    def rimuovi_collegamento(self, altro_corpo):
        if altro_corpo in self.adiacenti:
            del self.adiacenti[altro_corpo]

    def __str__(self):
        adiacenze = ", ".join([f"{corpo.nome} (distanza: {distanza} UA)" for \
                               corpo, distanza in self.adiacenti.items()])
        return f"{self.nome} -> {adiacenze}"

class MappaStellare:
    def __init__(self):
        self.corpi_celesti = {}

    def aggiungi_corpo_celeste(self, nome):
        corpo = CorpoCeleste(nome)
        self.corpi_celesti[nome] = corpo
        return corpo

    def rimuovi_corpo_celeste(self, nome):
        if nome in self.corpi_celesti:
            for corpo in self.corpi_celesti.values():
                corpo.rimuovi_collegamento(self.corpi_celesti[nome])
            del self.corpi_celesti[nome]

    def aggiungi_percorso(self, nome_a, nome_b, distanza):
        if nome_a in self.corpi_celesti and nome_b in self.corpi_celesti:
            self.corpi_celesti[nome_a] \
                .aggiungi_collegamento(self.corpi_celesti[nome_b], distanza)
            self.corpi_celesti[nome_b] \
                .aggiungi_collegamento(self.corpi_celesti[nome_a], distanza)

    def __str__(self):
        return "\n".join(str(corpo) for corpo in self.corpi_celesti.values())

nomi_pianeti = ["Zyther", "Quaxon", "Woburn", "Vulcan", 
                "Talos", "Sirius", "Remulak", 
                "Orion", "Nebulon", "Krypton"]

mappa = MappaStellare()
for nome in nomi_pianeti:
    mappa.aggiungi_corpo_celeste(nome)

# Creazione manuale delle connessioni
mappa.aggiungi_percorso("Zyther", "Quaxon", 2.5)
mappa.aggiungi_percorso("Quaxon", "Woburn", 3.1)
mappa.aggiungi_percorso("Woburn", "Vulcan", 1.2)
mappa.aggiungi_percorso("Vulcan", "Talos", 4.8)
mappa.aggiungi_percorso("Talos", "Sirius", 2.6)
mappa.aggiungi_percorso("Sirius", "Remulak", 5.0)
mappa.aggiungi_percorso("Remulak", "Orion", 3.3)
mappa.aggiungi_percorso("Orion", "Nebulon", 1.9)
mappa.aggiungi_percorso("Nebulon", "Krypton", 4.4)
mappa.aggiungi_percorso("Krypton", "Zyther", 3.7)

print(mappa)

mappa.rimuovi_corpo_celeste("Quaxon")
print("Rimosso il pianeta Quaxon")
print(mappa)

