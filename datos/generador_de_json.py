import json
import random

lista_marcas = ["Intel", "AMD"]
lista_lineas_intel = ["Pentium", "Core i3", "Core i5", "Core i7", "Core i9"]
lista_generaciones_intel = ["8va generacion", "9na generacion", "10ma generacion"]
lista_lineas_amd = ["Athlon", "Ryzen 3", "Ryzen 5", "Ryzen 7", "Ryzen 9"]
lista_generaciones_amd = ["Ryzen 2000", "Ryzen 3000", "Ryzen 5000"]
lista_estados = [" Nuevo", " Solo abierto"]
lista_garantias = [" Garantia 6 Meses", " Garantia 1 año", "Garantia 2 años", "Garantia de por vida"]


def main(veces):
    datos = []

    def generar(tipo):

        marca = random.choice(lista_marcas)
        if marca == "Intel":
            linea = random.choice(lista_lineas_intel)
            generacion = random.choice(lista_generaciones_intel)
        else:
            linea = random.choice(lista_lineas_amd)
            generacion = random.choice(lista_generaciones_amd)

        tipo = {
            "id": str(tipo).zfill(4),
            "nombre": "Procesador" + " " + linea + random.choice(lista_estados) + random.choice(lista_garantias),
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

    a = open("Scrap/JsonGenerados/datos_cpu.json", "w")
    a.write(data_string)
    a.close()


main(200)
