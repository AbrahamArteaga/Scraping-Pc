from json import *
import os


cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
# print("Files in %r: %s" % (cwd, files))
direccion = f"{cwd}\\datosA\\datos_"


def leer(nombre):
    with open(f"{direccion}{nombre}.json", "r") as lectura_archivo:
        return load(lectura_archivo)


def escribir(nombre, datos_archivo):
    datos_archivo = dumps(datos_archivo)
    almacenamiento = open(f"{direccion}{nombre}.json", "w")
    almacenamiento.write(datos_archivo)

