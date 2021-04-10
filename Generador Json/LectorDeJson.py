import json

archivo = open("Scraping-Pc/JsonGenerados/datos_CPU.json","r")
traduccion = archivo.read()
diccinarios = json.loads(traduccion)

keyss=[]
a=diccinarios[0].keys()
for i in a:
    keyss.append(i)

def DatosDicconario(numeroid):
    DatosDelDiccionario=[]

    for k in keyss:
        DatosDelDiccionario.append(diccinarios[numeroid][k])
    hilo = ' '.join(map(str,DatosDelDiccionario))
    print(hilo)

for i in range(50):
    DatosDicconario(i)
