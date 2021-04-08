import json
import random

Procesador = ["Intel", "AMD"]
Procesador1 = ["Pentium", "Core i3", "Core i5", "Core i7", "Core i9"]
Procesador1a = ["8va generacion", "9na generacion", "10ma generacion"]
Procesador2 = ["Athlon", "Ryzen 3", "Ryzen 5", "Ryzen 7", "Ryzen 9"]
Procesador2b = ["Ryzen 2000", "Ryzen 3000", "Ryzen 5000"]
ProcesadorT = [" Nuevo", "", " Solo abierto"]
ProcesadorH = [" Garantia 6 Meses", " Garantia 3 Meses", ""]


def main(veces):
    datos = []

    def generar(tipo):

        marca = random.choice(Procesador)
        if marca == "Intel":
            linea = random.choice(Procesador1)
            generacion = random.choice(Procesador1a)
        else:
            linea = random.choice(Procesador2)
            generacion = random.choice(Procesador2b)

        tipo = {
            "id": str(tipo).zfill(4),
            "nombre": "Procesador" + " " + linea + random.choice(ProcesadorT) + random.choice(ProcesadorH),
            "marca": marca,
            "linea": linea,
            "generacion": generacion,
            "valor": random.randrange(400000, 1300000, 10000)
        }
        datos.append(tipo)

    for contador in range(1, veces + 1):
        generar(contador)

    print(datos)
    data_string = json.dumps(datos)
    print(data_string)

    a = open("Scrap/JsonGenerados/datos_CPU.json", "w")
    a.write(data_string)
    a.close()


main(200)
