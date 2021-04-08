"""
Modulo encargado de leer la informacion
de los JSON de cada componente
"""

import json

RUTA = "datos_cpu.json"
cpus = json.load(open(RUTA))

print(type(cpus))
