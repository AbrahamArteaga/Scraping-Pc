"""
Modulo principal de la GUI
"""

"""
Chicos, una vez terminen de usar
los paquetes de importacion en general,
usen from x import y especificando
las clases y funciones que van a usar,
por que los tkinter estan importando
en total 157 funciones y clases.

    ATT: Francisco
    igual no afecta en el rendimiento y no es que haga mas pesado el archivo 
"""

from tkinter import *
from tkinter.ttk import *
from tkinter.font import *
from opciones import *


# Funciones principales de la GUI


def rgb(red, green, blue):

    """
    Estable la gamma RGB
    de la aplicación
    """

    return f'#{red:02x}{green:02x}{blue:02x}'

# Dimensiones de la ventana


ALTURA = 600
ANCHO = 800


"""
    raiz ventana
"""
raiz = Tk()
raiz.title("Scraping-PCs")
# raiz.iconbitmap("ruta.ico")
# raiz.geometry(f"{ancho}x{altura}")

# Permite o no que la ventana se pueda redimensionar
raiz.resizable(False, False)


#Sub-Pestañas

pestannas = Notebook(raiz)
pestannas.pack(fill="both", expand="yes")

pestanna_principal = Frame(height=f"{ALTURA}", width=f"{ANCHO}")
pestanna_principal.pack()
pestannas.add(pestanna_principal, text="Scraping-PCs")

pestanna_busqueda = Frame(height=f"{ALTURA}", width=f"{ANCHO}")
pestanna_busqueda.pack()
pestannas.add(pestanna_busqueda, text="Buscar componentes")

pestanna_favoritos = Frame(height=f"{ALTURA}", width=f"{ANCHO}")
pestanna_favoritos.pack()
pestannas.add(pestanna_favoritos, text="Favoritos")

pestanna_historial = Frame(height=f"{ALTURA}", width=f"{ANCHO}")
pestanna_historial.pack()
pestannas.add(pestanna_historial, text="Historial")


#Pestaña principal

estilo_de_fuente = Font(size=40)
etiqueta = Label(pestanna_principal, text="Scraping-PCs", font=estilo_de_fuente)
etiqueta.place(relx=0.5, rely=0.3, anchor=CENTER)


# Pestaña de busqueda


# Menu de opciones Componentes


def configurar_menu(variable, boton, opciones):

    """
    Funcion para configurar el menu.
    Argumentos: variable, boton, opciones
    """

    variable.set(opciones[0])
    boton.set_menu(None, *opciones)


def establecer_componente(componente):

    """
    Funcion para establecer el componente
    a ser seleccionado.
    Argumentos: componente
    """

    if componente == "CPU":
        configurar_menu(variable_marca, boton_menu_marca, OPCIONES_CPU_MARCA)
        configurar_menu(variable_primer_parametro, boton_menu_primer_parametro, OPCIONES_VACIAS)
        configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro, OPCIONES_VACIAS)

    elif componente == "GPU":
        configurar_menu(variable_marca, boton_menu_marca, OPCIONES_GPU_MARCA)
        configurar_menu(variable_primer_parametro, boton_menu_primer_parametro, OPCIONES_VACIAS)
        configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro, OPCIONES_VACIAS)

    elif componente == "PSU":
        configurar_menu(variable_marca, boton_menu_marca, OPCIONES_PSU_MARCA)
        configurar_menu(variable_primer_parametro, boton_menu_primer_parametro,
                        OPCIONES_PSU_POTENCIA)
        configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro,
                        OPCIONES_PSU_CERTIFICACION)

    elif componente == "RAM":
        variable_marca.set(OPCIONES_RAM_MARCA[0])
        configurar_menu(variable_marca, boton_menu_marca, OPCIONES_RAM_MARCA)
        configurar_menu(variable_primer_parametro, boton_menu_primer_parametro,
                        OPCIONES_RAM_CAPACIDAD)
        configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro,
                        OPCIONES_RAM_FRECUENCIA)

    elif componente == "Mother Board":
        variable_marca.set(OPCIONES_MOTHER_BOARD_MARCA[0])
        configurar_menu(variable_marca, boton_menu_marca, OPCIONES_MOTHER_BOARD_MARCA)
        configurar_menu(variable_primer_parametro, boton_menu_primer_parametro,
                        OPCIONES_MOTHER_BOARD_SOCKET)
        configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro, OPCIONES_VACIAS)

    elif componente == "Unidad de almacenamiento":
        configurar_menu(variable_marca, boton_menu_marca, OPCIONES_UNIDAD_ALMACENAMIENTO_MARCA)
        configurar_menu(variable_primer_parametro, boton_menu_primer_parametro,
                        OPCIONES_UNIDAD_ALMACENAMIENTO_CAPACIDAD)
        configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro,
                        OPCIONES_UNIDAD_ALMACENAMIENTO_TIPO)


variable_componentes = StringVar(pestanna_busqueda)
variable_componentes.set(OPCIONES_COMPONENTES[0])
boton_menu_componente = OptionMenu(pestanna_busqueda, variable_componentes,
                                   *OPCIONES_COMPONENTES, command=establecer_componente)
boton_menu_componente.config(width=25)
boton_menu_componente.grid(row=1, column=1)
# boton_menu_componente.pack()


# Menu de opciones de marcas


def establecer_marca(marca):

    """
    Esta funcion establece la marca
    a del componente seleccionado
    """

    if marca == "Intel":
        configurar_menu(variable_primer_parametro, boton_menu_primer_parametro,
                        OPCIONES_CPU_LINEA_INTEL)
        configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro,
                        OPCIONES_CPU_GENERACION_INTEL)
    elif marca == "AMD":
        if variable_componentes.get() == "CPU":
            configurar_menu(variable_primer_parametro, boton_menu_primer_parametro,
                        OPCIONES_CPU_LINEA_AMD)
            configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro,
                        OPCIONES_CPU_GENERACION_AMD)
        elif variable_componentes.get() == "GPU":
            configurar_menu(variable_primer_parametro, boton_menu_primer_parametro,
                        OPCIONES_GPU_LINEA_AMD)
            configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro,
                        OPCIONES_GPU_MODELO_AMD)
    elif marca == "Nvidia":
        configurar_menu(variable_primer_parametro, boton_menu_primer_parametro,
                    OPCIONES_GPU_LINEA_NVIDIA)
        configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro, OPCIONES_VACIAS)
    elif marca == "Todas las marcas" and variable_componentes.get() == "CPU":
        configurar_menu(variable_primer_parametro, boton_menu_primer_parametro, OPCIONES_VACIAS)
        configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro, OPCIONES_VACIAS)


variable_marca = StringVar(pestanna_busqueda)
variable_marca.set(OPCIONES_VACIAS[0])
boton_menu_marca = OptionMenu(pestanna_busqueda, variable_marca,
                              *OPCIONES_VACIAS, command=establecer_marca)
boton_menu_marca.config(width=25)
boton_menu_marca.grid(row=1, column=2)


# Menu de opciones primer parametro


def definir_serie(valor):

    """
    Escogido el componente y la marca,
    esta funcion se encarga de definir
    que serie en particular se esta buscando.
    Argumentos: valor
    """

    if variable_marca.get() == "Nvidia":
        seleccion = variable_primer_parametro.get()[6:]
        modelos_nvidia_gpu = [
            "Todos los modelos",
            f"{seleccion}50",
            f"{seleccion}50ti",
            f"{seleccion}60",
            f"{seleccion}60ti",
            f"{seleccion}70",
            f"{seleccion}70ti",
            f"{seleccion}80ti",
        ]
        if seleccion == "30":
            modelos_nvidia_gpu.append(f"{seleccion}90")
        configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro,
                        modelos_nvidia_gpu)


variable_primer_parametro = StringVar(pestanna_busqueda)
variable_primer_parametro.set(OPCIONES_VACIAS[0])
boton_menu_primer_parametro = OptionMenu(pestanna_busqueda, variable_primer_parametro,
                                         *OPCIONES_VACIAS,
                                         command=definir_serie)
boton_menu_primer_parametro.config(width=25)
boton_menu_primer_parametro.grid(row=1, column=3)


# Menu de opciones segundo parametro


variable_segundo_parametro = StringVar(pestanna_busqueda)
variable_segundo_parametro.set(OPCIONES_VACIAS[0])
boton_menu_segundo_parametro = OptionMenu(pestanna_busqueda, variable_segundo_parametro,
                                          *OPCIONES_VACIAS)
boton_menu_segundo_parametro.config(width=25)
boton_menu_segundo_parametro.grid(row=1, column=4)


# Menu de opciones estado


variable_estado = StringVar(pestanna_busqueda)
variable_estado.set(OPCIONES_ESTADO[0])
boton_menu_estado = OptionMenu(pestanna_busqueda, variable_estado, *OPCIONES_ESTADO)
boton_menu_estado.config(width=25)
boton_menu_estado.grid(row=2, column=1)


# Menu de opciones garantia minima


variable_garantia_minima = StringVar(pestanna_busqueda)
variable_garantia_minima.set(OPCIONES_GARANTIA_MINIMA[0])
boton_menu_garantia_minima = OptionMenu(pestanna_busqueda, variable_garantia_minima,
                                        *OPCIONES_GARANTIA_MINIMA)
boton_menu_garantia_minima.config(width=25)
boton_menu_garantia_minima.grid(row=2, column=2)


# Boton Buscar


def buscar_componentes():

    """
    Funcion para realizar la busqueda de
    componentes, aun en WIP
    """

    return None


boton_buscar = Button(pestanna_busqueda, text="Buscar Componente", command=buscar_componentes)
boton_buscar.place(relx=0.5, rely=0.3, anchor=CENTER)

# Pestaña de favoritos WIP

raiz.mainloop()
