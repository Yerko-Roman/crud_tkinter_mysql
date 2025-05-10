from mysql import connector

class Conexion_mysql:

    def __init__(self) -> None:
        self.conexion = connector.connect(user = "", 
                                          password = "",
                                          host = "",
                                          database = "",
                                          port = "")
    
    #Leer la tabla regiones.

    def read_region(self):
        self.cursor = self.conexion.cursor()
        self.cursor.execute("select * from regiones;")
        self.request = self.cursor.fetchall()
        self.conexion.close()

        return self.request
    
    #Leer la tabla comunas de una region en especifico.
    
    def read_bd_comunas_region(self, id_region):
        self.cursor = self.conexion.cursor()
        self.cursor.execute("select * from Comunas where id_region = {};".format(id_region))
        self.request = self.cursor.fetchall()
        self.conexion.close()

        return self.request
    
    #Insertar un nuevo usuario en la tabla usuarios.
    
    def insert_usuario(self, valores):
        try:

            self.value = "null,"
            for i in range(11):
                if valores[i] != 'null':
                    if i != 10:
                        self.value += "'{}',".format(valores[i])
                    else:
                        self.value += "'{}'".format(valores[i])
                else:
                    self.value += 'null,'

            self.sentencia = "insert into USUARIOS value ({})".format(self.value)
            self.cursor = self.conexion.cursor()
            self.cursor.execute(self.sentencia)
            self.conexion.commit()

            return True, None
        except Exception as error:
            return False, error
        finally:
            self.conexion.close()

    #Leer la tabla usuarios.

    def read_usuarios(self):
        consulta =('select u.rut, u.nombre, u.apellido, u.correo, u.telefono,\
                            u.fecha_ingreso, sexo.sexo, e.estado, r.nombre, c.nombre, u.direccion_ciudad\
                    from USUARIOS u\
                    inner join sexo on u.id_sexo = sexo.id_sexo\
                    inner join estado e on u.id_estado = e.id_estado\
                    inner join regiones r on u.id_region = r.id_region\
                    inner join comunas c on u.id_comuna = c.id_comuna;')
        self.cursor = self.conexion.cursor()
        self.cursor.execute(consulta)
        self.request = self.cursor.fetchall()
        self.conexion.close()
        
        return self.request
    
    #Verificar que rut exista en la tabla usuarios.
    
    def verificar_rut(self, rut):

        switch =False

        consulta = "select u.id_usuario, u.nombre, u.apellido, u.correo, u.telefono, e.id_estado \
                    from USUARIOS u inner join estado e on u.id_estado = e.id_estado\
                     where u.rut = '{}';".format(rut)
        
        self.cursor = self.conexion.cursor()
        self.cursor.execute(consulta)
        self.request = self.cursor.fetchall()
        self.conexion.close()


        if self.request != []:
            switch = True
        
        return switch, self.request
    
    #Actualizar los datos de un usuario.
    
    def actualizar_usuario(self, datos):
        
        consulta = "update USUARIOS set correo = '{}', telefono = '{}', id_estado = '{}' where id_usuario = '{}';".format(datos[3],datos[4],datos[5], datos[0])

        self.cursor = self.conexion.cursor()
        self.cursor.execute(consulta)
        self.conexion.commit()
        self.conexion.close()
