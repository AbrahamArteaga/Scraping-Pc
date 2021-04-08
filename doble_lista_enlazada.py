"""
Este es el modulo de
doble lista enlazada, aqui
se implementa nuestra
estructura de datos propia
"""


import nodo


class DobleListaEnlazada:

    """
    Nombre: DobleListaEnlazada
    Atributos: Primero, Ultimo
    Metodo: insertar_final, guardar_lista
    """

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar_final(self, data):

        """
        Metodo encargado de insertar un dato
        al final de la doble lista enlazada
        """

        dato = nodo.Nodo(data)
        if not self.primero:
            self.primero = dato
            self.ultimo = dato
            return 0
        dato.previo = self.ultimo
        self.ultimo.siguiente = dato
        self.ultimo = dato
        return None

    def guardar_lista(self):

        """
        Metodo encargado de guardar
        el estado de la lista
        """

        guardar = ""
        nodo_actual = self.primero
        while nodo_actual:
            guardar += str(nodo_actual.data) + " "
            nodo_actual = nodo_actual.siguiente
        guardar += "\n"
        return guardar
