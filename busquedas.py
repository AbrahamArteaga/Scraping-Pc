"""
Modulo encargado de ejecutar las querys de busqueda
en la base de datos, funciona mediante JSON.
"""
from lector_datos import *


def buscar(*parametros):
    """
    Buscara en la base de datos
    todo lo relacionado a CPU
    """

    parametros = parametros[0]
    if parametros[0] == "Mother Board":
        parametros[0] = "MOTHER"
        datos = leer(parametros[0])
    if parametros[0] == "Unidad de almacenamiento":
        parametros[0] = "ROM"
    datos = leer(parametros[0])
    for dato in datos:
        id = list(map(int, dato.get(f"id {parametros[0]}").split("-")))
        if (parametros[1] < 1 or parametros[1] == id[0]) and (parametros[2] < 1 or parametros[2] == id[1]) and \
                (parametros[3] < 1 or parametros[3] == id[2]):
                for instancia in dato.get("instancias"):
                    if (parametros[4] == "Todos los estados" or instancia.get("estado") == parametros[4]) and \
                            (parametros[5] == "Todas las garantias minimas" or instancia.get("garantia") == parametros[5]):
                        print(instancia)

                # print(dato.get(f"id {parametros[0]}"))



