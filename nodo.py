"""
Este es el Modulo nodo.
"""

class Nodo:

    """
    Nombre de clase: Nodo
    Atributos: data, siguiente, previo
    Metodos: Constructor
    """

    def __init__(self, data):
        self.data = data
        self.siguiente = None
        self.previo = None
