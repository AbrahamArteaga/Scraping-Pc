from Estructuras.cola_arreglo import *


class Arbol:
    def __init__(self, dato):
        self.dato = dato
        self.hijos = []

    def annadir_hijo_ord(self, dato):
        dato = Arbol(dato)
        self.hijos.append(dato)
        sorted(self.hijos, key=lambda x: x.dato)
        return dato

    def annadir_hijo(self, dato):
        dato = Arbol(dato)
        self.hijos.append(dato)
        return dato

    def es_hoja(self):
        if len(self.hijos) == 0:
            return True
        return False

    def dato_en_hijos(self, dato):
        for i in range(len(self.hijos)):
            if dato == self.hijos[i].dato:
                return i
        return -1

    def imprimir_arbol(self):
        q = Cola()
        print(self.dato)
        for hijo in self.hijos:
            q.enfilar(hijo)
        while q.longitud() > 0:
            n = q.desenfilar()
            print(n.dato, end=", ")
            if len(n.hijos) > 0:
                for hijo in n.hijos:
                    q.enfilar(hijo)

    def buscar_por_indice(self, indice):
        if len(indice) == 1:
            return self.hijos[indice[0]]
        indice = indice[1:]
        return self.buscar_por_indice(*indice)
