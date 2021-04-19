"""
Modulo de interfaz, encargado de ejecutar
la comunicación entre el usuario y la aplicación.

Modulos que se importan: busquedas.py
"""

from busquedas import *


def pedir_info(texto, *opciones):

    """
    Pedir info es la funcion que sirve como interfaz,
    esta tiene como parametros una linea de texto
    y una cantidad indefinida de opciones
    que el usuario puede elegir
    """

    print(texto)
    count = 0
    for i in opciones:
        count += 1
        print(str(count) + ") " + i)
    numero_respuesta = int(input())
    return opciones[numero_respuesta - 1]


def datos_cpu():

    """
    Esta funcion es la encargada
    de realizar las busquedas de CPU
    """

    marca = pedir_info("Seleccione una marca: ", "Intel", "AMD")

    if marca == "Intel":
        linea = pedir_info("Seleccione la linea: ", "Pentium", "Core i3",
                           "Core i5", "Core i7", "Core i9")
        generacion = pedir_info("Seleccione la generacion:", "8va generacion",
                                "9na generacion", "10ma generacion", "11va generacion")
    else:
        linea = pedir_info("seleccione la linea: ", "Athlon", "Ryzen 3",
                           "Ryzen 5", "Ryzen 7", "Ryzen 9")
        generacion = pedir_info("Seleccione la generacion:", "Ryzen 1000", "Ryzen 2000",
                                "Ryzen 3000", "Ryzen 5000")
    estado = pedir_info("Seleccione el estado del componente", "Nuevo", "Solo abierto")
    garantia = pedir_info("Seleccione la garantia minima: ", "Garantia 6 Meses", "Garantia 1 año",
                          "Garantia 2 años", "Garantia de por vida")

    print("Se empieza a buscar el procesador bajo los parametros:" + "\nMarca: ", marca +
          "\nLinea: ", linea + "\nGeneracion: ", generacion + "\nEstado: ", estado + "\nGarantia: ", garantia)

    buscar_cpu()


def datos_gpu():

    """
    Esta funcion es la encargada de realizar
    las busquedas de Tarjetas Graficas
    """

    marca = pedir_info("Seleccione la marca: ", "Nvidia", "AMD")

    if marca == "Nvidia":
        linea = pedir_info("Seleccione la serie: ", "Serie 10", "Serie 16",
                           "Serie 20", "Serie 30")
        modelo = pedir_info("Seleccione el modelo:", f"{linea}50", f"{linea}50ti", f"{linea}60",
                            f"{linea}60ti", f"{linea}70", f"{linea}70ti", f"{linea}80ti")
    else:
        linea = pedir_info("Seleccione la linea: ", "Radeon RX 3000", "Radeon RX 4000",
                           "Radeon RX 5000", "Radeon RX 6000")
        modelo = pedir_info("Seleccione el modelo:", "300", "400", "500", "600", "700")
    estado = pedir_info("Seleccione el estado del componente", "Nuevo", "Solo abierto")
    garantia = pedir_info("Seleccione la garantia minima: ", "Garantia 6 Meses",
                          "Garantia 1 año", "Garantia 2 años", "Garantia de por vida")

    print("Se empieza a buscar el GPU bajo los parametros:" + "\nMarca: ", marca +
          "\nLinea: ", linea + "\nModelo: ", modelo + "\nEstado: ", estado + "\nGarantia: ",
          garantia)
    buscar_gpu()


def datos_ram():

    """
    Esta funcion es la encargada de
    realizar las busquedas de memoria RAM
    """

    marca = pedir_info("Seleccione la marca: ", "Crucial", "HyperX", "Corsair")

    capacidad = pedir_info("Seleccione la capacidad: ", "2 GB", "4 GB", "8 GB", "16 GB")
    frecuencia = pedir_info("Seleccione el la frecuencia: ", "2400 Mhz",
                            "2777 Mhz", "3000 Mhz", "3200 Mhz")
    estado = pedir_info("Seleccione el estado del componente", "Nuevo", "Solo abierto")
    garantia = pedir_info("Seleccione la garantia minima: ", "Garantia 6 Meses", " Garantia 1 año",
                          "Garantia 2 años", "Garantia de por vida")

    print("Se empieza a buscar la memoria RAM bajo los parametros:" + "\nMarca: ", marca +
          "\nCapacidad: ", capacidad + "\nFrecuencia: ", frecuencia + "\nEstado: ", estado +
          "\nGarantia: ", garantia)
    buscar_ram()


def datos_mother():

    """
    Esta funcion es la encargada de
    realizar las busquedas de placas madre
    """

    marca = pedir_info("Seleccione la marca: ", "Aorus", "ASRock", "Msi", "Gigabyte",
                       "Asus", "ROG")
    socket = pedir_info("Seleccione la marca: ", "LGA", "AM4")
    estado = pedir_info("Seleccione el estado del componente", "Nuevo", "Solo abierto")
    garantia = pedir_info("Seleccione la garantia minima: ", "Garantia 6 Meses",
                          "Garantia 1 año", "Garantia 2 años", "Garantia de por vida")
    print("Se empieza a buscar la memoria motherboard bajo los parametros:" + "\nMarca: ", marca +
          "\nSocket: ", socket + "\nEstado: ", estado + "\nGarantia: ", garantia)
    buscar_mother()


def datos_psu():

    """
    Esta funcion es la encargada de
    realizar las busquedas de memoria RAM
    """

    marca = pedir_info("Seleccione la marca: ", "Aorus", "ASRock", "Msi", "Gigabyte",
                       "Asus", "ROG")
    potencia = pedir_info("Seleccione la potencia: ", "400W", "500W", "600W", "700W",
                          "800W", "900W", "1000W")
    certificacion = pedir_info("Seleccione la certificacion: ", "80+ White", "80+ Bronze",
                               "80+ Silver", "80+ Gold", "80+ Platinum", "80+ Titanium")
    estado = pedir_info("Seleccione el estado del componente", "Nuevo", "Solo abierto")
    garantia = pedir_info("Seleccione la garantia minima: ", "Garantia 6 Meses", " Garantia 1 año",
                          "Garantia 2 años", "Garantia de por vida")
    print("Se empieza a buscar la memoria motherboard bajo los parametros:" + "\nMarca: ",
          marca + "\nPotencia: ", potencia + "\nCertificacion: ", certificacion + "\nEstado: ",
          estado + "\nGarantia: ", garantia)
    buscar_psu()


def datos_disco():

    """
    Esta funcion es la encargada de
    realizar las busquedas de memoria RAM
    """

    marca = pedir_info("Seleccione la marca: ", "SanDisk", "Kingston", "Samsung", "Adata",
                       "Crucial", "WD")
    capacidad = pedir_info("Seleccione la capacidad: ", "250 GB", "500 GB", "1 TB", "2TB", "4 TB")
    tipo = pedir_info("Seleccione el tipo de almacenamiento: ", "HDD", "SSD", "NVME M.2")
    estado = pedir_info("Seleccione el estado del componente", "Nuevo", "Solo abierto")
    garantia = pedir_info("seleccione la garantia minima: ", "Garantia 6 Meses", " Garantia 1 año",
                          "Garantia 2 años", "Garantia de por vida")
    print("Se empieza a buscar la memoria motherboard bajo los parametros:" + "\nMarca: ", marca +
          "\nCapacidad: ", capacidad + "\nTipo: ", tipo + "\nEstado: ", estado +
          "\nGarantia: ", garantia)
