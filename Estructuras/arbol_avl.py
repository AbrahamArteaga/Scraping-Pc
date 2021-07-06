"Implementación de un Arbol AVL"


class Nodo:

    """
    Nombre de clase: Nodo
    Usado para ser un nodo
    de un Arbol tipo AVL
    """

    def __init__(self, data):
        self.data = data
        self.izquierda = None
        self.derecha = None
        self.altura = 0
        self.contador = 0


class ArbolAVL:

    """
    Nombre de Clase: Arbol AVL
    Funciones: obtener_altura,
    obtener_diferencia, obtener_dato_menor,
    calcular_altura, insertar, eliminar,
    rotacion_dd,rotacion_di,rotacion_ii
    rotacion_id
    """


    def obtener_altura(self, nodo):

        """
        Función: obtener_altura
        Retorna la altura
        de donde se ecnuentra un nodo.
        Argumentos: nodo
        """

        if not nodo:
            return 0
        return nodo.altura

    def obtener_diferencia(self, nodo):

        """
        Función: obtener_diferencia
        Calcula la diferencia
        que haya entre un nodo
        y sus dos hijos, si no los tiene
        se asume la diferencia como 0.
        Argumentos: Nodo
        """

        if not nodo:
            return 0
        if not nodo.izquierda and not nodo.derecha:
            return 0
        if not nodo.izquierda:
            return 0 - (self.obtener_altura(nodo.derecha) + 1)
        if not nodo.derecha:
            return self.obtener_altura(nodo.izquierda) + 1
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)

    def obtener_dato_menor(self, nodo):

        """
        Función: obtener_dato_menor
        Retorna el nodo con el valor
        mas pequeño.
        Argumentos: Nodo
        """

        if not nodo or not nodo.izquierda:
            return nodo
        return self.obtener_dato_menor(nodo.izquierda)

    def calcular_altura(self, nodo):
        """
        Función: Nodo
        Calcula la altura a la
        cual se haya un nodo.
        Argumentos: Nodo
        """
        return max(self.obtener_altura(nodo.derecha), self.obtener_altura(nodo.izquierda)) + 1

    def insertar(self, data, raiz):
        """
        Función:insertar
        Inserta un valor en el
        arbol.
        Argumentos: Data, Raíz
        """
        if not raiz:
            return Nodo(data)
        elif data < raiz.data:
            raiz.izquierda = self.insertar(data, raiz.izquierda)
        else:
            raiz.derecha = self.insertar(data, raiz.derecha)

        raiz.altura = self.calcular_altura(raiz)
        diferencia = self.obtener_diferencia(raiz)

        if diferencia < -1:
            if self.obtener_diferencia(raiz.derecha) < 0:
                return self.rotacion_dd(raiz)
            else:
                return self.rotacion_di(raiz)
        elif diferencia > 1:
            if self.obtener_diferencia(raiz.izquierda) > 0:
                return self.rotacion_ii(raiz)
            else:
                return self.rotacion_id(raiz)
        return raiz

    def eliminar(self, data, raiz):
        """
        Función: Eliminar
        Elimina un nodo del
        arbol
        Argumentos: Data y Raíz
        """
        if not raiz:
            return raiz
        elif data < raiz.data:
            raiz.izquierda = self.eliminar(data, raiz.izquierda)
        elif data > raiz.data:
            raiz.derecha = self.eliminar(data, raiz.derecha)
        else:
            if not raiz.derecha:
                tem = raiz.izquierda
                raiz = None
                return tem
            elif not raiz.izquierda:
                tem = raiz.derecha
                raiz = None
                return tem
            else:
                tem = self.obtener_dato_menor(raiz.derecha) # El menor dato de la derecha
                raiz.data = tem.data
                raiz.derecha = self.eliminar(tem.data, raiz.derecha)
        if not raiz:
            return raiz
        elif not raiz.derecha and not raiz.izquierda:
            raiz.altura = 0
        else:
            raiz.altura = 1 + max(self.obtener_altura(raiz.izquierda),
                                    self.obtener_altura(raiz.derecha))

        diferencia = self.obtener_diferencia(raiz)

        if diferencia < -1:
            if self.obtener_diferencia(raiz.derecha) < 0:
                return self.rotacion_dd(raiz)
            else:
                return self.rotacion_di(raiz)
        elif diferencia > 1:
            if self.obtener_diferencia(raiz.izquierda) > 0:
                return self.rotacion_ii(raiz)
            else:
                return self.rotacion_id(raiz)
        return raiz

    def rotacion_dd(self, nodo):
        """
        Función: rotacion_dd
        Hace que el arbol
        efectue una rotación
        derecha derecha.
        Argumentos: Nodo
        """
        tem = nodo.derecha
        nodo.derecha = tem.izquierda
        tem.izquierda = nodo
        if not nodo.derecha and not nodo.izquierda:
            nodo.altura = 0
        else:
            nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda),
                                    self.obtener_altura(nodo.derecha))
        tem.altura = 1 + max(self.obtener_altura(tem.derecha),
                             self.obtener_altura(tem.derecha))
        return tem

    def rotacion_ii(self, nodo):
        """
        Función: rotacion_ii
        Hace que el arbol
        efectue una rotación
        izquierda izquierda.
        Argumentos: Nodo
        """
        tem = nodo.izquierda
        nodo.izquierda = tem.derecha
        tem.derecha = nodo
        if not nodo.derecha and not nodo.izquierda:
            nodo.altura = 0
        else:
            nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda),
                                    self.obtener_altura(nodo.derecha))
        tem.altura = 1 + max(self.obtener_altura(tem.derecha),
                             self.obtener_altura(tem.izquierda))
        return tem

    def rotacion_id(self, nodo):
        """
        Función: rotacion_id
        Hace que el arbol
        efectue una rotación
        izquierda derecha.
        Argumentos: Nodo
        """
        nodo.izquierda = self.rotacion_dd(nodo.izquierda)
        return self.rotacion_ii(nodo)

    def rotacion_di(self, nodo):
        """
        Función: rotacion_di
        Hace que el arbol
        efectue una rotación
        derecha izquierda.
        Argumentos: Nodo
        """
        nodo.derecha = self.rotacion_ii(nodo.derecha)
        return self.rotacion_dd(nodo)
