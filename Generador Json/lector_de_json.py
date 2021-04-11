"""
Modulo encargado de leer
la data de los JSON
"""

import json

archivo = open("Scraping-Pc/JsonGenerados/datos_CPU.json","r")
traduccion = archivo.read()
diccinarios = json.loads(traduccion)

keyss=[]
a=diccinarios[0].keys()
for i in a:
    keyss.append(i)

def datos_diccionario(numeroid):

    """
    Funcion encargada de convertir
    la data de los JSON a un solo
    string de informacion
    """

    data_diccionario=[]

    for k in keyss:
        data_diccionario.append(diccinarios[numeroid][k])
    hilo = ' '.join(map(str,data_diccionario))
    print(hilo)

for i in range(50):
    datos_diccionario(i)
