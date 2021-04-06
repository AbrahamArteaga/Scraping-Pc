import json

ruta = "datos_cpu.json"
cpus = json.load(open(ruta))

print(type(cpus))
