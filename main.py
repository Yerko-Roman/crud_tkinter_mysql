#Librerias

from tkinter import Tk
from sheets import aplicacion


#Crear la ventana.

root = Tk()
root.title("Registro de Usuarios") #Colocar nombre bien.
root.geometry("1300x700")

#GIU

app = aplicacion(root)
app.sheet_agregar()
app.sheet_ver()
app.sheet_actualizar()

#Ejecutar app.

root.mainloop()