"""
Modulo principal de la GUI
"""

from tkinter import *
from tkinter.ttk import *
from tkinter.font import *


def rgb(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'


def establecer_marca(marca):
    if marca == "Todas las marcas":
        pass
    elif marca == "Intel":
        pass
    elif marca == "AMD":
        pass


def establecer_componente(valor):
    if valor == "CPU":
        boton_menu_marca_cpu = OptionMenu(pestanna_busqueda, variable_marca_cpu,
                                          *OPCIONES_CPU_MARCA, command=establecer_marca)
        boton_menu_marca_cpu.config(width=20)
        boton_menu_marca_cpu.pack(side="left", anchor=NW, pady=50)
        boton_menu_componente.place(x=0.51, rely=0.2)
        print(1)
    elif componente == "GPU":
        pass
    elif componente == "PSU":
        pass
    elif componente == "Mother Board":
        pass
    elif componente == "RAM":
        pass
    pass


componente = "Escoger componente"

OPCIONES_COMPONENTES = [
    "Escoger componente",
    "CPU",
    "GPU",
    "PSU",
    "Mother Board",
    "RAM"
]

OPCIONES_CPU_MARCA = [
    "Todas las marcas",
    "Todas las marcas",
    "Intel",
    "AMD"
]

OPCIONES_CPU_LINEA = [
    "Cualquiera",
    "Cualquiera",
    "Pentium",
    "Core i3",
    "Core i5",
    "Core i7",
    "Core i9"
]
OPCIONES_CPU_GENERACION = [
    "Cualquiera",
    "Cualquiera",
    "8va generacion",
    "9na generacion",
    "10ma generacion"
]
OPCIONES_CPU_ESTADO = [
    "Cualquiera",
    "Cualquiera",
    "Athlon",
    "Ryzen 3",
    "Ryzen 5",
    "Ryzen 7",
    "Ryzen 9"
]
OPCIONES_CPU_GARANTIA = [
    "Cualquiera",
    "Cualquiera",
]

altura = 600
ancho = 800

raiz = Tk()
# raiz.geometry(f"{ancho}x{altura}")
raiz.title("Scraping-PCs")
# raiz.iconbitmap("ruta.ico")

# Permite o no que la ventana se pueda redimensionar
raiz.resizable(False, False)

pestannas = Notebook(raiz)
pestannas.pack(fill="both", expand="yes")


pestanna_principal = Frame(height=f"{altura}", width=f"{ancho}")
pestanna_principal.pack()
estilo_de_fuente = Font(size=40)
etiqueta = Label(pestanna_principal, text="Scraping-PCs", font=estilo_de_fuente)
etiqueta.place(relx=0.5, rely=0.3, anchor=CENTER)
pestannas.add(pestanna_principal, text="Scraping-PCs")


pestanna_busqueda = Frame(height=f"{altura}", width=f"{ancho}")
pestanna_busqueda.pack()




variable_componentes = StringVar(pestanna_busqueda)
# valor por defecto
variable_componentes.set(OPCIONES_COMPONENTES[0])

variable_marca_cpu = StringVar(pestanna_busqueda)
# valor por defecto
variable_componentes.set(OPCIONES_CPU_MARCA[0])


boton_menu_componente = OptionMenu(pestanna_busqueda, variable_componentes,
                                   *OPCIONES_COMPONENTES, command=establecer_componente)
boton_menu_componente.config(width=20)
boton_menu_componente.place(relx=0.01, rely=0.2)
# boton_menu_componente.pack(side="left", anchor=NW, pady=50)


pestannas.add(pestanna_busqueda, text="Buscar componentes")


pestanna_favoritos = Frame(height=f"{altura}", width=f"{ancho}")
pestanna_favoritos.pack()

pestannas.add(pestanna_favoritos, text="Favoritos")


pestanna_historial = Frame(height=f"{altura}", width=f"{ancho}")
pestanna_historial.pack()

pestannas.add(pestanna_historial, text="Historial")





raiz.mainloop()
