import json

archivo = open("Scrap/JsonGenerados/datos_CPU.json","r")
traduccion = archivo.read()
diccinarios = json.loads(traduccion)

def DatosDicconario(numeroid):
    DatosDelDiccionario=[(diccinarios[numeroid]["id"]),(diccinarios[numeroid]["nombre"]),(diccinarios[numeroid]['marca']),(diccinarios[numeroid]['linea']),(diccinarios[numeroid]['generacion']),(diccinarios[numeroid]['valor'])]
    hilo = ' '.join(map(str,DatosDelDiccionario))
    print(hilo)



for i in range(30):
    DatosDicconario(i)