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


def converir_a_lista_enlazada(lista):
    lis = ListaEnlazadaSimple()
    for dato in lista:
        lis.insertar_final(dato)
    return lis


class ListaEnlazadaSimple:

    """
    Nombre: ListaEnlazadaSimple
    Atributos: Primero, Ultimo
    Metodo: insertar_final, guardar_lista
    """

    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.longitud = -1

    def insertar_final(self, data):

        """
        Metodo encargado de insertar un dato
        al final de la lista enlazada simple
        """

        dato = Nodo(data)
        if not self.primero:
            self.primero = dato
            self.ultimo = dato
            self.longitud += 1
            return 0
        self.ultimo.siguiente = dato
        self.ultimo = self.ultimo.siguiente
        self.longitud += 1

    def eliminar_final(self):
        if self.longitud > 0:
            k = self.longitud
            contador = 0
            nodo_actual = self.primero
            while contador < k - 1:
                contador += 1
                nodo_actual = nodo_actual.siguiente
            data = nodo_actual.siguiente.data
            nodo_actual.siguiente = None
            self.longitud -= 1
            return data
        elif self.longitud == 0:
            dato = self.primero
            self.primero = None
            self.ultimo = None
            self.longitud = 0
            return dato
        return "no se pueden eliminar elementos en una lista vacia"

    def actualizar_dato(self, k, data):
        contador = 0
        nodo_actual = self.primero
        while contador < k - 1:
            contador += 1
            if nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            else:
                return "la posicion esta fuera de rango"
        nodo_actual.data = data
        return 0

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
        nod = Nodo(data)
        if not self.primero:
            if k == 0:
                self.primero = nod
                self.ultimo = nod
                self.longitud += 1
                return 0
            else:
                return "la posicion esta fuera de rango"
        if k == 0:
            nod.siguiente = self.primero
            self.primero = nod
            return 0
        contador = 0
        nodo_actual = self.primero
        while contador < k-1:
            contador += 1
            if nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            else:
                return "la posicion esta fuera de rango"
        nod.siguiente = nodo_actual.siguiente
        nodo_actual.siguiente = nod
        self.longitud += 1
        return 0

    def eliminar_elemento_posicion_k(self, k):
        if self.longitud > 0:
            if k == 0 and self.primero.siguiente:
                data = self.primero.data
                self.primero = self.primero.siguiente
                return data
            contador = 0
            nodo_actual = self.primero
            while contador < k-1:
                contador += 1
                if k <= self.longitud and nodo_actual.siguiente:
                    nodo_actual = nodo_actual.siguiente
                else:
                    return "la posicion esta fuera de rango"
            if nodo_actual.siguiente.siguiente:
                data = nodo_actual.siguiente.data
                nodo_actual.siguiente = nodo_actual.siguiente.siguiente
                self.longitud -= 1
            else:
                data = nodo_actual.siguiente.data
                nodo_actual.siguiente = None
                self.longitud -= 1
            return data
        elif self.longitud == 0:
            if k != self.longitud:
                return "la posicion esta fuera de rango"
            else:
                dato = self.primero
                self.primero = None
                self.ultimo = None
                self.longitud = 0
                return dato
        return "no se pueden eliminar elementos en una lista vacia"

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

