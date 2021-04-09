"""
Modulo principal de la GUI
"""

from tkinter import *
from tkinter.ttk import *
from tkinter.font import *
from opciones import *

"""
Funciones
"""

def rgb(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'







"""
    dimensiones ventana
"""
altura = 600
ancho = 800


"""
    raiz ventana
"""
raiz = Tk()
raiz.title("Scraping-PCs")
# raiz.iconbitmap("ruta.ico")
# raiz.geometry(f"{ancho}x{altura}")

# Permite o no que la ventana se pueda redimensionar
raiz.resizable(False, False)



"""
    pestañas
"""
pestannas = Notebook(raiz)
pestannas.pack(fill="both", expand="yes")

pestanna_principal = Frame(height=f"{altura}", width=f"{ancho}")
pestanna_principal.pack()
pestannas.add(pestanna_principal, text="Scraping-PCs")

pestanna_busqueda = Frame(height=f"{altura}", width=f"{ancho}")
pestanna_busqueda.pack()
pestannas.add(pestanna_busqueda, text="Buscar componentes")

pestanna_favoritos = Frame(height=f"{altura}", width=f"{ancho}")
pestanna_favoritos.pack()
pestannas.add(pestanna_favoritos, text="Favoritos")

pestanna_historial = Frame(height=f"{altura}", width=f"{ancho}")
pestanna_historial.pack()
pestannas.add(pestanna_historial, text="Historial")



"""
    pestaña principal
"""
estilo_de_fuente = Font(size=40)
etiqueta = Label(pestanna_principal, text="Scraping-PCs", font=estilo_de_fuente)
etiqueta.place(relx=0.5, rely=0.3, anchor=CENTER)



"""
    pestaña de busqueda
"""


def establecer_componente(componente):
    if componente == "CPU":
        pass
    elif componente == "GPU":
        pass
    elif componente == "PSU":
        pass
    elif componente == "Mother Board":
        pass
    elif componente == "RAM":
        pass
    elif componente == "Unidad de almacenamiento":
        pass


variable_componentes = StringVar(pestanna_busqueda)
variable_componentes.set(OPCIONES_COMPONENTES[0])
boton_menu_componente = OptionMenu(pestanna_busqueda, variable_componentes,
                                   *OPCIONES_COMPONENTES, command=establecer_componente)
boton_menu_componente.config(width=20)
boton_menu_componente.place(relx=0.01, rely=0.2)


def establecer_marca(marca):
    pass


variable_marca_cpu = StringVar(pestanna_busqueda)
variable_componentes.set(OPCIONES_CPU_MARCA[0])
boton_menu_marca_cpu = OptionMenu(pestanna_busqueda, variable_marca_cpu,
                                  *OPCIONES_CPU_MARCA, command=establecer_marca)
boton_menu_marca_cpu.config(width=20)
boton_menu_componente.place(x=0.51, rely=0.2)


"""
    pestaña de favoritos
"""




raiz.mainloop()
