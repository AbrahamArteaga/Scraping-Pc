"""
Modulo encargado de ejecutar las querys de busqueda
en la base de datos, funciona mediante JSON.
"""
from lector_datos import *
from main import *
from main import componentes_arbol
from Estructuras.arbol_avl import *


def buscar(*parametros):
    """
    Buscara en la base de datos
    toddo lo relacionado a CPU
    """

    parametros = parametros[0]
    if parametros[0] == "Mother Board":
        parametros[0] = "MOTHER"
    if parametros[0] == "Unidad de almacenamiento":
        parametros[0] = "ROM"
    datosb = leer(parametros[0])
    inicio = time()
    for datob in datosb:
        idc = list(map(int, datob.get(f"id {parametros[0]}").split("-")))
        if (parametros[1] < 1 or parametros[1] == idc[0]) and (parametros[2] < 1 or parametros[2] == idc[1]) and \
                (parametros[3] < 1 or parametros[3] == idc[2]):
            print(datob)
            for instancia in datob.get("instancias"):
                if (parametros[4] == "Todos los estados" or instancia.get("estado") == parametros[4]) and \
                        (parametros[5] == "Todas las garantias minimas" or instancia.get("garantia")
                         == parametros[5]):
                    print(instancia)
    fin = time()
    print(f"T buscar = {fin-inicio}")


def buscar_en_arbol(*parametros):
    arbol = ArbolAVL()
    raiz = None
    parametros = parametros[0]
    inicio = time()
    # print(parametros)
    datos = []
    if parametros[1] == -1:
        for i in componentes_arbol.hijos[parametros[0]].hijos:
            for j in i.hijos:
                for k in j.hijos:
                    # print(k.hijos[0].dato)
                    raiz = buscar_intancias(k.hijos[0].dato.get("instancias"), parametros[4], parametros[5],
                                            k.hijos[0].dato, parametros[6], raiz)
    elif parametros[2] == -1:
        for i in componentes_arbol.hijos[parametros[0]].hijos[parametros[1]].hijos:
            if parametros[3] == -1:
                for j in i.hijos:
                    componente_escogido = j.hijos[0].dato
                    # print(componente_escogido)
                    raiz = buscar_intancias(componente_escogido.get("instancias"), parametros[4], parametros[5],
                                     componente_escogido, parametros[6], raiz)
            else:
                componente_escogido = i.hijos[parametros[3]].hijos[0].dato
                # print(componente_escogido)
                raiz = buscar_intancias(componente_escogido.get("instancias"), parametros[4], parametros[5],
                                 componente_escogido, parametros[6], raiz)
    elif parametros[3] == -1:
        for i in componentes_arbol.hijos[parametros[0]].hijos[parametros[1]].hijos[parametros[2]].hijos:
            componente_escogido = i.hijos[0].dato
            # print(componente_escogido)
            raiz = buscar_intancias(componente_escogido.get("instancias"), parametros[4], parametros[5],
                                    componente_escogido, parametros[6], raiz)
    else:
        componente_escogido = componentes_arbol.hijos[parametros[0]].hijos[parametros[1]].hijos[parametros[2]].\
            hijos[parametros[3]].hijos[0].dato
        # print(componente_escogido)
        raiz = buscar_intancias(componente_escogido.get("instancias"), parametros[4], parametros[5],
                                 componente_escogido, parametros[6], raiz)

    fin = time()
    print(f"T buscar en arbol = {fin - inicio}")
    if type(raiz) == list:
        return raiz
    datos = arbol.guardar_inorder(raiz, datos)
    return datos


def buscar_intancias(d_instancias, estado, garantia, componente, orden, raiz):
    datos_instancias = leer(f"{d_instancias}instancias")
    arbol = ArbolAVL()
    datos = []
    if orden == "Sin orden":
        for dato_instancia in datos_instancias:
            if (estado == "Todos los estados" or dato_instancia.get("estado") == estado) \
                    and (garantia == "Todas las garantias minimas" or dato_instancia.get("garantia") == garantia):
                datos.append([dato_instancia, componente])
                # print(dato_instancia)
        return datos
    elif orden == "Precio":
        for dato_instancia in datos_instancias:
            if (estado == "Todos los estados" or dato_instancia.get("estado") == estado) \
                    and (garantia == "Todas las garantias minimas" or dato_instancia.get("garantia") == garantia):
                raiz = arbol.insertar(dato_instancia.get("dia/precio")[1], raiz, [dato_instancia, componente])
    elif orden == "Alfabéticamente tienda":
        for dato_instancia in datos_instancias:
            if (estado == "Todos los estados" or dato_instancia.get("estado") == estado)\
                     and (garantia == "Todas las garantias minimas" or dato_instancia.get("garantia") == garantia):
                raiz = arbol.insertar(dato_instancia.get("tienda"), raiz, [dato_instancia, componente])
    return raiz



















