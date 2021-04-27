from lector_datos import *

from InterfazGrafica.opciones import *
from datetime import *
from random import *
from os import *
from lector_datos import direccion

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory

hoy = datetime.now()
un_dia = timedelta(days=1)
un_anno = timedelta(days=365)

lista_marca_de_componente = [[OPCIONES_CPU_MARCA, "CPU"], [OPCIONES_GPU_MARCA, "GPU"], [OPCIONES_PSU_MARCA, "PSU"],
                             [OPCIONES_RAM_MARCA, "RAM"], [OPCIONES_MOTHER_BOARD_MARCA, "MOTHER"],
                             [OPCIONES_UNIDAD_ALMACENAMIENTO_MARCA, "ROM"]]


#
# ejemplo = [
#     {
#         "marca": "",
#         "linea": "",
#         "generacion": "",
#         "historial precio": [],
#         "instancias": [
#             {
#                 "tienda": "",
#                 "estado": "",
#                 "garantia": "",
#                 "calificacion": "",
#                 "dia/precio": ""
#             }
#         ]
#
#     }
# ]


def generar_datos(opciones_marca, nombre):
    datos = []
    opcion_uno = []
    opcion_dos = []
    llave1 = ""
    llave2 = ""
    for indice_marca in range(1, len(opciones_marca)):
        if nombre == "CPU":
            llave1 = "linea"
            llave2 = "generacion"
            if opciones_marca[indice_marca] == "Intel":
                opcion_uno = OPCIONES_CPU_LINEA_INTEL
                opcion_dos = OPCIONES_CPU_GENERACION_INTEL
            elif opciones_marca[indice_marca] == "AMD":
                opcion_uno = OPCIONES_CPU_LINEA_AMD
                opcion_dos = OPCIONES_CPU_GENERACION_AMD
        elif nombre == "GPU":
            llave1 = "linea"
            llave2 = "modelo"
            if opciones_marca[indice_marca] == "Nvidia":
                opcion_uno = OPCIONES_GPU_LINEA_NVIDIA
            elif opciones_marca[indice_marca] == "AMD":
                opcion_uno = OPCIONES_CPU_LINEA_AMD
                opcion_dos = OPCIONES_GPU_MODELO_AMD
        elif nombre == "PSU":
            llave1 = "potencia"
            llave2 = "certificacion"
            opcion_uno = OPCIONES_PSU_POTENCIA
            opcion_dos = OPCIONES_PSU_CERTIFICACION
        elif nombre == "RAM":
            llave1 = "capacidad"
            llave2 = "frecuencia"
            opcion_uno = OPCIONES_RAM_CAPACIDAD
            opcion_dos = OPCIONES_RAM_FRECUENCIA
        elif nombre == "MOTHER":
            llave1 = "socket"
            opcion_uno = OPCIONES_MOTHER_BOARD_SOCKET
            for indice_opcion_uno in range(1, len(opcion_uno)):
                dic = {
                    f"id {nombre}": f"{indice_marca}-{indice_opcion_uno}-{0}",
                    "marca": f"{opciones_marca[indice_marca]}",
                    f"{llave1}": f"{opcion_uno[indice_opcion_uno]}",
                    "instancias": f"{nombre}\\{indice_marca}\\{indice_opcion_uno}\\"
                }
                datos.append(dic)
            escribir(nombre, datos)
        elif nombre == "ROM":
            llave1 = "capacidad"
            llave2 = "tipo"
            opcion_uno = OPCIONES_UNIDAD_ALMACENAMIENTO_CAPACIDAD
            opcion_dos = OPCIONES_UNIDAD_ALMACENAMIENTO_TIPO
        if nombre != "MOTHER":
            for indice_opcion_uno in range(1, len(opcion_uno)):
                if opciones_marca[indice_marca] == "Nvidia":
                    serie = opcion_uno[indice_opcion_uno]
                    OPCIONES_GPU_MODELO_NVIDIA = [
                        "Todos los modelos",
                        f"{serie}50",
                        f"{serie}50ti",
                        f"{serie}60",
                        f"{serie}60ti",
                        f"{serie}70",
                        f"{serie}70ti",
                        f"{serie}80ti",
                        f"{serie}90"
                    ]
                    if serie == "30":
                        OPCIONES_GPU_MODELO_NVIDIA.append(f"{serie}90")
                    opcion_dos = OPCIONES_GPU_MODELO_NVIDIA
                for indice_opcion_dos in range(1, len(opcion_dos)):
                    dic = {
                        f"id {nombre}": f"{indice_marca}-{indice_opcion_uno}-{indice_opcion_dos}",
                        "marca": f"{opciones_marca[indice_marca]}",
                        f"{llave1}": f"{opcion_uno[indice_opcion_uno]}",
                        f"{llave2}": f"{opcion_dos[indice_opcion_dos]}",
                        "instancias": f"{nombre}\\{indice_marca}\\{indice_opcion_uno}\\{indice_opcion_dos}\\"
                    }
                    datos.append(dic)
                escribir(nombre, datos)


def historial_precio(nombre, precio_minimo, precio_maximo, salto_precio):
    datos_archivo = leer(nombre)
    for dato in datos_archivo:
        historial = []
        for i in range(365):
            dia = hoy - un_anno + timedelta(days=i)
            precio = randrange(precio_minimo, precio_maximo, salto_precio)
            historial.append([dia.strftime("%d-%m-%y"), precio])
        d = dato.get("instancias")
        if path.exists(f"{direccion}{d}"):
            escribir(f"{d}historial_precio", historial)
        else:
            makedirs(f"{direccion}{d}")
            escribir(f"{d}historial_precio", historial)


def actualizar_dia(nombre, precio_minimo, precio_maximo, salto_precio):
    tiendas = [
        "Amazon",
        "PC componentes",
        "Alkosto",
        "Mercado libre",
        "NewEgg"
    ]
    datos_archivo = leer(nombre)
    for dato in datos_archivo:
        instacias = []
        for j in range(100):
            instacia = {
                "tienda": choice(tiendas),
                "estado": choice(OPCIONES_ESTADO[2:]),
                "garantia": choice(OPCIONES_GARANTIA_MINIMA[2:]),
                "calificacion": randrange(0, 100, 1),
                "dia/precio": [hoy.strftime("%d-%m-%y"), randrange(precio_minimo, precio_maximo, salto_precio)]
            }
            instacias.append(instacia)
        d = dato.get("instancias")
        if path.exists(f"{direccion}{d}"):
            escribir(f"{d}instancias", instacias)
        else:
            makedirs(f"{direccion}{d}")
            escribir(f"{d}instancias", instacias)


"falta agregar el dato con el menor precio al historial de precios en la funcion acutalizar dia"

for tupla in lista_marca_de_componente:
    # if tupla[1] == "MOTHER":
    generar_datos(tupla[0], tupla[1])
    actualizar_dia(tupla[1], 400000, 3300000, 10000)
    historial_precio(tupla[1], 400000, 3300000, 10000)

