"Implementación de arbol"

from Estructuras.cola_arreglo import *


class Arbol:
    """
    Clase: Arbol
    Funciones:annadir_hijo_ord,
    annadir_hijo,es_hoja,
    dato_en_hijos,imprimir_arbol
    buscar_por_indice
    """
    def __init__(self, dato):
        self.dato = dato
        self.hijos = []

    def annadir_hijo_ord(self, dato):
        """
        Añade un hijo dato
        en orden al arbol.
        Argumentos: dato
        """
        dato = Arbol(dato)
        self.hijos.append(dato)
        sorted(self.hijos, key=lambda x: x.dato)
        return dato

    def annadir_hijo(self, dato):
        """
        Añade un hijo
        al arbol.
        Argumentos: dato
        """
        dato = Arbol(dato)
        self.hijos.append(dato)
        return dato

    def es_hoja(self):
        """
        es_hoja
        Retorna true
        si el nodo es una hoja,
        false si no lo es.
        """
        if len(self.hijos) == 0:
            return True
        return False

    def dato_en_hijos(self, dato):
        """
        Retorna el dato
        que tengan los hijos
        en de un nodo.
        Argumentos: dato
        """
        for i in range(len(self.hijos)):
            if dato == self.hijos[i].dato:
                return i
        return -1

    def imprimir_arbol(self):
        """
        Imprime el valor
        de cada nodo en
        el arbol
        """
        cola = Cola()
        print(self.dato)
        for hijo in self.hijos:
            cola.enfilar(hijo)
        while cola.longitud() > 0:
            n = cola.desenfilar()
            print(n.dato, end=", ")
            if len(n.hijos) > 0:
                for hijo in n.hijos:
                    cola.enfilar(hijo)

    def buscar_por_indice(self, indice):
        """
        Buscara un nodo
        por indice y retornara
        el valor de este:
        Argumentos: Indice
        """
        if len(indice) == 1:
            return self.hijos[indice[0]]
        indice = indice[1:]
        return self.buscar_por_indice(*indice)
