"""
Modulo principal de la GUI
"""
from tkinter import *
from tkinter.ttk import *
from tkinter.font import *
from busquedas import *
from InterfazGrafica.opciones import *
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


# Funciones principales de la GUI


def rgb(red, green, blue):
    """
    Estable la gamma RGB
    de la aplicación
    """

    return f'#{red:02x}{green:02x}{blue:02x}'


def hacer_pestanna(nombre, altura, ancho, grupo_pestannas):
    pestanna = Frame(height=f"{altura}", width=f"{ancho}")
    pestanna.pack()
    grupo_pestannas.add(pestanna, text=nombre)
    return pestanna


def hacer_menu(pestanna, opciones, funcion, row, column, width):
    variable = StringVar(pestanna)
    variable.set(opciones[0])
    boton = OptionMenu(pestanna, variable, *opciones, command=funcion)
    boton.config(width=width)
    boton.grid(row=row, column=column)
    return variable, boton


def configurar_menu(variable, boton, opciones):
    """
    Funcion para configurar el menu.
    Argumentos: variable, boton, opciones
    """

    variable.set(opciones[0])
    boton.set_menu(None, *opciones)


def establecer_componente(componente):
    global opciones_marca, opciones_p, opciones_s
    """
    Funcion para establecer el componente
    a ser seleccionado.
    Argumentos: componente
    """

    if componente == "CPU":
        configurar_menu(variable_marca, boton_menu_marca, OPCIONES_CPU_MARCA)
        configurar_menu(variable_primer_parametro, boton_menu_primer_parametro, OPCIONES_VACIAS)
        configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro, OPCIONES_VACIAS)
        opciones_marca = OPCIONES_CPU_MARCA
        opciones_p = ["..."]
        opciones_s = ["..."]

    elif componente == "GPU":
        configurar_menu(variable_marca, boton_menu_marca, OPCIONES_GPU_MARCA)
        configurar_menu(variable_primer_parametro, boton_menu_primer_parametro, OPCIONES_VACIAS)
        configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro, OPCIONES_VACIAS)
        opciones_marca = OPCIONES_GPU_MARCA
        opciones_p = ["..."]
        opciones_s = ["..."]

    elif componente == "PSU":
        configurar_menu(variable_marca, boton_menu_marca, OPCIONES_PSU_MARCA)
        configurar_menu(variable_primer_parametro, boton_menu_primer_parametro,
                        OPCIONES_PSU_POTENCIA)
        configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro,
                        OPCIONES_PSU_CERTIFICACION)
        opciones_marca = OPCIONES_PSU_MARCA
        opciones_p = OPCIONES_PSU_POTENCIA
        opciones_s = OPCIONES_PSU_CERTIFICACION

    elif componente == "RAM":
        variable_marca.set(OPCIONES_RAM_MARCA[0])
        configurar_menu(variable_marca, boton_menu_marca, OPCIONES_RAM_MARCA)
        configurar_menu(variable_primer_parametro, boton_menu_primer_parametro,
                        OPCIONES_RAM_CAPACIDAD)
        configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro,
                        OPCIONES_RAM_FRECUENCIA)
        opciones_marca = OPCIONES_RAM_MARCA
        opciones_p = OPCIONES_RAM_CAPACIDAD
        opciones_s = OPCIONES_RAM_FRECUENCIA

    elif componente == "Mother Board":
        variable_marca.set(OPCIONES_MOTHER_BOARD_MARCA[0])
        configurar_menu(variable_marca, boton_menu_marca, OPCIONES_MOTHER_BOARD_MARCA)
        configurar_menu(variable_primer_parametro, boton_menu_primer_parametro,
                        OPCIONES_MOTHER_BOARD_SOCKET)
        configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro, OPCIONES_VACIAS)
        opciones_marca = OPCIONES_MOTHER_BOARD_MARCA
        opciones_p = OPCIONES_MOTHER_BOARD_SOCKET
        opciones_s = ["..."]

    elif componente == "Unidad de almacenamiento":
        configurar_menu(variable_marca, boton_menu_marca, OPCIONES_UNIDAD_ALMACENAMIENTO_MARCA)
        configurar_menu(variable_primer_parametro, boton_menu_primer_parametro,
                        OPCIONES_UNIDAD_ALMACENAMIENTO_CAPACIDAD)
        configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro,
                        OPCIONES_UNIDAD_ALMACENAMIENTO_TIPO)
        opciones_marca = OPCIONES_UNIDAD_ALMACENAMIENTO_MARCA
        opciones_p = OPCIONES_UNIDAD_ALMACENAMIENTO_CAPACIDAD
        opciones_s = OPCIONES_UNIDAD_ALMACENAMIENTO_TIPO


def establecer_marca(marca):
    global opciones_marca, opciones_p, opciones_s
    """
    Esta funcion establece la marca
    a del componente seleccionado
    """

    if marca == "Intel":
        configurar_menu(variable_primer_parametro, boton_menu_primer_parametro,
                        OPCIONES_CPU_LINEA_INTEL)
        configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro,
                        OPCIONES_CPU_GENERACION_INTEL)
        opciones_p = OPCIONES_CPU_LINEA_INTEL
        opciones_s = OPCIONES_CPU_GENERACION_INTEL
    elif marca == "AMD":
        if variable_componentes.get() == "CPU":
            configurar_menu(variable_primer_parametro, boton_menu_primer_parametro, OPCIONES_CPU_LINEA_AMD)
            configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro, OPCIONES_CPU_GENERACION_AMD)
            opciones_p = OPCIONES_CPU_LINEA_AMD
            opciones_s = OPCIONES_CPU_GENERACION_AMD
        elif variable_componentes.get() == "GPU":
            configurar_menu(variable_primer_parametro, boton_menu_primer_parametro, OPCIONES_GPU_LINEA_AMD)
            configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro, OPCIONES_GPU_MODELO_AMD)
            opciones_p = OPCIONES_GPU_LINEA_AMD
            opciones_s = OPCIONES_GPU_MODELO_AMD
    elif marca == "Nvidia":
        configurar_menu(variable_primer_parametro, boton_menu_primer_parametro, OPCIONES_GPU_LINEA_NVIDIA)
        configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro, OPCIONES_VACIAS)
        opciones_p = OPCIONES_GPU_LINEA_NVIDIA
        opciones_s = ["..."]
    elif marca == "Todas las marcas" and variable_componentes.get() == "CPU":
        configurar_menu(variable_primer_parametro, boton_menu_primer_parametro, OPCIONES_VACIAS)
        configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro, OPCIONES_VACIAS)
        opciones_p = ["..."]
        opciones_s = ["..."]


def definir_serie(valor):
    global opciones_s
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
        opciones_s = modelos_nvidia_gpu


def definir_serie_historial(marca, serie):
    global opciones_s
    """
    Escogido el componente y la marca,
    esta funcion se encarga de definir
    que serie en particular se esta buscando.
    Argumentos: valor
    """

    if marca == "Nvidia":
        seleccion = serie[6:]
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
        opciones_s = modelos_nvidia_gpu


def buscar_componentes():
    """
    Funcion para realizar la busqueda de
    componentes, aun en WIP
    """
    list_box.delete(0, END)
    num_componente = OPCIONES_COMPONENTES.index(variable_componentes.get())
    num_marca = opciones_marca.index(variable_marca.get())
    num_primer_parametro = opciones_p.index(variable_primer_parametro.get())
    num_segundo_parametro = opciones_s.index(variable_segundo_parametro.get())
    num_estado = OPCIONES_ESTADO.index(variable_estado.get())
    num_garantia = OPCIONES_GARANTIA_MINIMA.index(variable_garantia_minima.get())

    var = [variable_componentes.get(), variable_marca.get(), variable_primer_parametro.get(),
           variable_segundo_parametro.get(), variable_estado.get(), variable_garantia_minima.get()]
    var_arboles = [num_componente - 1, num_marca - 1, num_primer_parametro - 1, num_segundo_parametro - 1,
                   variable_estado.get(), variable_garantia_minima.get(), variable_orden_busqueda.get()]
    if variable_componentes.get() == OPCIONES_COMPONENTES[0]:
        return
    else:
        list_box_historial.delete(0, END)
        datos_historial = leer("Historial")
        datos_historial.append(var)
        escribir("Historial", datos_historial)
        imprimir_historial()
        # buscar(var)
        datos = buscar_en_arbol(var_arboles)
        for i in range(len(datos)):
            dato_limpio = "Tienda: "
            dato_limpio += datos[i][0].get('tienda')
            dato_limpio += " | Precio: "
            dato_limpio += str(datos[i][0].get('dia/precio')[1])
            dato_limpio += " | Calificación: "
            dato_limpio += str(datos[i][0].get('calificacion'))
            dato_limpio += " | "
            if var_arboles[1] == -1:
                dato_limpio += str(datos[i][1].get('marca'))
                dato_limpio += " | "
            if var_arboles[2] == -1:
                if var[0] == ("CPU" or "GPU"):
                    dato_limpio += str(datos[i][1].get('linea'))
                elif var[0] == "PSU":
                    dato_limpio += str(datos[i][1].get('potencia'))
                elif var[0] == ("RAM" or "Unidad de almacenamiento"):
                    dato_limpio += str(datos[i][1].get('capacidad'))
                elif var[0] == "Mother Board":
                    dato_limpio += str(datos[i][1].get('socket'))
                dato_limpio += " | "
            if var_arboles[3] == -1:
                if var[0] == "CPU":
                    dato_limpio += str(datos[i][1].get('generacion'))
                elif var[0] == "GPU":
                    dato_limpio += str(datos[i][1].get('modelo'))
                elif var[0] == "PSU":
                    dato_limpio += str(datos[i][1].get('certificacion'))
                elif var[0] == "RAM":
                    dato_limpio += str(datos[i][1].get('frecuencia'))
                elif var[0] == "Unidad de almacenamiento":
                    dato_limpio += str(datos[i][1].get('tipo'))
                dato_limpio += " | "
            if var_arboles[4] == "Todos los estados":
                dato_limpio += str(datos[i][0].get('estado'))
                dato_limpio += " | "
            if var_arboles[5] == "Todas las garantias minimas":
                dato_limpio += str(datos[i][0].get('garantia'))
                dato_limpio += " | "
            list_box.insert(i, dato_limpio)


def buscar_componentes_historial():
    list_box_historial_busqueda.delete(0, END)
    var = list_box_historial.get(list_box_historial.curselection())
    establecer_componente(var[0])
    establecer_marca_historial(var[1], var[0])
    print(var[2])
    definir_serie_historial(var[1], var[2])
    num_componente = OPCIONES_COMPONENTES.index(var[0])
    num_marca = opciones_marca.index(var[1])
    print(opciones_s)
    print(var)
    num_primer_parametro = opciones_p.index(var[2])
    num_segundo_parametro = opciones_s.index(var[3])

    var_arboles = [num_componente - 1, num_marca - 1, num_primer_parametro - 1, num_segundo_parametro - 1,
                   var[4], var[5], variable_orden_busqueda.get()]

    datos = buscar_en_arbol(var_arboles)
    for i in range(len(datos)):
        dato_limpio = "Tienda: "
        dato_limpio += datos[i][0].get('tienda')
        dato_limpio += " | Precio: "
        dato_limpio += str(datos[i][0].get('dia/precio')[1])
        dato_limpio += " | Calificación: "
        dato_limpio += str(datos[i][0].get('calificacion'))
        dato_limpio += " | "
        if var_arboles[1] == -1:
            dato_limpio += str(datos[i][1].get('marca'))
            dato_limpio += " | "
        if var_arboles[2] == -1:
            if var[0] == ("CPU" or "GPU"):
                dato_limpio += str(datos[i][1].get('linea'))
            elif var[0] == "PSU":
                dato_limpio += str(datos[i][1].get('potencia'))
            elif var[0] == ("RAM" or "Unidad de almacenamiento"):
                dato_limpio += str(datos[i][1].get('capacidad'))
            elif var[0] == "Mother Board":
                dato_limpio += str(datos[i][1].get('socket'))
            dato_limpio += " | "
        if var_arboles[3] == -1:
            if var[0] == "CPU":
                dato_limpio += str(datos[i][1].get('generacion'))
            elif var[0] == "GPU":
                dato_limpio += str(datos[i][1].get('modelo'))
            elif var[0] == "PSU":
                dato_limpio += str(datos[i][1].get('certificacion'))
            elif var[0] == "RAM":
                dato_limpio += str(datos[i][1].get('frecuencia'))
            elif var[0] == "Unidad de almacenamiento":
                dato_limpio += str(datos[i][1].get('tipo'))
            dato_limpio += " | "
        if var_arboles[4] == "Todos los estados":
            dato_limpio += str(datos[i][0].get('estado'))
            dato_limpio += " | "
        if var_arboles[5] == "Todas las garantias minimas":
            dato_limpio += str(datos[i][0].get('garantia'))
            dato_limpio += " | "
        list_box_historial_busqueda.insert(i, dato_limpio)


def borrar_historial():
    list_box_historial_busqueda.delete(0, END)
    list_box_historial.delete(0, END)
    datos_historial = []
    escribir("Historial", datos_historial)


def establecer_marca_historial(marca, componente):
    global opciones_marca, opciones_p, opciones_s
    """
    Esta funcion establece la marca
    a del componente seleccionado
    """

    if marca == "Intel":
        configurar_menu(variable_primer_parametro, boton_menu_primer_parametro,
                        OPCIONES_CPU_LINEA_INTEL)
        configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro,
                        OPCIONES_CPU_GENERACION_INTEL)
        opciones_p = OPCIONES_CPU_LINEA_INTEL
        opciones_s = OPCIONES_CPU_GENERACION_INTEL
    elif marca == "AMD":
        if componente == "CPU":
            configurar_menu(variable_primer_parametro, boton_menu_primer_parametro, OPCIONES_CPU_LINEA_AMD)
            configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro, OPCIONES_CPU_GENERACION_AMD)
            opciones_p = OPCIONES_CPU_LINEA_AMD
            opciones_s = OPCIONES_CPU_GENERACION_AMD
        elif componente == "GPU":
            configurar_menu(variable_primer_parametro, boton_menu_primer_parametro, OPCIONES_GPU_LINEA_AMD)
            configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro, OPCIONES_GPU_MODELO_AMD)
            opciones_p = OPCIONES_GPU_LINEA_AMD
            opciones_s = OPCIONES_GPU_MODELO_AMD
    elif marca == "Nvidia":
        configurar_menu(variable_primer_parametro, boton_menu_primer_parametro, OPCIONES_GPU_LINEA_NVIDIA)
        configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro, OPCIONES_VACIAS)
        opciones_p = OPCIONES_GPU_LINEA_NVIDIA
        opciones_s = ["..."]
    elif marca == "Todas las marcas" and componente == "CPU":
        configurar_menu(variable_primer_parametro, boton_menu_primer_parametro, OPCIONES_VACIAS)
        configurar_menu(variable_segundo_parametro, boton_menu_segundo_parametro, OPCIONES_VACIAS)
        opciones_p = ["..."]
        opciones_s = ["..."]


def imprimir_historial():
    datos_historial = leer("Historial")
    for i in range(len(datos_historial)):
        list_box_historial.insert(i, datos_historial[i])
# Dimensiones de la ventana


def annadir_favoritos():
    var = [variable_componentes.get(), variable_marca.get(), variable_primer_parametro.get(),
           variable_segundo_parametro.get(), variable_estado.get(), variable_garantia_minima.get()]
    variantes = ["Todos los tipos", "Todas las capacidades", "Todas las marcas", "Todas las certificaciones",
                 "Todas las potencias", "Todos los sockets", "Todas las frecuencias", "Todos los modelos",
                 "Todas las lineas", "Todas las generaciones", "Todas las garantias minimas", "Todos los estados",
                 "..."]
    for i in range(5, -1, -1):
        if var[i] in variantes:
            var.pop(i)
    print(var)
    print(list_box.get(list_box.curselection()))
    var.append(str(list_box.get(list_box.curselection())))
    datos_favoritos = leer("Favoritos")
    datos_favoritos.append(var)
    escribir("Favoritos", datos_favoritos)
    imprimir_favoritos()


def imprimir_favoritos():
    list_box_favoritos.delete(0, END)
    datos_favoritos = leer("Favoritos")
    for i in range(len(datos_favoritos)):
        list_box_favoritos.insert(i, datos_favoritos[i])


def borrar_favorito():
    var = list_box_favoritos.curselection()
    print(var)
    datos_favoritos = leer("Favoritos")
    datos_favoritos.pop(var[0])
    escribir("Favoritos", datos_favoritos)
    imprimir_favoritos()


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

# Sub-Pestañas

pestannas = Notebook(raiz)
pestannas.pack(fill="both", expand="yes")

pestanna_principal = hacer_pestanna("Scraping-PCs", ALTURA, ANCHO, pestannas)
pestanna_busqueda = hacer_pestanna("Buscar componentes", ALTURA, ANCHO, pestannas)
pestanna_favoritos = hacer_pestanna("Favoritos", ALTURA, ANCHO, pestannas)
pestanna_historial = hacer_pestanna("Historial", ALTURA, ANCHO, pestannas)


# Pestaña principal

estilo_de_fuente = Font(size=40)
etiqueta = Label(pestanna_principal, text="Scraping-PCs", font=estilo_de_fuente)
etiqueta.place(relx=0.5, rely=0.3, anchor=CENTER)

# Pestaña de busqueda


opciones_marca = ["..."]
opciones_p = ["..."]
opciones_s = ["..."]

# Menu de opciones Componentes
variable_componentes, boton_menu_componente = hacer_menu(pestanna_busqueda, OPCIONES_COMPONENTES, establecer_componente,
                                                         1, 1, 25)
# Menu de opciones de marcas
variable_marca, boton_menu_marca = hacer_menu(pestanna_busqueda, OPCIONES_VACIAS, establecer_marca, 1, 2, 25)
# Menu de opciones primer parametro
variable_primer_parametro, boton_menu_primer_parametro = hacer_menu(pestanna_busqueda, OPCIONES_VACIAS, definir_serie,
                                                                    1, 3, 25)
# Menu de opciones segundo parametro
variable_segundo_parametro, boton_menu_segundo_parametro = hacer_menu(pestanna_busqueda, OPCIONES_VACIAS, None, 1, 4,
                                                                      25)
# Menu de opciones estado
variable_estado, boton_menu_estado = hacer_menu(pestanna_busqueda, OPCIONES_ESTADO, None, 2, 1, 25)
# Menu de opciones garantia minima
variable_garantia_minima, boton_menu_garantia_minima = hacer_menu(pestanna_busqueda, OPCIONES_GARANTIA_MINIMA, None, 2,
                                                                  2, 25)
# Menu de opciones orden de busqueda
variable_orden_busqueda, boton_menu_orden_busqueda = hacer_menu(pestanna_busqueda, OPCIONES_ORDEN_BUSQUEDA, None, 2, 3,
                                                                25)

# Boton Buscar


boton_buscar = Button(pestanna_busqueda, text="Buscar Componente", command=buscar_componentes)
boton_buscar.place(relx=0.5, rely=0.2, anchor=CENTER)

boton_favoritos = Button(pestanna_busqueda, text="☆", command=annadir_favoritos)
boton_favoritos.place(relx=0.8, rely=0.2, anchor=CENTER)

frame = Frame(pestanna_busqueda)
scrollbary = Scrollbar(frame, orient=VERTICAL)
scrollbarx = Scrollbar(frame, orient=HORIZONTAL)
list_box = Listbox(frame, activestyle='none', cursor='hand2', selectmode=EXTENDED, height=20, width=110,
                   yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=list_box.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=list_box.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
frame.place(relx=0.5, rely=0.6, anchor=CENTER)
list_box.pack(pady=15)


# Pestaña de Historial

frame = Frame(pestanna_historial)
scrollbary = Scrollbar(frame, orient=VERTICAL)
list_box_historial = Listbox(frame, activestyle='none', cursor='hand2', selectmode=EXTENDED, height=12, width=110,
                             yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=list_box_historial.yview)
scrollbary.pack(side=RIGHT, fill=Y)
frame.place(relx=0.5, rely=0.2, anchor=CENTER)
list_box_historial.pack(pady=15)

frame = Frame(pestanna_historial)
scrollbary = Scrollbar(frame, orient=VERTICAL)
scrollbarx = Scrollbar(frame, orient=HORIZONTAL)
list_box_historial_busqueda = Listbox(frame, activestyle='none', cursor='hand2', selectmode=EXTENDED, height=15,
                                      width=110, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)

scrollbary.config(command=list_box_historial_busqueda.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=list_box_historial_busqueda.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
frame.place(relx=0.5, rely=0.7, anchor=CENTER)
list_box_historial_busqueda.pack(pady=15)

boton_buscar_historial = Button(pestanna_historial, text="Buscar Componente", command=buscar_componentes_historial)
boton_buscar_historial.place(relx=0.5, rely=0.425, anchor=CENTER)

boton_borrar_historial = Button(pestanna_historial, text="Borrar Historial", command=borrar_historial)
boton_borrar_historial.place(relx=0.8, rely=0.425, anchor=CENTER)


# Menu de opciones orden de busqueda


variable_orden_busqueda_historial = StringVar(pestanna_historial)
variable_orden_busqueda_historial.set(OPCIONES_ORDEN_BUSQUEDA[0])
boton_menu_orden_busqueda_historial = OptionMenu(pestanna_historial, variable_orden_busqueda,
                                       *OPCIONES_ORDEN_BUSQUEDA)
boton_menu_orden_busqueda_historial.config(width=25)
# boton_menu_orden_busqueda.grid(row=2, column=3)
boton_menu_orden_busqueda_historial.place(relx=0.2, rely=0.425, anchor=CENTER)

#
imprimir_historial()


# Pestaña Favoritos

boton_borrar_favorito = Button(pestanna_favoritos, text="-", command=borrar_favorito)
boton_borrar_favorito.place(relx=0.5, rely=0.925, anchor=CENTER)

frame = Frame(pestanna_favoritos)
scrollbary = Scrollbar(frame, orient=VERTICAL)
scrollbarx = Scrollbar(frame, orient=HORIZONTAL)
list_box_favoritos = Listbox(frame, activestyle='none', cursor='hand2', selectmode=EXTENDED, height=30, width=110,
                             yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=list_box_favoritos.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=list_box_favoritos.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
frame.place(relx=0.5, rely=0.45, anchor=CENTER)
list_box_favoritos.pack(pady=15)

imprimir_favoritos()

raiz.mainloop()

