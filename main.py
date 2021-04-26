"""
Modulo principal de Scraping-PC

Autor Original: Manuel

Ultima Revision: 6/04/2021

Modulos que se importan: interfaz.py

"""

# from interfaz import *


from time import time
from InterfazGrafica.interfaz_grafica import *
from Estructuras.arboles import *
from Estructuras.lista_enlazada_simple import *
from lector_datos import *


lista_componentes = ["CPU", "GPU", "PSU", "RAM", "MOTHER", "ROM"]
componentes_arbol = Arbol("Componentes")
for componente in lista_componentes:
    datos = leer(componente)
    comp = componentes_arbol.annadir_hijo(componente)
    for dato in datos:
        # historial_precio = converir_a_lista_enlazada(dato.pop("historial precio"))
        # dato["historial precio"] = historial_precio
        idd = list(map(int, dato.get(f"id {componente}").split("-")))
        i_indice = comp.dato_en_hijos(idd[0])
        if i_indice >= 0:
            j_indice = comp.hijos[i_indice].dato_en_hijos(idd[1])
            if j_indice >= 0:
                comp.hijos[i_indice].hijos[j_indice].annadir_hijo_ord(idd[2]).annadir_hijo(dato)
            else:
                comp.hijos[i_indice].annadir_hijo_ord(idd[1]).annadir_hijo_ord(idd[2]).annadir_hijo(dato)
        else:
            comp.annadir_hijo_ord(idd[0]).annadir_hijo_ord(idd[1]).annadir_hijo_ord(idd[2]).annadir_hijo(dato)























































# def buscar_componente():
#
#     """
#     Dependiendo de que componente elija el usuario,
#     se llama a la funcion correspondiente
#     """
#
#     componente = pedir_info("Elija el componente que desea buscar: ",
#                                      "CPU", "GPU", "Tarjeta madre", "PSU", "Modulo RAM")
#     if componente == "CPU":
#         datos_cpu()
#     elif componente == "GPU":
#         datos_gpu()
#     elif componente == "Tarjeta madre":
#         datos_mother()
#     elif componente == "PSU":
#         datos_psu()
#     elif componente == "Modulo RAM":
#         datos_ram()
#
#
# buscar_componente()

