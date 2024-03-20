from tkinter import *
from tkinter import messagebox
import sqlite3
import querys, MultiListBox

dbName="jurQ_DB"

root=Tk()
root.iconbitmap("T.ico")
root.title("Sociedad")

#==========BARRA MENÚ==========
barraMenu=Menu(root)
root.config(menu=barraMenu)

MenuVentana=Menu(barraMenu, tearoff=0)
MenuVentana.add_command(label="Volver")
MenuVentana.add_command(label="Salir")

MenuDatos=Menu(barraMenu, tearoff=0)
MenuDatos.add_command(label="Nuevo")
MenuDatos.add_command(label="Editar")
MenuDatos.add_command(label="Eliminar")

MenuAyuda=Menu(barraMenu, tearoff=0)
MenuAyuda.add_command(label="Licencia")
MenuAyuda.add_command(label="Acerca de...")

barraMenu.add_cascade(label="Ventana", menu=MenuVentana)
barraMenu.add_cascade(label="Datos", menu=MenuDatos)
barraMenu.add_cascade(label="Ayuda", menu=MenuAyuda)

#==========CAMPOS==========
miFrame1=Frame()
miFrame1.pack(fill="both", expand=True) #Fill usa nomenclatura deejes de coordenadas X, Y, both o none
miFrame1.config(bg="steelblue2", width=900)

miFrame2=Frame(root)
miFrame2.config(bg="steelblue1", width=900, padx=10, pady=0)
miFrame2.pack(fill="both", expand=True)

miFrame3=Frame(root)
miFrame3.config(bg="steelblue1", width=900, padx=10, pady=0)
miFrame3.pack(fill="both", expand=True)

miFrame4=Frame(root)
miFrame4.config(bg="steelblue1", width=900, padx=10, pady=0)
miFrame4.pack(fill="both", expand=True)

headLabel=Label(miFrame1,fg = "blue", bg = "steelblue2", text="DATOS SOCIEDAD.", font=("Speak Pro",16))
headLabel.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
headLabel.config(width=20)


miId=StringVar()
miSociedad=StringVar()
miTipo=StringVar()
miCif=StringVar()
miDireccion=StringVar()

idLabel=Label(miFrame2,fg = "blue", bg = "steelblue1", text="Id", font=("Speak Pro",11), disabledforeground="gray60")
idLabel.grid(row=0, column=0, sticky="e", padx=0, pady=5)
cuadroID=Entry(miFrame2,bg = "khaki1", textvariable=miId, font=("Speak Pro",11))
cuadroID.grid(row=0, column=1, padx=5, pady=0)
cuadroID.config(width=8)

NombreLabel=Label(miFrame3,fg = "blue", bg = "steelblue1", text="Nombre", font=("Speak Pro",11))
NombreLabel.grid(row=1, column=0, sticky="e", padx=0, pady=5)
cuadroNombre=Entry(miFrame3,bg = "khaki1", textvariable=miSociedad, font=("Speak Pro",11))
cuadroNombre.grid(row=1, column=1, padx=5, pady=5)
cuadroNombre.config(fg="black", justify="left", width=35)
cuadroNombre.bind("<FocusOut>")

TipoLabel=Label(miFrame3,fg = "blue", bg = "steelblue1", text="Tipo", font=("Speak Pro",11))
TipoLabel.grid(row=1, column=2, sticky="e", padx=0, pady=5)
cuadroTipo=Entry(miFrame3,bg = "khaki1", textvariable=miTipo, font=("Speak Pro",11))
cuadroTipo.grid(row=1, column=3, padx=5, pady=5)
cuadroTipo.config(fg="black", justify="left", width=6)

CifLabel=Label(miFrame3,fg = "blue", bg = "steelblue1", text="CIF", font=("Speak Pro",11))
CifLabel.grid(row=1, column=4, sticky="e", padx=0, pady=5)
cuadroCif=Entry(miFrame3,bg = "khaki1", textvariable=miCif, font=("Speak Pro bold",13))
cuadroCif.grid(row=1, column=5, padx=5, pady=5)
cuadroCif.config(fg="blue", justify="center", width=12)
cuadroCif.bind("<FocusOut>")

DirLabel=Label(miFrame4,fg = "blue", bg = "steelblue1", text="Dirección", font=("Speak Pro",11))
DirLabel.grid(row=0, column=0, sticky="e", padx=0, pady=5)
cuadroDir=Entry(miFrame4,bg = "khaki1", textvariable=miDireccion, font=("Speak Pro",11))
cuadroDir.grid(row=0, column=1, padx=5, pady=5)
cuadroDir.config(fg="black", justify="left", width=66)

#==========BOTONES==========
miFrame5=Frame()
miFrame5.pack(fill="both", expand=True) #Fill usa nomenclatura deejes de coordenadas X, Y, both o none
miFrame5.config(bg="steelblue3", width=900)

botonLimpiar=Button(miFrame2,text="Limpiar", font=("Speak Pro",9), bg="darkolivegreen1",fg = "blue",
                     cursor="hand2", width=5, height=1)
botonLimpiar.grid(row=0,column=3,sticky="e", padx=10, pady=10)


botonCancelar=Button(miFrame5,text="Salir", font=("Speak Pro",11),fg = "blue", 
                     cursor="hand2", width=10)
botonCancelar.grid(row=1,column=0,sticky="e", padx=10, pady=10)

botonNuevo=Button(miFrame5,text="Nuevo", font=("Speak Pro",11),fg = "blue", 
                     cursor="hand2",width=10)
botonNuevo.grid(row=1,column=1,sticky="e", padx=10, pady=10)

botonBuscar=Button(miFrame5,text="Buscar", font=("Speak Pro",11), fg = "blue",
                     cursor="hand2", width=10)
botonBuscar.grid(row=1,column=2,sticky="e", padx=10, pady=10)

botonGuardar=Button(miFrame5,text="Guardar", font=("Speak Pro",11), bg="darkolivegreen1",fg = "blue",
                     cursor="hand2", width=10)
botonGuardar.grid(row=1,column=3,sticky="e", padx=10, pady=10)

botonEliminar=Button(miFrame5,text="Eliminar", font=("Speak Pro",11),bg="orange",fg = "blue", 
                     cursor="hand2",width=10, disabledforeground="gray30")
botonEliminar.grid(row=1,column=4,sticky="e", padx=10, pady=10)
botonEliminar.config(state="disabled")

#==========EVENTOS==========


root.mainloop()
