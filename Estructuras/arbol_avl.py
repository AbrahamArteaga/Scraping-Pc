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
        return self.obtener_altura(nodo.izquierda) - self.obtener_altura(nodo.derecha)

    def calcular_altura(self, nodo):
        if not nodo.derecha and nodo.izquierda:
            return 0
        elif not nodo.derecha:
            return nodo.izquierda.altura + 1
        elif not nodo.izquierda:
            return nodo.derecha.altura + 1
        else:
            return max(nodo.derecha.altura, nodo.izquierda.altura) + 1

    def insertar(self, data, raiz):
        if not raiz:
            return Nodo(data)
        elif data < raiz.data:
            raiz.izquierda = self.insertar(data, raiz.izquierda)
        else:
            raiz.derecha = self.insertar(data, raiz.derecha)

        raiz.altura = self.calcular_altura(raiz)

        if self.obtener_diferencia(raiz) < -1:
            if self.obtener_diferencia(raiz.derecha) <= 0:
                return self.rotacion_dd(raiz)
            else:
                return self.rotacion_di(raiz)
        elif self.obtener_diferencia(raiz) > 1:
            if self.obtener_diferencia(raiz.izquierda) >= 0:
                return self.rotacion_ii(raiz)
            else:
                return self.rotacion_id(raiz)
        return raiz

    def eliminar(self, data):
        pass

    def rotacion_dd(self, nodo):
        tem = nodo.derecha
        nodo.derecha = tem.izquierda
        tem.izquierda = nodo
        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha))
        tem.altura = 1 + max(self.obtener_altura(nodo), self.obtener_altura(tem.derecha))
        return tem

    def rotacion_ii(self, nodo):
        tem = nodo.izquierda
        nodo.izquierda = tem.derecha
        tem.derecha = nodo
        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierda), self.obtener_altura(nodo.derecha))
        tem.altura = 1 + max(self.obtener_altura(nodo), self.obtener_altura(tem.izquierda))
        return tem

    def rotacion_id(self, nodo):
        nodo.izquierda = self.rotacion_dd(nodo.izquierda)
        return self.rotacion_ii(nodo)

    def rotacion_di(self, nodo):
        nodo.derecha = self.rotacion_ii(nodo.derecha)
        return self.rotacion_dd(nodo)


arbol = ArbolAVL()

raiz = None
for i in range(10):
    raiz = arbol.insertar(i, raiz)

print()
