"""
Modulo de la clase Cola
aqui implementamos
nuestra propia Cola
"""


class Cola:

    """
    Nombre de clase: Pila
    Atributos: inicio, final, fila
    Metodos: obtener_incial, obtener_final, agregar
             remover, __str__, __len__
    """

    def __init__(self):
        self.inicial = None
        self.final = None
        self.fila = []

    def obtener_inicial(self):

        """
        Funcion para obtener
        el incial de la cola
        """

        return self.inicial

    def obtener_final(self):

        """
        Funcion para obtener
        el final de la cola
        """

        return self.final

    def enfilar(self, elemento):

        """
        Funcion para agregar
        datos a la cola.
        """

        self.fila.append(elemento)
        self.final = elemento

    def desenfilar(self):

        """
        Funcion para eliminar el dato
        inicial de la fila
        """

        elemento_desenfilado = self.fila.pop(0)
        if self.longitud() > 0:
            self.inicial = self.fila[0]
        else:
            self.inicial = None
        return elemento_desenfilado

    def esta_vacia(self):
        if self.longitud() == 0:
            return True
        return False

    def vaciar(self):
        self.inicial = None
        self.final = None
        self.fila = []

    def imprimir(self):
        pass

    def __str__(self):
        return str(self.fila)

    def longitud(self):
        return len(self.fila)
