def pedirInfo(texto, *opciones):
    #pedir info es la funcion que sirve como interfaz, esta tiene como parametros una linea de texto
    # y una cantidad indefinida de opciones que el usuario puede elegir

    print(texto)
    count = 0
    for i in opciones:
        count += 1
        print(str(count) + ") " + i)
    numeroRespuesta = int(input())
    return opciones[numeroRespuesta-1]

def busquedaComponente():
    #dependiendo de que componente elija el usuario, se llama a la funcion correspondiente
    componente = pedirInfo("Elija el componente que desea buscar: ", "CPU", "GPU", "Tarjeta madre", "PSU", "Modulo RAM")
    if componente == "CPU":
        busquedaCPU()
    elif componente == "GPU":
        busquedaGPU()
    elif componente == "Tarjeta madre":
        busquedaMother()
    elif componente == "PSU":
        busquedaPSU()
    elif componente == "Modulo RAM":
        busquedaRAM()


def busquedaCPU():
    marca = pedirInfo("seleccione la marca: ", "Intel", "AMD")
    if marca == "Intel":
        linea = pedirInfo("seleccione la linea: ", "Pentium", "Core i3", "Core i5", "Core i7", "Core i9")
        generacion = pedirInfo("Seleccione la generacion:", "8va generacion", "9na generacion", "10ma generacion")
    else:
        linea = pedirInfo("seleccione la linea: ", "Athlon", "Ryzen 3", "Ryzen 5", "Ryzen 7", "Ryzen 9")
        generacion = pedirInfo("Seleccione la generacion:", "Ryzen 2000", "Ryzen 3000", "Ryzen 5000")

    print("Se empieza a buscar el procesador bajo los parametros:" + "\nMarca: ",marca +
          "\nLinea: ", linea + "\nGeneracion: ",generacion)

def busquedaGPU():
    marca = pedirInfo("seleccione la marca: ", "Nvidia", "AMD")
    if marca == "Nvidia":
        linea = pedirInfo("seleccione la serie: ", "Serie 10", "Serie 16", "Serie 20", "Serie 30")
        modelo = pedirInfo("Seleccione el modelo:", f"{linea}50", f"{linea}60", f"{linea}70", f"{linea}80")
    else:
        linea = pedirInfo("seleccione la linea: ", "Radeon RX 5000" , "Radeon RX 6000")
        modelo = pedirInfo("Seleccione el modelo:", "300", "500", "Ryzen 700")

    print("Se empieza a buscar el GPU bajo los parametros:" + "\nMarca: ", marca +
          "\nLinea: ", linea + "\nModelo: ", modelo)

def busquedaRAM():
    marca = pedirInfo("seleccione la marca: ", "Crucial", "HyperX", "Corsair")
    capacidad = pedirInfo("seleccione la capacidad: ", "2 GB", "4 GB", "8 GB", "16 GB")
    frecuencia = pedirInfo("Seleccione el la frecuencia: " , "2400 Mhz", "2777 Mhz", "3000 Mhz", "3200 Mhz")


    print("Se empieza a buscar la memoria RAM bajo los parametros:" + "\nMarca: ", marca +
          "\nCapacidad: ", capacidad + "\nFrecuencia: ", frecuencia)



busquedaComponente()
