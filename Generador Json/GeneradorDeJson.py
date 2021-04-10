import json
import random

total =[

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

            #cpu
        [
            ["Intel", "AMD"],

            ["Pentium","Core i3","Core i5", "Core i7", "Core i9"],
            ["8va generacion","9na generacion", "10ma generacion", "11va generacion"],

            ["Athlon", "Ryzen 3","Ryzen 5", "Ryzen 7", "Ryzen 9"],
            ["Ryzen 1000", "Ryzen 2000","Ryzen 3000", "Ryzen 5000"]
        ],
            #gpu
        [
            ["Nvidia", "AMD"],

            ["Serie 10", "Serie 16","Serie 20", "Serie 30"],
            ["Nvidia50", "Nvidia50ti", "Nvidia60", "Nvidia60ti","Nvidia70", "Nvidia70ti", "Nvidia80ti"],

            ["Radeon RX 3000", "Radeon RX 4000", "Radeon RX 5000","Radeon RX 6000"],
            ["300", "400", "500", "600", "700"]
        ],
            #ram
        [
            ["Crucial", "HyperX", "Corsair"],
            ["2 GB", "4 GB", "8 GB", "16 GB"],
            ["2400 Mhz","2777 Mhz", "3000 Mhz", "3200 Mhz"]
        ],
            #mother
        [
            ["Aorus", "ASRock", "Msi", "Gigabyte", "Asus", "ROG"],
            ["LGA", "AM4"]
        ],
            #psu
        [
            ["Aorus", "ASRock", "Msi", "Gigabyte", "Asus", "ROG"],
            ["400W", "500W", "600W", "700W", "800W", "900W", "1000W"],
            ["80+ White", "80+ Bronze", "80+ Silver", "80+ Gold","80+ Platinum", "80+ Titanium"]
        ],
            #disco
        [
            ["SanDisk", "Kingston", "Samsung", "Adata", "Crucial", "WD"],
            ["250 GB", "500 GB", "1 TB", "2TB", "4 TB"],
            ["HDD", "SSD", "NVME M.2"]
        ] 
    ]

def CPU(veces,Termnacion,nombre,CODIGOPRO):   
    datos=[]
    def generar (tipo):

        marca = random.choice(total[2][0])
        if marca == "Intel":
            linea = random.choice(total[2][1])
            generacion = random.choice(total[2][2])
        else:
            linea = random.choice(total[2][3])
            generacion = random.choice(total[2][4])
 
        Estado = random.choice(total[0])
        if marca == "Usado":
            Garantia = "Sin garantia"
        else:
            Garantia = random.choice(total[1])
        tipo = {
            "id":CODIGOPRO+str(tipo).zfill(4),
            "nombre":nombre,
            "marca": marca,
            "linea":linea,
            "generacion":generacion,
            "valor": random.randrange(400000, 1300000,10000),
            "Estado": Estado,
            "Garantia": Garantia
        } 
        datos.append(tipo)

    for contador in range(1,veces+1) :
        generar(contador)
    data_string = json.dumps(datos)
    a = open("Scraping-Pc/JsonGenerados/datos_"+ Termnacion +".json", "w")
    a.write(data_string)
    a.close()
def GPU(veces,Termnacion,nombre,CODIGOPRO):   
    datos=[]
    def generar (tipo):
        marca = random.choice(total[3][0])
        if marca == "Intel":
            linea = random.choice(total[3][1])
            generacion = random.choice(total[3][2])
        else:
            linea = random.choice(total[3][3])
            generacion = random.choice(total[3][4])
        Estado = random.choice(total[0])
        if marca == "Usado":
            Garantia = "Sin garantia"
        else:
            Garantia = random.choice(total[1])
        tipo = {
            "id":CODIGOPRO+str(tipo).zfill(4),
            "nombre":nombre,
            "marca": marca,
            "linea":linea,
            "generacion":generacion,
            "valor": random.randrange(300000, 1200000,10000),
            "Estado": Estado,
            "Garantia": Garantia
        } 
        datos.append(tipo)

    for contador in range(1,veces+1) :
        generar(contador)
    data_string = json.dumps(datos)
    a = open("Scraping-Pc/JsonGenerados/datos_"+ Termnacion +".json", "w")
    a.write(data_string)
    a.close()
def RAM(veces,Termnacion,nombre,CODIGOPRO):   
    datos=[]
    def generar (tipo):

        marca = random.choice(total[4][0])
        capacidad = random.choice(total[4][1])
        frecuencia = random.choice(total[4][2])

        Estado = random.choice(total[0])
        if marca == "Usado":
            Garantia = "Sin garantia"
        else:
            Garantia = random.choice(total[1])
        tipo = {
            "id":CODIGOPRO+str(tipo).zfill(4),
            "nombre":nombre,
            "marca": marca,
            "capacidad":capacidad,
            "frecuencia":frecuencia,
            "valor": random.randrange(120000,500000,50000),
            "Estado": Estado,
            "Garantia": Garantia
        } 
        datos.append(tipo)

    for contador in range(1,veces+1) :
        generar(contador)
    data_string = json.dumps(datos)
    a = open("Scraping-Pc/JsonGenerados/datos_"+ Termnacion +".json", "w")
    a.write(data_string)
    a.close()
def PSU(veces,Termnacion,nombre,CODIGOPRO):   
    datos=[]
    def generar (tipo):

        marca = random.choice(total[6][0])
        capacidad = random.choice(total[6][1])
        frecuencia = random.choice(total[6][2])

        Estado = random.choice(total[0])
        if marca == "Usado":
            Garantia = "Sin garantia"
        else:
            Garantia = random.choice(total[1])
        tipo = {

            "id":CODIGOPRO+str(tipo).zfill(4),
            "nombre":nombre,
            "marca": marca,
            "Potencia":capacidad,
            "Certificacion":frecuencia,
            "valor": random.randrange(100000, 400000,10000),
            "Estado": Estado,
            "Garantia": Garantia
        } 
        datos.append(tipo)

    for contador in range(1,veces+1) :
        generar(contador)
    data_string = json.dumps(datos)
    a = open("Scraping-Pc/JsonGenerados/datos_"+ Termnacion +".json", "w")
    a.write(data_string)
    a.close()
def ROM(veces,Termnacion,nombre,CODIGOPRO):   
    datos=[]
    def generar (tipo):

        marca = random.choice(total[7][0])
        capacidad = random.choice(total[7][1])
        frecuencia = random.choice(total[7][2])

        Estado = random.choice(total[0])
        if marca == "Usado":
            Garantia = "Sin garantia"
        else:
            Garantia = random.choice(total[1])
        tipo = {

            "id":CODIGOPRO+str(tipo).zfill(4),
            "nombre":nombre,

            "marca": marca,
            "Capacidad":capacidad,
            "Tipo":frecuencia,

            "valor": random.randrange(150000, 450000,25000),
            "Estado": Estado,
            "Garantia": Garantia
        } 
        datos.append(tipo)

    for contador in range(1,veces+1) :
        generar(contador)
    data_string = json.dumps(datos)
    a = open("Scraping-Pc/JsonGenerados/datos_"+ Termnacion +".json", "w")
    a.write(data_string)
    a.close()
def MOTHER(veces,Termnacion,nombre,CODIGOPRO):   
    datos=[]
    def generar (tipo):

        marca = random.choice(total[5][0])
        capacidad = random.choice(total[5][1])

        Estado = random.choice(total[0])
        if marca == "Usado":
            Garantia = "Sin garantia"
        else:
            Garantia = random.choice(total[1])
        tipo = {

            "id":CODIGOPRO+str(tipo).zfill(4),
            "nombre":nombre,

            "marca": marca,
            "Socket":capacidad,


            "valor": random.randrange(170000, 600000,10000),
            "Estado": Estado,
            "Garantia": Garantia
        } 
        datos.append(tipo)

    for contador in range(1,veces+1) :
        generar(contador)
    data_string = json.dumps(datos)
    a = open("Scraping-Pc/JsonGenerados/datos_"+ Termnacion +".json", "w")
    a.write(data_string)
    a.close()

CPU(50,"CPU","Procesador","1")
GPU(50,"GPU","Tarjeta Grafica","2")
RAM(50,"RAM","Tarjeta Ram","3")
MOTHER(50,"MOTHER","Tarjeta Madre","4")
PSU(50,"PSU","Fuente","5")
ROM(50,"ROM","Disco Duro","6")
