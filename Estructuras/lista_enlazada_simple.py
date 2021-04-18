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

    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar_final(self, data):
        dato = Nodo(data)
        if not self.primero:
            self.primero = dato
            self.ultimo = dato
            return 0
        self.ultimo.siguiente = dato

    def leer_elemento_posicion_k(self, k):
        pass

    def insertar_elemento_posicion_k(self, k):
        pass

    def eliminar_elemento_posicion_k(self, k):
        pass

    def guardar_lista(self):
        guardar = ""
        nodo_actual = self.primero
        while nodo_actual:
            guardar += str(nodo_actual.data) + " "
            nodo_actual = nodo_actual.siguiente
        guardar += "\n"
        return guardar

