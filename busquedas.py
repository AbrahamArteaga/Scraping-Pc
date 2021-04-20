"""
Modulo encargado de ejecutar las querys de busqueda
en la base de datos, funciona mediante JSON.
"""
from lector_datos import *


def buscar_cpu(*parametros):
    """
    Buscara en la base de datos
    todo lo relacionado a CPU
    """
    parametros = parametros[0]
    datos = leer("CPU")
    for dato in datos:
        id = list(map(int, dato.get("id cpu").split("-")))
        if (parametros[0] < 1 or parametros[0] == id[0]) and (parametros[1] < 1 or parametros[1] == id[1]) and \
                (parametros[2] < 1 or parametros[2] == id[2]):
                #\ and (parametros[3] < 2 or parametros[3] == id[3]) and \
                # (parametros[4] < 2 or parametros[4] == id[1]):
            print(dato.get("id cpu"))



def buscar_gpu(*parametros):
    """
    Buscara en la base de datos
    todo lo relacionado a tarjetas
    graficas
    """

    print("Buscar gpus (WIP)")


def buscar_mother(*parametros):
    """
    Buscara en la base de datos
    todo lo relacionado a tarjetas madre
    """

    print("Buscar mother boards (WIP)")


def buscar_psu(*parametros):
    """
    Buscara en la base de datos
    todo lo relacionado a PSU
    """

    print("Buscar psu (WIP)")


def buscar_ram(*parametros):
    """
    Buscara en la base de datos
    todo lo relacionado a mamorias
    RAM
    """

    print("Buscar ram (WIP)")


def buscar_unidad_almacenamiento(*parametros):
    pass

