#Librerias

from tkinter import StringVar, IntVar, Entry, Frame, Label, ttk
from tkinter import NO
from tkcalendar import DateEntry
from datetime import datetime
import Funciones

class aplicacion:

    def __init__(self, root) -> None:

        #Crear tres vistas para agregar, ver y actualizar.

        self.notebook = ttk.Notebook(root, width=1300, height=700)
        self.notebook.pack()

        self.frame_agregar = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_agregar, text="Agregar")

        self.frame_ver = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_ver, text="Ver")

        self.frame_actualizar = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_actualizar, text="Actualizar")

    #sheet agregar usuario.

    def sheet_agregar(self):

        #variables

        rut = StringVar()
        nombre = StringVar()
        apellido = StringVar()
        correo = StringVar()
        telefono = StringVar()
        sexo = IntVar()
        estado = IntVar()
        region = StringVar()
        comuna = StringVar()
        ciudad = StringVar()

        #Funciones de los widgets de la sheet agregar

        #Funcionalidad del button.

        def command_button():

            #Rescatar los datos ingresados en el formulario

            values = [rut.get(),
                        nombre.get(),
                        apellido.get(),
                        correo.get(),
                        telefono.get(),
                        entry_fecha_ingreso.get_date(),
                        sexo.get(),
                        estado.get(),
                        region.get(),
                        comuna.get(),
                        ciudad.get()]
            
            switch = Funciones.button_agregar(values)

            #Si fue agregado a la bd se eliminan los datos ingresados en el formulario.

            if switch:
                entry_rut.delete(0, len(rut.get()))
                entry_rut.focus()
                entry_nombre.delete(0, len(nombre.get()))
                entry_apellido.delete(0, len(apellido.get()))
                entry_correo.delete(0, len(correo.get()))
                entry_telefono.delete(0, len(telefono.get()))
                entry_fecha_ingreso.set_date(datetime.today())
                sexo.set(value=0)
                estado.set(value=0)
                combox_region.set("")
                combox_comuna.set("")
                combox_comuna['values'] = []
                entry_ciudad.delete(0, len(ciudad.get()))

        #Eliminar los valores y la seleccion del combobox comuna.

        def limpiar_combobox_comuna():
            combox_comuna.set("")
            combox_comuna['value'] = []

        #Agregar los valores al combobox comuna.

        def value_combobox_comuna():
            combox_comuna['value'] = list({i[1] for i in Funciones.lista_comunas(combox_region.get())})
        
        #Widgets de la sheet.

        #Rut
        
        label_rut = ttk.Label(self.frame_agregar,text="Rut: ", anchor='e', font=('Arial', 20))
        label_rut.place(relx=0.25, rely=0.01, relwidth=0.15, relheight=0.05)

        entry_rut = Entry(self.frame_agregar, textvariable=rut)
        entry_rut.place(relx=0.40, rely=0.01, relwidth=0.2, relheight=0.05)

        #Nombre

        label_nombre = ttk.Label(self.frame_agregar, text="Nombre: ", anchor='e', font=('Arial', 20))
        label_nombre.place(relx=0.25, rely=0.07, relwidth=0.15, relheight=0.05)

        entry_nombre = Entry(self.frame_agregar, textvariable=nombre)
        entry_nombre.place(relx=0.40, rely=0.07, relwidth=0.2, relheight=0.05)

        #Apellido
        
        label_apellido = ttk.Label(self.frame_agregar, text="Apellido: ", anchor='e', font=('Arial', 20))
        label_apellido.place(relx=0.25, rely=0.13, relwidth=0.15, relheight=0.05)

        entry_apellido = Entry(self.frame_agregar, textvariable=apellido)
        entry_apellido.place(relx=0.40, rely=0.13, relwidth=0.2, relheight=0.05)

        #Correo

        label_correo = ttk.Label(self.frame_agregar, text="Correo: ", anchor='e', font=('Arial', 20))
        label_correo.place(relx=0.25, rely=0.19, relwidth=0.15, relheight=0.05)

        entry_correo = Entry(self.frame_agregar, textvariable=correo)
        entry_correo.place(relx=0.40, rely=0.19, relwidth=0.2, relheight=0.05)

        #Telefono

        label_telefono = ttk.Label(self.frame_agregar, text="Telefono: ", anchor='e', font=('Arial', 20))
        label_telefono.place(relx=0.25, rely=0.25, relwidth=0.15, relheight=0.05)

        entry_telefono = Entry(self.frame_agregar, textvariable=telefono)
        entry_telefono.place(relx=0.40, rely=0.25, relwidth=0.2, relheight=0.05)

        #Fecha nacimiento

        label_fecha_ingreso = ttk.Label(self.frame_agregar, text="Fecha ingreso: ", anchor='e', font=('Arial', 20))
        label_fecha_ingreso.place(relx=0.25, rely=0.31, relwidth=0.15, relheight=0.05)

        entry_fecha_ingreso = DateEntry(self.frame_agregar, selectmode="day", date_pattern= ("dd/mm/y"))
        entry_fecha_ingreso.place(relx=0.40, rely=0.31, relwidth= 0.18, relheight=0.05)

        #Sexo
        
        label_sexo = ttk.Label(self.frame_agregar,text="Sexo: ", anchor='e', font=('Arial', 20))
        label_sexo.place(relx=0.25, rely=0.37, relwidth=0.15, relheight=0.05)

        radiobut_masculino = ttk.Radiobutton(self.frame_agregar, text="Hombre", variable=sexo, value=1)
        radiobut_masculino.place(relx=0.41, rely=0.37, relwidth= 0.1, relheight=0.05)
        radiobut_femenino = ttk.Radiobutton(self.frame_agregar, text="Mujer", variable=sexo, value=2)
        radiobut_femenino.place(relx=0.48, rely=0.37, relwidth= 0.1, relheight=0.05)

        #Estado

        label_estado = ttk.Label(self.frame_agregar,text="Estado: ", anchor='e', font=('Arial', 20))
        label_estado.place(relx=0.25, rely=0.43, relwidth=0.15, relheight=0.05)

        radiobut_activo = ttk.Radiobutton(self.frame_agregar, text="Activo", variable=estado, value=1)
        radiobut_activo.place(relx=0.41, rely=0.43, relwidth= 0.1, relheight=0.05)
        radiobut_desactivo = ttk.Radiobutton(self.frame_agregar, text="Desactivo", variable=estado, value=2)
        radiobut_desactivo.place(relx=0.48, rely=0.43, relwidth= 0.1, relheight=0.05)

        #Region

        label_region = ttk.Label(self.frame_agregar, text="Region: ", anchor='e', font=('Arial', 20))
        label_region.place(relx=0.25, rely=0.49, relwidth=0.15, relheight=0.05)

        combox_region = ttk.Combobox(self.frame_agregar,
                                            values= list(Funciones.lista_regiones().values()),
                                            textvariable= region,
                                            postcommand= limpiar_combobox_comuna,
                                            state= "readonly")
        combox_region.place(relx=0.40, rely=0.49, relwidth=0.28, relheight=0.05)

        #comuna

        label_comuna = ttk.Label(self.frame_agregar, text="Comuna: ", anchor='e', font=('Arial', 20))
        label_comuna.place(relx=0.25, rely=0.55, relwidth=0.15, relheight=0.05)

        combox_comuna = ttk.Combobox(self.frame_agregar,
                                            textvariable= comuna,
                                            postcommand= value_combobox_comuna,
                                            state= "readonly")
        combox_comuna.place(relx=0.40, rely=0.55, relwidth=0.28, relheight=0.05)

        #ciudad

        label_ciudad = ttk.Label(self.frame_agregar, text="Ciudad: ", anchor='e', font=('Arial', 20))
        label_ciudad.place(relx=0.25, rely=0.61, relwidth=0.15, relheight=0.05)

        entry_ciudad = Entry(self.frame_agregar, textvariable=ciudad)
        entry_ciudad.place(relx=0.40, rely=0.61, relwidth=0.2, relheight=0.05)

        #Button

        button_agregar = ttk.Button(self.frame_agregar, text="Agregar", command=command_button)
        button_agregar.place(relx=0.45, rely=0.70, relwidth=0.1, relheight=0.05)

    #Sheet ver usuarios.

    def sheet_ver(self):

        #Variables

        columnas = ["Rut","Nombre","Apellio","Correo","Telefono",
                    "Fecha de ingreso","Sexo","Estado","Region",
                    "Comuna","Ciudad"]
        
        orden = StringVar(value="Asendente")
        Columna_ordenar = StringVar()
        estado = StringVar()
        sexo = StringVar()
        region = StringVar()
        comuna = StringVar()

        #Funciones de los widgets de la sheet ver.

        #Al vizualizar la vista ver rrelenar el treeview con los datos.

        def datos_usuarios(event):
            if self.notebook.index(self.notebook.select()) == 1:
                datos_treeview(Funciones.lista_usuarios())

        #Rellenar el treeview con los datos de la lista recibida.
        
        def datos_treeview(lista_usuarios):
            if lista_usuarios != None:
                tabla.delete(*tabla.get_children())
                count = 1
                for i in lista_usuarios:
                    tabla.insert("","end",text=count, values=i[0:11])
                    count += 1
        
        #Filtrar la lista de usuarios.

        def filtro(event):
            datos_treeview(Funciones.filtrar_listado([sexo.get(),
                                      estado.get(),
                                      region.get(),
                                      comuna.get()]))
            
        #Ordenar la lista de usuarios.
            
        def ordenar(event):
            datos_treeview(Funciones.ordenar_listado(Columna_ordenar.get(), orden.get()))

        #Eliminar los valores y la seleccion del combobox comuna.

        def limpiar_combobox_comuna():
            combox_comuna.set("")
            combox_comuna['value'] = []

        #Rrellenar el combobox comuna con los datos correspondientes a la region.
            
        def value_combobox_comuna():
            combox_comuna['value'] = list({i[1] for i in Funciones.lista_comunas(region.get())})
        
        #Limpiar la seleccion de los combobox de ordenar y filtrar y rrellenar el treeview.

        def command_button_limpiar():

            datos_treeview(Funciones.limpiar_filtro())

            combox_columna_ordenar.set(value="")
            orden.set(value="Asendente")
            combox_sexo.set(value="")
            combox_estado.set(value="")
            combox_region.set(value="")
            combox_comuna.set(value="")

        #Frame para el treeview y los botones de filtro, sort y funciones                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                4
        
        frame_orden = Frame(self.frame_ver, highlightcolor="black", highlightthickness=3)
        frame_filtro = Frame(self.frame_ver, highlightcolor="black", highlightthickness=3)
        frame_comandos = ttk.Frame(self.frame_ver)
        frame_treewiew = ttk.Frame(self.frame_ver, width=1250,height=570)

        frame_orden.place(relx=0.016, rely=0, relwidth= 0.2, relheight=0.09)
        frame_filtro.place(relx=0.22, rely=0, relwidth= 0.68, relheight=0.09)
        frame_comandos.place(relx=0.91, rely=0, relwidth= 0.1, relheight=0.09)
        frame_treewiew.place(relx= 0, rely= 0.1, relwidth=1.07, relheight=0.95)

        #widgets

        #Ordenar, filtrar y descargar

        #Ordenar lista

        label_ordenar = Label(frame_orden,text="Ordenar", anchor='center', font=('Arial', 15))
        label_ordenar.place(relx= 0 , rely=0.01, relwidth=1, relheight=0.4)

        #Columna a ordenar

        combox_columna_ordenar = ttk.Combobox(frame_orden,
                                      values=("Nombre","Apellido","Sexo","Estado","Region","Comuna","Ciudad"),
                                      textvariable=Columna_ordenar,
                                      state="readonly")
        combox_columna_ordenar.place(relx=0.01, rely=0.45, relwidth=0.45, relheight=0.52)

        #Tipo de orden asendente o desendente.

        combox_columna_ordenar.bind("<<ComboboxSelected>>", ordenar)

        combox_ordenar = ttk.Combobox(frame_orden,
                                      values=["Asendente","Desendente"],
                                      textvariable=orden,
                                      state="readonly")
        combox_ordenar.place(relx=0.5, rely=0.45, relwidth=0.45, relheight=0.52)

        combox_ordenar.bind("<<ComboboxSelected>>", ordenar)

        #Filtrar lista

        label_filtro = Label(frame_filtro,text="Filtro",anchor="center",font=('Arial', 15))
        label_filtro.place(relx= 0 , rely=0.01, relwidth=1, relheight=0.4)

        #Sexo

        combox_sexo = ttk.Combobox(frame_filtro,
                                   values=("Hombre", "Mujer"),
                                   textvariable= sexo,
                                   state="readonly")
        combox_sexo.place(relx=0.01, rely=0.45, relwidth=0.13, relheight=0.52)

        combox_sexo.bind("<<ComboboxSelected>>", filtro)

        #Estado

        combox_estado = ttk.Combobox(frame_filtro,
                                   values=("Activo", "Desactivo"),
                                   textvariable= estado,
                                   state="readonly")
        combox_estado.place(relx=0.15, rely=0.45, relwidth=0.15, relheight=0.52)

        combox_estado.bind("<<ComboboxSelected>>", filtro)

        #Region

        combox_region = ttk.Combobox(frame_filtro,
                                   values=list(Funciones.lista_regiones().values()),
                                   textvariable= region,
                                   postcommand= limpiar_combobox_comuna,
                                   state="readonly")
        combox_region.place(relx=0.31, rely=0.45, relwidth=0.395, relheight=0.52)

        combox_region.bind("<<ComboboxSelected>>", filtro)

        #Comuna

        combox_comuna = ttk.Combobox(frame_filtro,
                                   textvariable= comuna,
                                   postcommand= value_combobox_comuna,
                                   state="readonly")
        combox_comuna.place(relx=0.715, rely=0.45, relwidth=0.2, relheight=0.52)

        combox_comuna.bind("<<ComboboxSelected>>", filtro)

        #Comando descargar y limpiar orden y filtro.

        button_limpiar = ttk.Button(frame_comandos, text="Limpiar", command=command_button_limpiar)
        button_limpiar.place(relx= 0.03 , rely=0.01, relwidth=0.85, relheight=0.5)

        button_descargar = ttk.Button(frame_comandos, text="Guardar", command=Funciones.guardar_lista)
        button_descargar.place(relx=0.03, rely=0.45, relwidth=0.85, relheight=0.5)

        #Treeview y scrollbar

        tabla = ttk.Treeview(frame_treewiew)
        scrollx = ttk.Scrollbar(frame_treewiew, orient= 'horizontal')
        scrolly = ttk.Scrollbar(frame_treewiew, orient='vertical')

        tabla.place(relx=0.01, rely=0.01, relwidth=0.9, relheight=0.9)
        scrollx.place(relx=0.01, rely=0.92, relwidth=0.9, relheight=0.03)
        scrolly.place(relx=0.91, rely=0.01, relwidth=0.03, relheight=0.9)

        #Configuracion treeview con scrollbar.

        scrollx.configure(command= tabla.xview)
        scrolly.configure(command= tabla.yview)
        tabla.configure(columns= columnas)
        tabla.configure(xscrollcommand= scrollx.set, yscrollcommand= scrolly.set)

        #Formatear columan treeview.

        tabla.column("#0", stretch=NO, minwidth=50, width=50, anchor='nw')
        tabla.column("#1", stretch=NO, minwidth=150, width=150, anchor='nw')
        tabla.column("#2", stretch=NO, minwidth=180, width=180, anchor='nw')
        tabla.column("#3", stretch=NO, minwidth=180, width=180, anchor='nw')
        tabla.column("#4", stretch=NO, minwidth=300, width=300, anchor='nw')
        tabla.column("#5", stretch=NO, minwidth=150, width=150, anchor='nw')
        tabla.column("#6", stretch=NO, minwidth=200, width=200, anchor='nw')
        tabla.column("#7", stretch=NO, minwidth=100, width=100, anchor='nw')
        tabla.column("#8", stretch=NO, minwidth=100, width=100, anchor='nw')
        tabla.column("#9", stretch=NO, minwidth=370, width=370, anchor='nw')
        tabla.column("#10", stretch=NO, minwidth=170, width=170, anchor='nw')
        tabla.column("#11", stretch=NO, minwidth=170, width=170, anchor='nw')

        #Nombre columna

        for i in range(12):
            if i != 0:
                tabla.heading("{}".format(columnas[i-1]), text=columnas[i-1])
            else:
                tabla.heading("#0", text="-")

        #Rrellenar el treeview con los datos de los usuarios.

        self.notebook.bind('<<NotebookTabChanged>>', datos_usuarios)

    #Sheet actualizar datos usuario.

    def sheet_actualizar(self):

        #variables

        rut = StringVar()
        correo = StringVar()
        telefono = StringVar()
        estado = IntVar()

        #Funciones de los widgets de la sheet actualizar.

        #Limpiar los campos y dejarlos vacios.

        def limpiar_campos():
            entry_correo.delete(0, len(correo.get()))
            entry_telefono.delete(0, len(telefono.get()))
            estado.set(value=0)

        #Buscar al usuario y rrellenar los campos con los datos del usuario.

        def command_button_buscar():

            if rut.get() != "":

                datos = Funciones.buscar_socio(rut.get())

                limpiar_campos()

                if datos != None:

                    if datos[3] != None:
                        entry_correo.insert(0, datos[3])

                    entry_telefono.insert(0, datos[4][3:])

                    if datos[5] == 1:
                        estado.set(value=1)
                    else:
                        estado.set(value=2)

        #Tomar los datos y ejecutar el proceso para actualizar al usuario

        def command_button_actualizar():
            
            datos_actualizados = [correo.get(),telefono.get(),estado.get()]

            if datos_actualizados != ["","",0]:

                switch = Funciones.actualizar_socio(datos_actualizados)

                if switch:
                    limpiar_campos()
                    entry_rut.delete(0, len(entry_rut.get()))
                    entry_rut.focus()

        #Buscar registro a actualizar

        #Rut
        label_rut = ttk.Label(self.frame_actualizar,text="Rut: ", anchor='e', font=('Arial', 20))
        label_rut.place(relx=0.25, rely=0.02, relwidth=0.15, relheight=0.05)

        entry_rut = Entry(self.frame_actualizar, textvariable=rut)
        entry_rut.place(relx=0.40, rely=0.02, relwidth=0.2, relheight=0.05)

        #Button

        button_buscar = ttk.Button(self.frame_actualizar, text="Buscar", command= command_button_buscar)
        button_buscar.place(relx=0.45, rely=0.1, relwidth=0.1, relheight=0.05)


        #Opciones a actualizar

        #Correo

        label_correo = ttk.Label(self.frame_actualizar, text="Correo: ", anchor='e', font=('Arial', 20))
        label_correo.place(relx=0.25, rely=0.2, relwidth=0.15, relheight=0.05)

        entry_correo = Entry(self.frame_actualizar, textvariable= correo)
        entry_correo.place(relx=0.40, rely=0.2, relwidth=0.2, relheight=0.05)

        #Telefono

        label_telefono = ttk.Label(self.frame_actualizar, text="Telefono: ", anchor='e', font=('Arial', 20))
        label_telefono.place(relx=0.25, rely=0.26, relwidth=0.15, relheight=0.05)

        entry_telefono = Entry(self.frame_actualizar, textvariable= telefono)
        entry_telefono.place(relx=0.40, rely=0.26, relwidth=0.2, relheight=0.05)

        #Estado

        label_estado = ttk.Label(self.frame_actualizar,text="Estado: ", anchor='e', font=('Arial', 20))
        label_estado.place(relx=0.25, rely=0.32, relwidth=0.15, relheight=0.05)

        radiobut_activo = ttk.Radiobutton(self.frame_actualizar, text="Activo", variable=estado, value=1)
        radiobut_activo.place(relx=0.41, rely=0.32, relwidth= 0.1, relheight=0.05)
        radiobut_desactivo = ttk.Radiobutton(self.frame_actualizar, text="Desactivo", variable=estado, value=2)
        radiobut_desactivo.place(relx=0.48, rely=0.32, relwidth= 0.1, relheight=0.05)

        #Button

        button_actualizar = ttk.Button(self.frame_actualizar, text="Actualizar", command=command_button_actualizar)
        button_actualizar.place(relx=0.45, rely=0.40, relwidth=0.1, relheight=0.05)