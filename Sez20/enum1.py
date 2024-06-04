"""Modellare schema di classificazione per
colori primari RGB. Chiameremo i colori RED, GREEN, BLUE"""

from enum import Enum

class ColorePrimario(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# la classe ColorePrimario è sottoclasse di Enum

