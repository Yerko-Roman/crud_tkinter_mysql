# crud_python_tkinter_mysql

Aplicacion de escritorio desarrollada con python, tkinter y mysql. Tiene como objetivo
llevar el registro de los socios de una organizacion. Esta aplicacion esta pensada para
ser utilizada en chile, ya que la verificacion del rut es para rut chileno y las regiones
y comunas salen las de chile.

Esta compuesta de tres ventanas:
    - Agregar: En esta ventana se ingresan los datos de un nuevo usuario y se agrega a la bd.
    - Ver: En este apartado se muestran todos los usuarios agregados a la bd, tine funcionalidades de
           orden, filtro, y guardar el listado que se esta mostrando.
    - Actualizar: Con el rut del usuario se puede actualizar los siguientes datos correo, telefono y su estado.


# Como utilizarla

Primero es que instalar mysql y python

Despues es que inizializar la base de datos,3 para esto es que crear la base de datos y
sus tablas, ademas rrellenar las tablas estado, sexo, region y comuna con sus datos predeterminados.

    - En el archivo 'BD.sql' se encuentra la creacion de la base de datos, la creacion de las tablas
      y los datos de la tabla estado y sexo. Se recomienda ir ejecutando el codigo por secciones, primero
      crear la bd, despues crear las tablas una a una y por ultimo agregar los datos de estado y despues los de sexo.
    - Para los datos de la tabla region y comuna se debe ejectura el archivo 'regiones_comunas.py', antes de ejecutar el archivo
      colocar los paramatetros de user, password, host, database y port.

Una vez que esta lista la bd es que configurar el archivo 'conexion.py', es que rrellenar los campos de user, password, host,
database y port, con los datos correspondientes.

Instalar las librerias faltantes:
    - mysql-connector-python
    - python-dateutil
    - panda
    - tkcalendar
    - openpyxl

Una vez que tenemos todo esto listo es que ejecutar el archivo main.py

# ¿Que se utilizo?

- python 3.10.11
- Tkinter
- mysql 8.0.36
- Librerias
    - mysql-connector-python
    - python-dateutil
    - panda
    - tkcalendar
    - openpyxl