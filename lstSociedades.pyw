from tkinter import *
from tkinter import messagebox
import sqlite3
import MultiListBox, querys

dbName="jurQ_DB"

def cargaLista(miQuery="SELECT * FROM SOCIEDADES"):
    miConexion=sqlite3.connect(dbName)
    miCursor=miConexion.cursor()

    #mySql="SELECT * FROM SOCIEDADES"
    miCursor.execute(miQuery)
    #print(miQuery)
    laSociedad=miCursor.fetchall()
    
    #print(laSociedad)
    mlb.delete(0,END)
    for soc in laSociedad:
        mlb.insert(END, (soc[0], soc[3], soc[1], soc[2]))
    miConexion.close()

def eliminaRegistro():
    
    querys.eliminaReg(dbName, "DELETE FROM SOCIEDADES WHERE ID=" + miId.get())
    
    #limpiarCampos()
    mlb.delete(0,END)
    cargaLista()

def buscar(*args):
    datos=[miId.get(),miSociedad.get(),miTipo.get(),miCif.get(),miDireccion.get()]
    mySql="SELECT * FROM SOCIEDADES WHERE "
    mySql=mySql + 'ID LIKE "%' + datos[0] + '%"'
    mySql=mySql + ' AND NOMBRE LIKE "%' + datos[1] + '%"'
    mySql=mySql + ' AND TIPO LIKE "%' + datos[2] + '%"'
    mySql=mySql + ' AND CIF LIKE "%' + datos[3] + '%"'
    #mySql=mySql + ' AND DIRECCION LIKE "%' + datos[4] + '%"'
    
    #print(mySql)

    cargaLista(mySql)    
   
    botonEliminar.config(state="normal")

def sel():
    datos=[miId.get(),miSociedad.get(),miTipo.get(),miCif.get(),miDireccion.get()]
    mySql="SELECT * FROM SOCIEDADES WHERE ID=" + labelId.get()
    
    laSociedad=querys.buscarReg(dbName,mySql, datos)

    for soc in laSociedad:
        labelId.set(soc[0])
        labelSociedad.set(soc[1])
        labelTipo.set(soc[2])
        labelCIF.set(soc[3])
    
    botonEliminar.config(state="normal")

def selectMlb(event):
    cs=mlb.curselection()
    cadena=mlb.get(cs)
    buscoID=cadena[0]
    #print(buscoID)
    labelId.set(buscoID)
    sel()

root=Tk()
root.iconbitmap("T.ico")
root.title("Sociedades")

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
miFrame4.config(bg="orange", width=900, padx=0, pady=0)
miFrame4.pack(fill="both", expand=True)

headLabel=Label(miFrame1,fg = "blue", bg = "steelblue2", text="DATOS SOCIEDAD.", font=("Speak Pro",16))
headLabel.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
headLabel.config(width=20)

miId=StringVar()
miSociedad=StringVar()
miTipo=StringVar()
miCif=StringVar()
miDireccion=StringVar()
labelId=StringVar()
labelSociedad=StringVar()
labelTipo=StringVar()
labelCIF=StringVar()

cuadroID=Entry(miFrame2,bg = "khaki1", textvariable=miId)
cuadroID.grid(row=1, column=0, padx=0, pady=0)
cuadroID.config(width=5)

cuadroCIF=Entry(miFrame2,bg = "khaki1", textvariable=miCif)
cuadroCIF.grid(row=1, column=1, padx=0, pady=0)
cuadroCIF.config(width=14)

cuadroSociedad=Entry(miFrame2,bg = "khaki1", textvariable=miSociedad)
cuadroSociedad.grid(row=1, column=2, padx=0, pady=0)
cuadroSociedad.config(width=90)

cuadroTipo=Entry(miFrame2,bg = "khaki1", textvariable=miTipo)
cuadroTipo.grid(row=1, column=3, padx=0, pady=0)
cuadroTipo.config(width=6)

mlb = MultiListBox.MultiListbox(miFrame3, (('Id', 5), ('CIF', 15), ('Nombre', 90), ('Tipo', 6)))
mlb.config(width=206,)
mlb.pack(expand=YES,fill=Y)

idLabel=Label(miFrame4,fg = "blue", bg = "orange", textvariable=labelId, disabledforeground="gray60")
idLabel.grid(row=1, column=0, padx=0, pady=0)
idLabel.config(width=5)

CIFLabel=Label(miFrame4,fg = "blue", bg = "orange", textvariable=labelCIF, disabledforeground="gray60", anchor="w")
CIFLabel.grid(row=1, column=1, padx=0, pady=0)
CIFLabel.config(width=12)

SociedadLabel=Label(miFrame4,fg = "blue", bg = "orange", textvariable=labelSociedad, disabledforeground="gray60", anchor="w")
SociedadLabel.grid(row=1, column=2, padx=0, pady=0)
SociedadLabel.config(width=77)

TipoLabel=Label(miFrame4,fg = "blue", bg = "orange", textvariable=labelTipo, disabledforeground="gray60", anchor="w")
TipoLabel.grid(row=1, column=3, padx=0, pady=0)
TipoLabel.config(width=5)


mlb.bind('<<DoubleClick>>', selectMlb)
miId.trace_add("write",buscar)
miCif.trace_add("write",buscar)
miSociedad.trace_add("write",buscar)
miTipo.trace_add("write",buscar)

cargaLista()

#==========BOTONES==========
miFrame5=Frame()
miFrame5.pack(fill="both", expand=True) #Fill usa nomenclatura deejes de coordenadas X, Y, both o none
miFrame5.config(bg="steelblue3", width=900)

botonCancelar=Button(miFrame5,text="Salir", font=("Speak Pro",11),fg = "blue", 
                     cursor="hand2", width=10)
botonCancelar.grid(row=1,column=0,sticky="e", padx=10, pady=10)

botonNuevo=Button(miFrame5,text="Nuevo", font=("Speak Pro",11),fg = "blue", 
                     cursor="hand2",width=10)
botonNuevo.grid(row=1,column=1,sticky="e", padx=10, pady=10)

""" botonBuscar=Button(miFrame5,text="Buscar", font=("Speak Pro",11), fg = "blue",
                     cursor="hand2", width=10, command=buscar)
botonBuscar.grid(row=1,column=2,sticky="e", padx=10, pady=10) """

""" botonGuardar=Button(miFrame5,text="Guardar", font=("Speak Pro",11), bg="darkolivegreen1",fg = "blue",
                     cursor="hand2", width=10)
botonGuardar.grid(row=1,column=3,sticky="e", padx=10, pady=10) """

botonEliminar=Button(miFrame5,text="Eliminar", font=("Speak Pro",11),bg="orange",fg = "blue", 
                     cursor="hand2",width=10, command=eliminaRegistro, disabledforeground="gray30")
botonEliminar.grid(row=1,column=4,sticky="e", padx=10, pady=10)
botonEliminar.config(state="disabled")


root.mainloop()