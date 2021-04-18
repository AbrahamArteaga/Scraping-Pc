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


class ListaEnlazadasCircularesDobles:

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

        dato = Nodo(data)
        if not self.primero:
            self.primero = dato
            self.ultimo = dato
            return 0
        dato.previo = self.ultimo
        self.ultimo.siguiente = dato
        self.ultimo = dato
        return None

    def leer_elemento_posicion_k(self, k):
        pass

    def insertar_elemento_posicion_k(self, k):
        pass

    def eliminar_elemento_posicion_k(self, k):
        pass

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