class Nodo:
    def __init__(self, data):
        self.data = data
        self.izquierda = None
        self.derecha = None
        self.altura = 0
        self.contador = 0


class ArbolAVL:

    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def obtener_diferencia(self, nodo):
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
        if not nodo or not nodo.izquierda:
            return nodo
        return self.obtener_dato_menor(nodo.izquierda)

    def calcular_altura(self, nodo):
        return max(self.obtener_altura(nodo.derecha), self.obtener_altura(nodo.izquierda)) + 1

    def insertar(self, data, raiz):
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
                tem = self.obtener_dato_menor(raiz.derecha) # el menor dato de la derecha
                raiz.data = tem.data
                raiz.derecha = self.eliminar(tem.data, raiz.derecha)
        if not raiz:
            return raiz
        elif not raiz.derecha and not raiz.izquierda:
            raiz.altura = 0
        else:
            raiz.altura = 1 + max(self.obtener_altura(raiz.izquierda), self.obtener_altura(raiz.derecha))

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
        tem = nodo.derecha
        nodo.derecha = tem.izquierda
        tem.izquierda = nodo
        if not nodo.derecha and not nodo.izquierda:
            nodo.altura = 0
        else:
            nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha))
        tem.altura = 1 + max(self.obtener_altura(tem.derecha), self.obtener_altura(tem.derecha))
        return tem

    def rotacion_ii(self, nodo):
        tem = nodo.izquierda
        nodo.izquierda = tem.derecha
        tem.derecha = nodo
        if not nodo.derecha and not nodo.izquierda:
            nodo.altura = 0
        else:
            nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha))
        tem.altura = 1 + max(self.obtener_altura(tem.derecha), self.obtener_altura(tem.izquierda))
        return tem

    def rotacion_id(self, nodo):
        nodo.izquierda = self.rotacion_dd(nodo.izquierda)
        return self.rotacion_ii(nodo)

    def rotacion_di(self, nodo):
        nodo.derecha = self.rotacion_ii(nodo.derecha)
        return self.rotacion_dd(nodo)


