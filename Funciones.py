from itertools import cycle
from re import sub
from datetime import datetime
from dateutil.relativedelta import relativedelta
import conexion
from pandas import DataFrame
from tkinter import messagebox
from tkinter import filedialog
from tkinter.simpledialog import askstring

#Variables

datos_usuario = []
datos_usuario_actualizados = []
lista_usuarios_ordenados_filtrados = []
lista_usuario = []
lista_region = []
lista_comuna = []


#Funciones secundarias.

#Verificar que los datos sean validos y en caso de ser validos formatear los datos para ser procesados.

#Rut.

def verificar_rut(rut):
    switch = False
    rut = rut.replace(" ", "")
    rut = sub("[.-]", "",rut)

    numero = rut[:-1]
    digito_verificador = rut[-1]

    if numero.isdigit() and (digito_verificador.isdigit() or digito_verificador == "k" or digito_verificador == "K"):
        if len(rut) == 9 or len(rut) == 8:
                reversed_digits = map(int, reversed(str(numero)))
                factors = cycle(range(2, 8))
                s = sum(d * f for d, f in zip(reversed_digits, factors))
                resultado = (-s) % 11
                if digito_verificador.isdigit():
                    if resultado == int(digito_verificador):
                        switch = True
                if digito_verificador.upper() == "K":
                    if resultado == 10:
                        switch = True

        if switch:
            rut = rut.replace(" ", "")
            rut = sub("[.-]", "",rut)
            rut = rut[:-7] + '.' + rut[-7:-4] + '.' + rut[-4:-1] + '-' + rut[-1]

    return switch, rut

#Nombre y apellido.

def verificar_nombre_apellido(cadena):
    switch = False

    if (cadena.replace(" ", "")).isalpha():
        switch = True

    if switch:
        cadena = cadena.strip()
        cadena = cadena.title()
        cadena = " ".join(cadena.split())

    return switch, cadena

#Correo.

def verificar_correo(correo):
    switch = False
    gmail = "@gmail.com"
    hotmail = "@hotmail.com"

    correo = correo.replace(" ", "")
    correo = correo.lower()

    if correo[-10:] == gmail:
        if len(correo) > 10:
            switch = True
    if correo[-12:] == hotmail:
        if len(correo) > 12:
            switch = True

    if switch:
        correo = correo.replace(" ", "")
        correo = correo.lower()
    else:
        correo = 'null'

    return switch, correo

#Telefono.

def verificar_telefono(telefono):
    switch = False
    telefono = telefono.replace(" ", "")

    if len(telefono) == 9:
        if telefono[0] == "9":
            if telefono.isdigit():
                switch = True

    if switch:
        telefono = telefono.replace(" ", "")
        telefono = "+56" + telefono

    return switch, telefono

#Fecha de ingreso.

def verificar_fecha_ingreso(fecha_ingreso):
    switch = False

    if fecha_ingreso != datetime.today().strftime("%Y-%m-%d"):
        if fecha_ingreso.year < datetime.today().year:
            if (relativedelta(datetime.now(), fecha_ingreso)).years >= 18:
                switch = True

    if not(switch):
        fecha_ingreso = 'null'

    return switch, fecha_ingreso

#Comuna y region.

def verificar_comuna_region(region, comuna):
    id_region = 0
    id_comuna = 0
    
    #Obtener los identificadores de region y comuna para ser agregados a la BD.

    for i in lista_region:
        if region == lista_region[i]:
            id_region = i
            for i in lista_comuna:
                if comuna == i[1]:
                    id_comuna = i[2]
    
    return id_region, id_comuna

#Ciudad.

def verificar_ciudad(ciudad):
    switch = False

    ciudad = ciudad.replace(" ", "")
    if ciudad.isalpha():
        switch = True
    
    if switch:
        ciudad = ciudad.strip()
        ciudad = ciudad.title()
        ciudad = " ".join(ciudad.split())

    return switch, ciudad

#Traer los valores de la BD y almazenarlos en variables globales.

#Lista usuarios

def lista_usuarios():
    global lista_usuario, lista_usuarios_ordenados_filtrados

    conexion_socios = conexion.Conexion_mysql()
    lista_usuario = conexion_socios.read_usuarios()
    lista_usuarios_ordenados_filtrados = lista_usuario

    return lista_usuario

#Lista regiones

def lista_regiones():

    global lista_region

    if lista_region == []:
        conexion_region = conexion.Conexion_mysql()
        lista_region = conexion_region.read_region()
        lista_region = dict(lista_region)
    
    return lista_region

#lista comunas

def lista_comunas(region):

    global lista_comuna

    lista_comuna.clear()

    if region != '':
        for i in range(1,17):
            if lista_region[i] == region:
                conexion_comuna = conexion.Conexion_mysql()
                lista_comuna = conexion_comuna.read_bd_comunas_region(i)
                return lista_comuna
    
    return lista_comuna

#Funciones principales.

#Funciones sheet agregar

#Funcion para verificar que los datos ingresados sean correctos y formatearlos.

def verificcar_datos(valores):

    datos_formateados = []

    #Que todas los campos tengan algun valor

    for i in range(11):
        if i in (0,1,2,4,6,7,8,9,10): #El correo y fecha de nacimiento no es obligatorio.
            if valores[i] == 0 or valores[i] =='':
                return False, None , "Faltan datos por ingresar."
        

    #validar los datos de los campos.

    #rut

    switch_rut , rut = verificar_rut(valores[0])

    if not(switch_rut):
        return False, None,  'El rut es invalido.'
    else:
        datos_formateados.append(rut)

    #Nombre

    switch_nombre, nombre = verificar_nombre_apellido(valores[1])

    if not(switch_nombre):
        return False, None, 'El nombre es invalido.'
    else:
        datos_formateados.append(nombre)

    #apellido

    switch_apellido, apellido = verificar_nombre_apellido(valores[2])

    if not(switch_apellido):
        return False, None, 'El apellido es invalido.'
    else:
        datos_formateados.append(apellido)

    #Correo

    if valores[3] != '':
        switch_correo, correo = verificar_correo(valores[3])
        if not(switch_correo):
            return False, None, 'El correo es invalido'
        else:
            datos_formateados.append(correo)
    else:
        datos_formateados.append('null')

    #Telefono

    switch_telefono, telefono = verificar_telefono(valores[4])
    
    if not(switch_telefono):
        return False, None, 'El telefono ingresado es invalido'
    else:
        datos_formateados.append(telefono)
    
    #Fecha ingreso

    if str(valores[5]) != datetime.today().strftime("%Y-%m-%d"):
        switch_fecha_ingreso, fecha_ingreso = verificar_fecha_ingreso(valores[5])
        if not(switch_fecha_ingreso):
            return False, None, 'La fecha de ingreso es invalida'
        else:
            datos_formateados.append(fecha_ingreso)
    else:
        datos_formateados.append('null')

    #sexo

    datos_formateados.append(valores[6])

    #Estado

    datos_formateados.append(valores[7])

    #Region comuna

    region, comuna = verificar_comuna_region(valores[8], valores[9])

    datos_formateados.append(region)
    datos_formateados.append(comuna)

    #Direccion ciudad

    switch_ciudad, direccion_ciudad = verificar_ciudad(valores[10])  

    if not(switch_ciudad):
        return False, None, 'La ciudad de la direccion es invalida.'
    else:
        datos_formateados.append(direccion_ciudad)
    
    return True, datos_formateados, 'Los datos ingresados son correctos'

#Agregar usuario a la BD.

def agregar_usuario(valores):

    conexion_bd = conexion.Conexion_mysql()
    switch, error = conexion_bd.insert_usuario(valores)

    return switch, error
            
#Funcion del button agregar.
            
def button_agregar(valores_ingresados):
            
            #Validar que los datos sean correctos.
            
            switch, valores_formateados, mensaje_error_datos = verificcar_datos(valores_ingresados)

            if switch:
                copia_valores_formateados = valores_formateados.copy()

                mensaje_validar = ""
                campos = ["Rut","Nombre","Apellido","Correo","Telefono","Fecha ingreso","Sexo","Estado",
                          "Region","Comuna","Ciudad"]

                if copia_valores_formateados[5] != 'null':
                    copia_valores_formateados[5] = copia_valores_formateados[5].strftime("%d-%m-%Y")

                if valores_ingresados[6] == 1:
                    copia_valores_formateados[6] = "Hombre"
                if valores_ingresados[6] == 2:
                    copia_valores_formateados[6] = "Mujer"

                if valores_ingresados[7] == 1:
                    copia_valores_formateados[7] = "Activo"
                if valores_ingresados[7] == 2:
                    copia_valores_formateados[7] = "Desactivo"

                copia_valores_formateados[8] = valores_ingresados[8]
                copia_valores_formateados[9] = valores_ingresados[9]

                #Se muestra un mensaje para confirmar.

                for i in range(11):
                    mensaje_validar = mensaje_validar + campos[i] + ": " + copia_valores_formateados[i] + "\n"

                respuesta = messagebox.askyesno("Validar datos", mensaje_validar)

                #Se procede agregar el usuario.

                if respuesta:
                    switch, mensaje_error = agregar_usuario(valores_formateados)

                    #Si hubo un error se muestra un mensaje, si fue correcto se muestra otro mensaje.

                    if switch:
                        messagebox.showinfo("Socio registrado", 
                                            "El socio {0} {1} fue agregado con exito a la BD.".format(valores_formateados[1], valores_formateados[2]))
                        return True
                    else:
                       messagebox.showerror('Error en la bd', "Error al registrar el socio en la BD. '{0}'".format(mensaje_error))
                       return False
            else:
                messagebox.showerror('Error dato mal ingresado', mensaje_error_datos)
                return False

#Funciones sheet ver

#Ordenar la lista de usuarios.

def ordenar_listado(columna, orden):

    global lista_usuarios_ordenados_filtrados

    if columna != "" and orden != "":

        if columna == "Nombre":
            columna = 1
        elif columna == "Apellido":
            columna = 2
        elif columna == "Sexo":
            columna = 6
        elif columna == "Estado":
            columna = 7
        elif columna == "Region":
            columna = 8
        elif columna == "Comuna":
            columna = 9
        elif columna == "Ciudad":
            columna = 10


        if orden == "Asendente":
            return sorted(lista_usuarios_ordenados_filtrados, key= lambda x : x[columna])
        if orden == "Desendente":
            return sorted(lista_usuarios_ordenados_filtrados, key=lambda x : x[columna], reverse= True)
        
    return

#Filtrar la lista de usuarios.

def filtrar_listado(filtro):

    global lista_usuarios_ordenados_filtrados, lista_usuario

    lista_usuarios_ordenados_filtrados = lista_usuario

    if filtro[0] != "":
        lista_usuarios_ordenados_filtrados = list(filter(lambda x : x[6] == filtro[0], lista_usuarios_ordenados_filtrados))
    if filtro[1] != "":
        lista_usuarios_ordenados_filtrados = list(filter(lambda x : x[7] == filtro[1], lista_usuarios_ordenados_filtrados))
    if filtro[2] != "":
        lista_usuarios_ordenados_filtrados = list(filter(lambda x : x[8] == filtro[2], lista_usuarios_ordenados_filtrados))
    if filtro[3] != "":
        lista_usuarios_ordenados_filtrados = list(filter(lambda x : x[9] == filtro[3], lista_usuarios_ordenados_filtrados))

    return lista_usuarios_ordenados_filtrados

#Entregar la lista donde se encuentran todos los usuarios.

def limpiar_filtro():
    return lista_usuario

#Descargar la lista que se visualiza en el treeview en formato excel.

def guardar_lista():

    columnas = ["Rut","Nombre","Apellio","Correo","Telefono",
                "Fecha de ingreso","Sexo","Estado","Region",
                "Comuna","Ciudad"]
    
    ruta = filedialog.askdirectory()
    nombre_archivo = askstring(title="Nombre del archivo", prompt="Ingrese el nombre del archivo:")

    if ruta != "/" and nombre_archivo != None:
        df_datos_usuario = DataFrame(lista_usuarios_ordenados_filtrados, columns=columnas)
        df_datos_usuario.to_excel((ruta + "/" + nombre_archivo + ".xlsx"))

        messagebox.showinfo("Archivo guardado","El archivo {} fue guardo con exito en la ruta {}".format(nombre_archivo, ruta))
    else:
        messagebox.showerror('Error', 'Faltaron datos por ingresar')

#Funciones sheet actualizar

#Buscar el usuario y traer sus datos de la BD para ser actualizados.

def buscar_socio(rut):

    global datos_usuario

    #Priemero verificar el rut y formatearlo.
    
    switch, Rut_formateado= verificar_rut(rut)
    
    if switch:

        #Si el rut es valido procedemos a buscar en la BD.

        conexion_bd = conexion.Conexion_mysql()
        switch, datos_usuario = conexion_bd.verificar_rut(Rut_formateado)

        datos_usuario = list(datos_usuario[0])

        if switch:

            #Si el usuario existe, confirmamos que es el usuario que queremos actualizar.

            mensaje = "Desea actualizar los datos de {} {}".format(datos_usuario[1],datos_usuario[2])
            respuesta = messagebox.askyesno("Confirmacion usuario", mensaje)

            if respuesta:

                return datos_usuario

        else:
            messagebox.showerror('Error', 'El rut ingresado no existe.')
    else:
        messagebox.showerror('Error dato mal ingresado', 'El rut es invalido.')

#Realizar la actualizacion de los datos del usuario.

def actualizar_socio(datos_actualizados):

    global datos_usuario

    switch = True
    message = ""

    #Verificar y formatear los valores de los campos.

    if datos_actualizados[0] != "":
        switch_correo, correo= verificar_correo(datos_actualizados[0])
        if not(switch_correo):
            switch = False
            message = "El correo es invalido"
        else:
            datos_actualizados[0] = correo
    else:
        datos_actualizados[0] = 'null'

    if switch:
        switch_telefono, telefono = verificar_telefono(datos_actualizados[1])
        if not(switch_telefono):
            switch = False
            message = "El telefono ingresado es invalido"
        else:
            datos_actualizados[1] = telefono

    if switch:

        #Confirmar la actualizacion de los datos.

        estado = ""

        if datos_actualizados[2] == 1:
            estado = "Activo"
        else:
            estado = "Desactivo"

        mensaje = """ El usuario {} {} queda con los siguietes datos \n
                      Correo: {} \n
                      Telefono: {} \n
                      Estado: {} \n """.format(datos_usuario[1],datos_usuario[2],datos_actualizados[0],datos_actualizados[1],estado)

        respuesta = messagebox.askyesno("Confirmacion usuario", mensaje)

        if respuesta:

            #En caso de que la confirmacion sea afirmativa se actualizan los datos en la BD.

            datos_usuario[3] = datos_actualizados[0]
            datos_usuario[4] = datos_actualizados[1]
            datos_usuario[5] = datos_actualizados[2]

            conexion_bd = conexion.Conexion_mysql()
            conexion_bd.actualizar_usuario(datos_usuario)

            messagebox.showinfo("Actualizacion exitosa","El usuario {} {} fue actualizado.".format(datos_usuario[1], datos_usuario[2]))

            datos_usuario = []
        else:
            switch = False

    else:
        messagebox.showerror('Error', message)

    return switch
