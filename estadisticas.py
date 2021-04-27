from Estructuras.lista_enlazada_simple import *
from Estructuras.lista_enlazada_doble import *
from Estructuras.lista_enlazada_circular_simple import *
from Estructuras.lista_enlazada_circular_doble import *
from Estructuras.cola_arreglo import *
from Estructuras.cola_lista_enlazada import *
from Estructuras.pila_arreglo import *
from Estructuras.pila_lista_enlazada import *
from time import time
from random import randrange

n = 10000

"""arreglos"""


def estadisticas_arreglo(n):
    print("arreglo")
    # crear

    arreglo = []
    tiempo = 0
    for i in range(n):
        inicio = time()
        arreglo.append(i)
        fin = time()
        tiempo += fin - inicio
    crear = "crear", n, tiempo
    print(crear)

    # recorrer

    tiempo = 0
    inicio = time()
    for i in arreglo:
        pass
    fin = time()
    tiempo += fin - inicio
    recorrer = "recorrer", n, tiempo
    print(recorrer)

    # leer

    tiempo = 0
    for i in range(n):
        indice = randrange(n)
        inicio = time()
        arreglo[indice]
        fin = time()
        tiempo += fin - inicio
    leer = "leer", n, tiempo
    print(leer)

    # actualizar

    tiempo = 0
    for i in range(n):
        indice = randrange(n)
        inicio = time()
        arreglo[indice] = i
        fin = time()
        tiempo += fin - inicio
    actualizar = "actualizar", n, tiempo
    print(actualizar)

    # insertar

    arreglo = []
    tiempo = 0
    for i in range(n):
        indice = randrange(i+1)
        inicio = time()
        arreglo.insert(indice, i)
        fin = time()
        tiempo += fin - inicio
    insertar = "insertar", n, tiempo
    print(insertar)

    # eliminar

    tiempo = 0
    for i in range(n):
        indice = randrange(n - i)
        inicio = time()
        arreglo.pop(indice)
        fin = time()
        tiempo += fin - inicio
    eliminar = "eliminar", n, tiempo
    print(eliminar)


def estadisticas_lista_enlazada_simple(n):
    print("lista enlazada simple")
    # crear

    lista = ListaEnlazadaSimple()
    tiempo = 0
    for i in range(n):
        inicio = time()
        lista.insertar_final(i)
        fin = time()
        tiempo += fin - inicio
    crear = "crear", n, tiempo
    print(crear)

    # recorrer

    tiempo = 0
    nodo_actual = lista.primero
    while nodo_actual:
        inicio = time()
        nodo_actual = nodo_actual.siguiente
        fin = time()
    tiempo += fin - inicio
    recorrer = "recorrer", n, tiempo
    print(recorrer)

    # leer

    tiempo = 0
    for i in range(n):
        indice = randrange(n)
        inicio = time()
        lista.leer_elemento_posicion_k(indice)
        fin = time()
        tiempo += fin - inicio
    leer = "leer", n, tiempo
    print(leer)

    # actualizar

    tiempo = 0
    for i in range(n):
        indice = randrange(n)
        inicio = time()
        lista.actualizar_dato(indice, i)
        fin = time()
        tiempo += fin - inicio
    actualizar = "actualizar", n, tiempo
    print(actualizar)

    # insertar

    lista = ListaEnlazadaSimple()
    tiempo = 0
    for i in range(n):
        indice = randrange(i+1)
        inicio = time()
        lista.insertar_elemento_posicion_k(indice, i)
        fin = time()
        tiempo += fin - inicio
    insertar = "insertar", n, tiempo
    print(insertar)

    # eliminar

    tiempo = 0
    for i in range(n):
        indice = randrange(n - i)
        inicio = time()
        lista.eliminar_elemento_posicion_k(indice)
        fin = time()
        tiempo += fin - inicio
    eliminar = "eliminar", n, tiempo
    print(eliminar)


def estadisticas_lista_enlazada_doble(n):
    print("lista enlazada doble")
    # crear

    lista = ListaEnlazadaDoble()
    tiempo = 0
    for i in range(n):
        inicio = time()
        lista.insertar_final(i)
        fin = time()
        tiempo += fin - inicio
    crear = "crear", n, tiempo
    print(crear)

    # recorrer

    tiempo = 0
    nodo_actual = lista.primero
    while nodo_actual:
        inicio = time()
        nodo_actual = nodo_actual.siguiente
        fin = time()
        tiempo += fin - inicio
    recorrer = "recorrer", n, tiempo
    print(recorrer)

    # leer

    tiempo = 0
    for i in range(n):
        indice = randrange(n)
        inicio = time()
        lista.leer_elemento_posicion_k(indice)
        fin = time()
        tiempo += fin - inicio
    leer = "leer", n, tiempo
    print(leer)

    # actualizar

    tiempo = 0
    for i in range(n):
        indice = randrange(n)
        inicio = time()
        lista.actualizar_dato(indice, i)
        fin = time()
        tiempo += fin - inicio
    actualizar = "actualizar", n, tiempo
    print(actualizar)

    # insertar

    lista = ListaEnlazadaDoble()
    tiempo = 0
    for i in range(n):
        indice = randrange(i+1)
        inicio = time()
        lista.insertar_elemento_posicion_k(indice, i)
        fin = time()
        tiempo += fin - inicio
    insertar = "insertar", n, tiempo
    print(insertar)

    # eliminar

    tiempo = 0
    for i in range(n):
        indice = randrange(n - i)
        inicio = time()
        lista.eliminar_elemento_posicion_k(indice)
        fin = time()
        tiempo += fin - inicio
    eliminar = "eliminar", n, tiempo
    print(eliminar)


estadisticas_arreglo(n)
estadisticas_lista_enlazada_simple(n)
estadisticas_lista_enlazada_doble(n)

# lista = ListaEnlazadaSimple()
# tiempo = 0
# for i in range(5):
#     lista.insertar_final(i)
# print(lista.eliminar_elemento_posicion_k(5))
# print(lista.guardar_lista())
