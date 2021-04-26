"""
Modulo encargado de ejecutar las querys de busqueda
en la base de datos, funciona mediante JSON.
"""
from lector_datos import *
from main import *
from main import componentes_arbol


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
    parametros = parametros[0]
    inicio = time()
    print(parametros)
    if parametros[1] == -1:
        for i in componentes_arbol.hijos[parametros[0]].hijos:
            for j in i.hijos:
                for k in j.hijos:
                    print(k.hijos[0].dato)
                    buscar_intancias(k.hijos[0].dato.get("instancias"), parametros[4], parametros[5])
    elif parametros[2] == -1:
        for i in componentes_arbol.hijos[parametros[0]].hijos[parametros[1]].hijos:
            if parametros[3] == -1:
                for j in i.hijos:
                    componente_escogido = j.hijos[0].dato
                    print(componente_escogido)
                    buscar_intancias(componente_escogido.get("instancias"), parametros[4], parametros[5])
            else:
                componente_escogido = i.hijos[parametros[3]].hijos[0].dato
                print(componente_escogido)
                buscar_intancias(componente_escogido.get("instancias"), parametros[4], parametros[5])
    elif parametros[3] == -1:
        for i in componentes_arbol.hijos[parametros[0]].hijos[parametros[1]].hijos[parametros[2]].hijos:
            componente_escogido = i.hijos[0].dato
            print(componente_escogido)
            buscar_intancias(componente_escogido.get("instancias"), parametros[4], parametros[5])
    else:
        componente_escogido = componentes_arbol.hijos[parametros[0]].hijos[parametros[1]].hijos[parametros[2]].\
            hijos[parametros[3]].hijos[0].dato
        print(componente_escogido)
        buscar_intancias(componente_escogido.get("instancias"), parametros[4], parametros[5])

    fin = time()
    print(f"T buscar en arbol = {fin - inicio}")


def buscar_intancias(d_instancias, estado, garantia):
    datos_instancias = leer(f"{d_instancias}instancias")
    for dato_instancia in datos_instancias:
        if (estado == "Todos los estados" or dato_instancia.get("estado") == estado)\
                 and (garantia == "Todas las garantias minimas" or dato_instancia.get("garantia") == garantia):
            pass
            # print(dato_instancia)

