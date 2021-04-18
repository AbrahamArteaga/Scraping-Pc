"""
Este es el modulo de
lista enlazada simple, aqui
se implementa nuestra
estructura de datos propia
"""


class Nodo:

    """
    Nombre de clase: Nodo
    Atributos: data, siguiente
    Metodos: Constructor
    """

    def __init__(self, data):
        self.data = data
        self.siguiente = None


class ListaEnlazadaSimple:

    """
    Nombre: ListaEnlazadaSimple
    Atributos: Primero, Ultimo
    Metodo: insertar_final, guardar_lista
    """

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar_final(self, data):

        """
        Metodo encargado de insertar un dato
        al final de la lista enlazada simple
        """

        dato = Nodo(data)
        if not self.primero:
            self.primero = dato
            self.ultimo = dato
            return 0
        self.ultimo.siguiente = dato
        self.ultimo = self.ultimo.siguiente

    def leer_elemento_posicion_k(self, k):
        contador = 0
        nodo_actual = self.primero
        while contador < k:
            contador += 1
            if nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            else:
                return "la posicion esta fuera de rango"
        return nodo_actual.data

    def insertar_elemento_posicion_k(self, k, data):
        dato = Nodo(data)
        contador = 0
        nodo_actual = self.primero
        while contador != k - 1:
            contador += 1
            if nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            else:
                return "la posicion esta fuera de rango"
        dato.siguiente = nodo_actual.siguiente
        nodo_actual.siguiente = dato
        return 0

    def eliminar_elemento_posicion_k(self, k):
        contador = 0
        nodo_actual = self.primero
        while contador != k - 1:
            contador += 1
            if nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            else:
                return "la posicion esta fuera de rango"
        if nodo_actual.siguiente.siguiente:
            data = nodo_actual.siguiente.data
            nodo_actual.siguiente = nodo_actual.siguiente.siguiente
        else:
            nodo_actual.siguiente = None
        return data

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

