from Estructuras.arbol_avl import *
from time import time
from random import randrange
#
# n = 100000000
#
# """arreglos"""
#
#
# def estadisticas_arreglo(n):
#     print("arreglo")
#     # crear
#
#     arreglo = []
#     tiempo = 0
#     for i in range(n):
#         inicio = time()
#         arreglo.append(i)
#         fin = time()
#         tiempo += fin - inicio
#     crear = "crear", n, tiempo
#     print(tiempo)
#     # print(crear)
#
#     # recorrer
#
#     tiempo = 0
#     inicio = time()
#     for i in arreglo:
#         pass
#     fin = time()
#     tiempo += fin - inicio
#     recorrer = "recorrer", n, tiempo
#     print(tiempo)
#     # print(recorrer)
#
#     # leer
#
#     tiempo = 0
#     for i in range(n):
#         indice = randrange(n)
#         inicio = time()
#         arreglo[indice]
#         fin = time()
#         tiempo += fin - inicio
#     leer = "leer", n, tiempo
#     # print(leer)
#     print(tiempo)
#
#     # actualizar
#
#     tiempo = 0
#     for i in range(n):
#         indice = randrange(n)
#         inicio = time()
#         arreglo[indice] = i
#         fin = time()
#         tiempo += fin - inicio
#     actualizar = "actualizar", n, tiempo
#     # print(actualizar)
#     print(tiempo)
#
#     # insertar
#
#     arreglo = []
#     tiempo = 0
#     for i in range(n):
#         indice = randrange(i + 1)
#         inicio = time()
#         arreglo.insert(indice, i)
#         fin = time()
#         tiempo += fin - inicio
#     insertar = "insertar", n, tiempo
#     # print(insertar)
#     print(tiempo)
#
#     # eliminar
#
#     tiempo = 0
#     for i in range(n):
#         indice = randrange(n - i)
#         inicio = time()
#         arreglo.pop(indice)
#         fin = time()
#         tiempo += fin - inicio
#     eliminar = "eliminar", n, tiempo
#     # print(eliminar)
#     print(tiempo)
#
#
# def estadisticas_lista_enlazada_simple(n):
#     print("lista enlazada simple")
#     # crear
#
#     lista = ListaEnlazadaSimple()
#     tiempo = 0
#     for i in range(n):
#         inicio = time()
#         lista.insertar_final(i)
#         fin = time()
#         tiempo += fin - inicio
#     crear = "crear", n, tiempo
#     print(tiempo)
#
#     # recorrer
#
#     tiempo = 0
#     nodo_actual = lista.primero
#     while nodo_actual:
#         inicio = time()
#         nodo_actual = nodo_actual.siguiente
#         fin = time()
#         tiempo += fin - inicio
#     recorrer = "recorrer", n, tiempo
#     print(tiempo)
#     #
#     # # leer
#     #
#     # tiempo = 0
#     # for i in range(n):
#     #     indice = randrange(n)
#     #     inicio = time()
#     #     lista.leer_elemento_posicion_k(indice)
#     #     fin = time()
#     #     tiempo += fin - inicio
#     # leer = "leer", n, tiempo
#     # print(tiempo)
#     #
#     # # actualizar
#     #
#     # tiempo = 0
#     # for i in range(n):
#     #     indice = randrange(n)
#     #     inicio = time()
#     #     lista.actualizar_dato(indice, i)
#     #     fin = time()
#     #     tiempo += fin - inicio
#     # actualizar = "actualizar", n, tiempo
#     # print(tiempo)
#     #
#     # # insertar
#     #
#     # lista = ListaEnlazadaSimple()
#     # tiempo = 0
#     # for i in range(n):
#     #     indice = randrange(i + 1)
#     #     inicio = time()
#     #     lista.insertar_elemento_posicion_k(indice, i)
#     #     fin = time()
#     #     tiempo += fin - inicio
#     # insertar = "insertar", n, tiempo
#     # print(tiempo)
#
#     # eliminar
#
#     # tiempo = 0
#     # for i in range(n):
#     #     indice = randrange(n - i)
#     #     inicio = time()
#     #     lista.eliminar_elemento_posicion_k(indice)
#     #     fin = time()
#     #     tiempo += fin - inicio
#     # eliminar = "eliminar", n, tiempo
#     # print(tiempo)
#
#
# def estadisticas_lista_enlazada_doble(n):
#     print("lista enlazada doble")
#     # crear
#
#     lista = ListaEnlazadaDoble()
#     tiempo = 0
#     for i in range(n):
#         inicio = time()
#         lista.insertar_final(i)
#         fin = time()
#         tiempo += fin - inicio
#     crear = "crear", n, tiempo
#     print(crear)
#
#     # recorrer
#
#     tiempo = 0
#     nodo_actual = lista.primero
#     while nodo_actual:
#         inicio = time()
#         nodo_actual = nodo_actual.siguiente
#         fin = time()
#         tiempo += fin - inicio
#     recorrer = "recorrer", n, tiempo
#     print(recorrer)
#
#     # leer
#
#     # tiempo = 0
#     # for i in range(n):
#     #     indice = randrange(n)
#     #     inicio = time()
#     #     lista.leer_elemento_posicion_k(indice)
#     #     fin = time()
#     #     tiempo += fin - inicio
#     # leer = "leer", n, tiempo
#     # print(leer)
#     #
#     # # actualizar
#     #
#     # tiempo = 0
#     # for i in range(n):
#     #     indice = randrange(n)
#     #     inicio = time()
#     #     lista.actualizar_dato(indice, i)
#     #     fin = time()
#     #     tiempo += fin - inicio
#     # actualizar = "actualizar", n, tiempo
#     # print(actualizar)
#     #
#     # # insertar
#     #
#     # lista = ListaEnlazadaDoble()
#     # tiempo = 0
#     # for i in range(n):
#     #     indice = randrange(i + 1)
#     #     inicio = time()
#     #     lista.insertar_elemento_posicion_k(indice, i)
#     #     fin = time()
#     #     tiempo += fin - inicio
#     # insertar = "insertar", n, tiempo
#     # print(insertar)
#     #
#     # # eliminar
#     #
#     # tiempo = 0
#     # for i in range(n):
#     #     indice = randrange(n - i)
#     #     inicio = time()
#     #     lista.eliminar_elemento_posicion_k(indice)
#     #     fin = time()
#     #     tiempo += fin - inicio
#     # eliminar = "eliminar", n, tiempo
#     # print(eliminar)
#
#
# def estadisticas_cola_arreglo():
#     print("cola")
#
#     col = Cola()
#     tiempo = 0
#     for i in range(n):
#         inicio = time()
#         col.enfilar(i)
#         fin = time()
#         tiempo += fin - inicio
#     crear = "crear", n, tiempo
#     print(tiempo)
#
#     tiempo = 0
#     for i in range(n):
#         inicio = time()
#         col.desenfilar()
#         fin = time()
#         tiempo += fin - inicio
#     crear = "crear", n, tiempo
#     print(tiempo)
#
#
#
#
# def estadisticas_cola_lista_enlazada():
#     pass
#
#
# def estadisticas_pila_arreglo():
#     pass
#
#
# def estadisticas_pila_lista_enlazada():
#     pass
#
#
# # estadisticas_arreglo(n)
# # estadisticas_lista_enlazada_simple(n)
# # estadisticas_lista_enlazada_doble(n)
# estadisticas_cola_arreglo()
#
# # lista = ListaEnlazadaSimple()
# # tiempo = 0
# # for i in range(1):
# #     lista.insertar_final(i)
# # print(lista.eliminar_elemento_posicion_k(0))
# # print(lista.guardar_lista())
# s = Pila()
# q = Cola()
# for i in range(4):
#     for j in range(4):
#         if (i + j) % 2 == 0:
#             s.enpilar(i+j)
#             print(1)
#             q.enfilar(s.obtener_cabeza())
#         if ((i * 2) + j) % 3 == 0:
#             t = q.obtener_inicial()
#             q.enfilar(s.desenpilar())
#             s.enpilar(t)
#             q.desenfilar()
#
# print(s, q)


"""arbol avl"""

n = 100000000

"""arreglos"""


def estadisticas_avl(n):
    print("avl")
    # crear

    arbol = ArbolAVL()
    # raiz = None
    # tiempo = 0
    # for i in range(n):
    #     inicio = time()
    #     raiz = arbol.insertar(i, raiz)
    #     fin = time()
    #     tiempo += fin - inicio
    # crear = "crear", n, tiempo
    # print(tiempo)
    # # print(crear)

    # insertar

    raiz = None
    tiempo = 0
    for i in range(n):
        indice = randrange(i + 1)
        inicio = time()
        raiz = arbol.insertar(indice, raiz)
        fin = time()
        tiempo += fin - inicio
    insertar = "insertar", n, tiempo
    # print(insertar)
    print(tiempo)

    # eliminar

    tiempo = 0
    for i in range(n):
        indice = randrange(n - i)
        inicio = time()
        raiz = arbol.eliminar(indice, raiz)
        fin = time()
        tiempo += fin - inicio
    eliminar = "eliminar", n, tiempo
    # print(eliminar)
    print(tiempo)


estadisticas_avl(n)
