"""
Modulo principal de Scraping-PC

Autor Original: Manuel

Ultima Revision: 6/04/2021
"""

def pedir_info(texto, *opciones):

    """Pedir info es la funcion que sirve como interfaz,
    esta tiene como parametros una linea de texto
    y una cantidad indefinida de opciones
    que el usuario puede elegir"""

    print(texto)
    count = 0
    for i in opciones:
        count += 1
        print(str(count) + ") " + i)
    numero_respuesta = int(input())
    return opciones[numero_respuesta-1]

def busqueda_componente():

    """
    Dependiendo de que componente elija el usuario, se llama a la funcion correspondiente
    """

    componente = pedir_info("Elija el componente que desea buscar: ",
                            "CPU", "GPU", "Tarjeta madre", "PSU", "Modulo RAM")
    if componente == "CPU":
        busqueda_cpu()
    elif componente == "GPU":
        busqueda_gpu()
    elif componente == "Tarjeta madre":
        busqueda_mother()
    elif componente == "PSU":
        busqueda_psu()
    elif componente == "Modulo RAM":
        busqueda_ram()


def busqueda_cpu():

    """
    Esta funcion es la encargada de realizar las busquedas de CPU
    """

    marca = pedir_info("Seleccione una marca: ", "Intel", "AMD")

    if marca == "Intel":
        linea = pedir_info("Seleccione la linea: ", "Pentium", "Core i3",
                           "Core i5", "Core i7", "Core i9")
        generacion = pedir_info("Seleccione la generacion:", "8va generacion",
                                "9na generacion", "10ma generacion")
    else:
        linea = pedir_info("seleccione la linea: ", "Athlon", "Ryzen 3",
                           "Ryzen 5", "Ryzen 7", "Ryzen 9")
        generacion = pedir_info("Seleccione la generacion:", "Ryzen 2000",
                                "Ryzen 3000", "Ryzen 5000")

    print("Se empieza a buscar el procesador bajo los parametros:" + "\nMarca: ",marca +
          "\nLinea: ", linea + "\nGeneracion: ",generacion)

def busqueda_gpu():

    """
    Esta funcion es la encargada de realizar las busquedas de Tarjetas Graficas
    """

    marca = pedir_info("Seleccione la marca: ", "Nvidia", "AMD")

    if marca == "Nvidia":
        linea = pedir_info("Seleccione la serie: ", "Serie 10", "Serie 16",
                           "Serie 20", "Serie 30")
        modelo = pedir_info("Seleccione el modelo:", f"{linea}50", f"{linea}60",
                            f"{linea}70", f"{linea}80")
    else:
        linea = pedir_info("seleccione la linea: ", "Radeon RX 5000" ,
                          "Radeon RX 6000")
        modelo = pedir_info("Seleccione el modelo:", "300", "500", "Ryzen 700")

    print("Se empieza a buscar el GPU bajo los parametros:" + "\nMarca: ", marca +
          "\nLinea: ", linea + "\nModelo: ", modelo)

def busqueda_ram():

    """
    Esta funcion es la encargada de realizar las busquedas de memoria RAM
    """

    marca = pedir_info("Seleccione la marca: ", "Crucial", "HyperX", "Corsair")

    capacidad = pedir_info("Seleccione la capacidad: ", "2 GB", "4 GB", "8 GB", "16 GB")
    frecuencia = pedir_info("Seleccione el la frecuencia: " , "2400 Mhz",
                            "2777 Mhz", "3000 Mhz", "3200 Mhz")


    print("Se empieza a buscar la memoria RAM bajo los parametros:" + "\nMarca: ", marca +
          "\nCapacidad: ", capacidad + "\nFrecuencia: ", frecuencia)

def busqueda_mother():

    """
    Esta es la funcion encargada de hacer las busquedas de placas madre
    """

    print("Funcion aun en estado WIP")

def busqueda_psu():

    """
    Esta es la busqueda encargada de hacer las busquedas de PSU
    """

    print("Funcion aun en estado WIP")


busqueda_componente()
