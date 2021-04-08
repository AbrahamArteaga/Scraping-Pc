import json

archivo = open("Scrap/JsonGenerados/datos_CPU.json", "r")
traduccion = archivo.read()
diccinarios = json.loads(traduccion)


def datos_diccionario(numeroid):
    datos_del_diccionario = [(diccinarios[numeroid]["id"]), (diccinarios[numeroid]["nombre"]),
                           (diccinarios[numeroid]['marca']), (diccinarios[numeroid]['linea']),
                           (diccinarios[numeroid]['generacion']), (diccinarios[numeroid]['valor'])]
    hilo = ' '.join(map(str, datos_del_diccionario))
    print(hilo)


for i in range(30):
    datos_diccionario(i)
