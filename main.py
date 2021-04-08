"""
Modulo principal de Scraping-PC

Autor Original: Manuel

Ultima Revision: 6/04/2021

Modulos que se importan: interfaz.py

"""

import interfaz


def busqueda_componente():
    """
    Dependiendo de que componente elija el usuario,
    se llama a la funcion correspondiente
    """

    componente = interfaz.pedir_info("Elija el componente que desea buscar: ",
                                     "CPU", "GPU", "Tarjeta madre", "PSU", "Modulo RAM")
    if componente == "CPU":
        interfaz.datos_cpu()
    elif componente == "GPU":
        interfaz.datos_gpu()
    elif componente == "Tarjeta madre":
        interfaz.datos_mother()
    elif componente == "PSU":
        interfaz.datos_psu()
    elif componente == "Modulo RAM":
        interfaz.datos_ram()


busqueda_componente()
