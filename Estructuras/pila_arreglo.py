"""
Modulo de la clase Pila
aqui implementamos
nuestra propia Pila
"""


class Pila:

    """
    Nombre de clase: Pila
    Atributos: cabeza, stack
    Metodos: obtener_cabeza, agregar
             remover, __str__, __len__
    """

    def __init__(self):
        self.cabeza = None
        self.stack = []

    def obtener_cabeza(self):

        """
        Esta funcion retorna
        la cabeza de la pila,
        mas no la elimina.
        """
        if self.cabeza != None:
            return self.cabeza

    def enpilar(self, elemento):

        """
        Esta funcion agrega
        datos a nuestra pila
        """

        self.cabeza = elemento
        self.stack.append(elemento)

    def desenpilar(self):

        """
        Remueve solamente la cabeza,
        si la lista esta vacia
        retorna valor Falso
        """

        if self.cabeza is None:
            pass
        else:
            self.stack.pop()
            if len(self.stack) > 0:
                self.cabeza = self.stack[-1]
            else:
                self.cabeza = None

    def esta_vacia(self):
        pass

    def vaciar(self):
        pass

    def imprimir(self):
        pass

    def __str__(self):
        return str(self.stack)

    def __len__(self):
        return len(self.stack)

