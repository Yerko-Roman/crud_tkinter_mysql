import json
import mysql.connector

id_region  = 1
id_comuna = 1

conexion = mysql.connector.connect(user = "", 
                                   password = "",
                                   host = "",
                                   database = "usuario",
                                   port = "")

datos = open("regiones-provincias-comunas.json")

dic_reg_com = json.load(datos)

for region in dic_reg_com:
    region_nom = region["region"] + " " + region["region_number"]
    sentencia_region = 'INSERT INTO regiones VALUES("{0}","{1}")'.format(id_region, region_nom)
    cursor = conexion.cursor()
    cursor.execute(sentencia_region)
    conexion.commit()
    for i in region["provincias"]:
        for comuna in i["comunas"]:
            comuna_nom = comuna["name"]
            sentencia_comuna = 'INSERT INTO comunas VALUES("{0}","{1}","{2}")'.format(id_comuna, comuna_nom, id_region)
            cursor.execute(sentencia_comuna)
            conexion.commit()
            id_comuna += 1
    id_region += 1       
    print("registro realizado")




conexion.close()