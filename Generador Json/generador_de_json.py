"""
Modulo generador encargado de crear
los JSON de los componentes
"""

import json
import random

total = [

    [
        "Nuevo",
        "Solo abierto",
        "Usado"
    ],

    [
        "Garantia 6 Meses",
        "Garantia 1 año",
        "Garantia 1 Meses",
        "Garantia 2 Meses",
        "Garantia 3 Meses",
        "Sin garantia"
    ],

    # cpu
    [
        ["Intel", "AMD"],

        ["Pentium", "Core i3", "Core i5", "Core i7", "Core i9"],
        ["8va generacion", "9na generacion", "10ma generacion", "11va generacion"],

        ["Athlon", "Ryzen 3", "Ryzen 5", "Ryzen 7", "Ryzen 9"],
        ["Ryzen 1000", "Ryzen 2000", "Ryzen 3000", "Ryzen 5000"]
    ],
    # gpu
    [
        ["Nvidia", "AMD"],

        ["Serie 10", "Serie 16", "Serie 20", "Serie 30"],
        ["Nvidia50", "Nvidia50ti", "Nvidia60", "Nvidia60ti", "Nvidia70",
         "Nvidia70ti", "Nvidia80ti"],

        ["Radeon RX 3000", "Radeon RX 4000", "Radeon RX 5000", "Radeon RX 6000"],
        ["300", "400", "500", "600", "700"]
    ],
    # ram
    [
        ["Crucial", "HyperX", "Corsair"],
        ["2 GB", "4 GB", "8 GB", "16 GB"],
        ["2400 Mhz", "2777 Mhz", "3000 Mhz", "3200 Mhz"]
    ],
    # mother
    [
        ["Aorus", "ASRock", "Msi", "Gigabyte", "Asus", "ROG"],
        ["LGA", "AM4"]
    ],
    # psu
    [
        ["Aorus", "ASRock", "Msi", "Gigabyte", "Asus", "ROG"],
        ["400W", "500W", "600W", "700W", "800W", "900W", "1000W"],
        ["80+ White", "80+ Bronze", "80+ Silver", "80+ Gold", "80+ Platinum", "80+ Titanium"]
    ],
    # disco
    [
        ["SanDisk", "Kingston", "Samsung", "Adata", "Crucial", "WD"],
        ["250 GB", "500 GB", "1 TB", "2TB", "4 TB"],
        ["HDD", "SSD", "NVME M.2"]
    ]
]


def generar_cpu(veces, terminacion, nombre, codigo_de_producto):
    """
    Funcion encargada de generar los JSON
    de la CPU
    """

    datos = []

    def generar(tipo):

        marca = random.choice(total[2][0])
        if marca == "Intel":
            linea = random.choice(total[2][1])
            generacion = random.choice(total[2][2])
        else:
            linea = random.choice(total[2][3])
            generacion = random.choice(total[2][4])

        estado = random.choice(total[0])
        if marca == "Usado":
            garantia = "Sin garantia"
        else:
            garantia = random.choice(total[1])
        tipo = {
            "id": codigo_de_producto + str(tipo).zfill(4),
            "nombre": nombre,
            "marca": marca,
            "linea": linea,
            "generacion": generacion,
            "valor": random.randrange(400000, 1300000, 10000),
            "Estado": estado,
            "Garantia": garantia
        }
        datos.append(tipo)

    for contador in range(1, veces + 1):
        generar(contador)
    data_string = json.dumps(datos)
    almacenamiento_cpu = open("Scraping-Pc/JsonGenerados/datos_" + terminacion + ".json", "w")
    almacenamiento_cpu.write(data_string)
    almacenamiento_cpu.close()


def generar_gpu(veces, terminacion, nombre, codigo_de_producto):
    """
    Funcion encargada de generar los JSON
    de la GPU
    """

    datos = []

    def generar(tipo):
        marca = random.choice(total[3][0])
        if marca == "Intel":
            linea = random.choice(total[3][1])
            generacion = random.choice(total[3][2])
        else:
            linea = random.choice(total[3][3])
            generacion = random.choice(total[3][4])
        estado = random.choice(total[0])
        if marca == "Usado":
            garantia = "Sin garantia"
        else:
            garantia = random.choice(total[1])
        tipo = {
            "id": codigo_de_producto + str(tipo).zfill(4),
            "nombre": nombre,
            "marca": marca,
            "linea": linea,
            "generacion": generacion,
            "valor": random.randrange(300000, 1200000, 10000),
            "Estado": estado,
            "Garantia": garantia
        }
        datos.append(tipo)

    for contador in range(1, veces + 1):
        generar(contador)
    data_string = json.dumps(datos)
    almacenamiento_gpu = open("Scraping-Pc/JsonGenerados/datos_" + terminacion + ".json", "w")
    almacenamiento_gpu.write(data_string)
    almacenamiento_gpu.close()


def generar_ram(veces, terminacion, nombre, codigo_de_producto):
    """
    Funcion encargada de generar los JSON
    de la RAM
    """

    datos = []

    def generar(tipo):

        marca = random.choice(total[4][0])
        capacidad = random.choice(total[4][1])
        frecuencia = random.choice(total[4][2])

        estado = random.choice(total[0])
        if marca == "Usado":
            garantia = "Sin garantia"
        else:
            garantia = random.choice(total[1])
        tipo = {
            "id": codigo_de_producto + str(tipo).zfill(4),
            "nombre": nombre,
            "marca": marca,
            "capacidad": capacidad,
            "frecuencia": frecuencia,
            "valor": random.randrange(120000, 500000, 50000),
            "Estado": estado,
            "Garantia": garantia
        }
        datos.append(tipo)

    for contador in range(1, veces + 1):
        generar(contador)
    data_string = json.dumps(datos)
    almacenamiento_ram = open("Scraping-Pc/JsonGenerados/datos_" + terminacion + ".json", "w")
    almacenamiento_ram.write(data_string)
    almacenamiento_ram.close()


def generar_psu(veces, terminacion, nombre, codigo_de_producto):
    """
    Funcion encargada de generar los JSON
    de la PSU
    """

    datos = []

    def generar(tipo):

        marca = random.choice(total[6][0])
        capacidad = random.choice(total[6][1])
        frecuencia = random.choice(total[6][2])

        estado = random.choice(total[0])
        if marca == "Usado":
            garantia = "Sin garantia"
        else:
            garantia = random.choice(total[1])
        tipo = {

            "id": codigo_de_producto + str(tipo).zfill(4),
            "nombre": nombre,
            "marca": marca,
            "Potencia": capacidad,
            "Certificacion": frecuencia,
            "valor": random.randrange(100000, 400000, 10000),
            "Estado": estado,
            "Garantia": garantia
        }
        datos.append(tipo)

    for contador in range(1, veces + 1):
        generar(contador)
    data_string = json.dumps(datos)
    almacenamiento_psu = open("Scraping-Pc/JsonGenerados/datos_" + terminacion + ".json", "w")
    almacenamiento_psu.write(data_string)
    almacenamiento_psu.close()


def generar_rom(veces, terminacion, nombre, codigo_de_producto):
    """
    Funcion encargada de generar los JSON
    de la ROM
    """

    datos = []

    def generar(tipo):

        marca = random.choice(total[7][0])
        capacidad = random.choice(total[7][1])
        frecuencia = random.choice(total[7][2])

        estado = random.choice(total[0])
        if marca == "Usado":
            garantia = "Sin garantia"
        else:
            garantia = random.choice(total[1])
        tipo = {

            "id": codigo_de_producto + str(tipo).zfill(4),
            "nombre": nombre,
            "marca": marca,
            "Capacidad": capacidad,
            "Tipo": frecuencia,
            "valor": random.randrange(150000, 450000, 25000),
            "Estado": estado,
            "Garantia": garantia
        }
        datos.append(tipo)

    for contador in range(1, veces + 1):
        generar(contador)
    data_string = json.dumps(datos)
    almacenamiento_rom = open("Scraping-Pc/JsonGenerados/datos_" + terminacion + ".json", "w")
    almacenamiento_rom.write(data_string)
    almacenamiento_rom.close()


def generar_mother(veces, terminacion, nombre, codigo_de_producto):
    """
    Funcion encargada de generar los JSON
    de la mother board
    """

    datos = []

    def generar(tipo):

        marca = random.choice(total[5][0])
        capacidad = random.choice(total[5][1])

        estado = random.choice(total[0])
        if marca == "Usado":
            garantia = "Sin garantia"
        else:
            garantia = random.choice(total[1])
        tipo = {

            "id": codigo_de_producto + str(tipo).zfill(4),
            "nombre": nombre,
            "marca": marca,
            "Socket": capacidad,
            "valor": random.randrange(170000, 600000, 10000),
            "Estado": estado,
            "Garantia": garantia
        }
        datos.append(tipo)

    for contador in range(1, veces + 1):
        generar(contador)
    data_string = json.dumps(datos)
    almacenamiento_mother = open("Scraping-Pc/JsonGenerados/datos_" + terminacion + ".json", "w")
    almacenamiento_mother.write(data_string)
    almacenamiento_mother.close()


generar_cpu(50, "CPU", "Procesador", "1")
generar_gpu(50, "GPU", "Tarjeta Grafica", "2")
generar_ram(50, "RAM", "Tarjeta Ram", "3")
generar_mother(50, "MOTHER", "Tarjeta Madre", "4")
generar_psu(50, "PSU", "Fuente", "5")
generar_rom(50, "ROM", "Disco Duro", "6")
