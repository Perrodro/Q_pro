from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import re
import querys

dbName="jurQ_DB"

#app.setStyleSheet(open("style.css", "r").read())

root=Tk()
#root.iconbitmap("T.ico")
root.title("Notarías")

#==========FUNCIONES==========

def limpiarCampos():
    
    miId.set("")
    miSociedad.set("")
    miTipo.set("")
    miCif.set("")
    miDireccion.set("")
    cargaLista()
    cuadroID.config(state="normal")
    botonNuevo.config(state="normal")

def nuevo():
    limpiarCampos()
    #cuadroID.config(state="disabled", disabledbackground="gray60")
    cuadroID.config(state="disabled")
    botonGuardar.config(state="disabled", text="Guardar")
    botonNuevo.config(state="disabled")

def habilitaBoton(e):

    soc=miSociedad.get()
    Cf=miCif.get()

    if len(soc) != 0 and len(Cf) != 0:
        botonGuardar.config(state="normal")

def guardar():
    datos=miSociedad.get().upper(),miTipo.get().upper(),miCif.get().upper(),miDireccion.get()
    
    if botonNuevo['state'] == "disabled":
        querys.devReg(dbName, "INSERT INTO SOCIEDADES VALUES (NULL,?,?,?,?)",True, datos)
        #messagebox.showinfo("Tabla SOCIEDADES. Nuevo registro", "Registro insertado con éxito")
    else:
        querys.devReg(dbName,"UPDATE SOCIEDADES SET NOMBRE=?, TIPO=?, CIF=?, DIRECCION=? WHERE ID=" + miId.get(), True,datos)
        #messagebox.showinfo("Tabla SOCIEDADES. Actualización de registros", "Registro Actualizado con éxito")

    limpiarCampos()
    cuadroID.config(state="normal")
    botonGuardar.config(state="normal")
    botonNuevo.config(state="normal")
    listbox.delete(0,END)
    cargaLista()

def buscar():
    datos=[miId.get(),miSociedad.get(),miTipo.get(),miCif.get(),miDireccion.get()]
    mySql="SELECT * FROM SOCIEDADES WHERE "
    mySql=mySql + 'ID LIKE "%' + datos[0] + '%"'
    mySql=mySql + ' AND NOMBRE LIKE "%' + datos[1] + '%"'
    mySql=mySql + ' AND TIPO LIKE "%' + datos[2] + '%"'
    mySql=mySql + ' AND CIF LIKE "%' + datos[3] + '%"'
    mySql=mySql + ' AND DIRECCION LIKE "%' + datos[4] + '%"'
    
    #print(mySql)
    
    laSociedad=querys.devReg(dbName,mySql, True)

    #print (laSociedad)

    listbox.delete(0,END)
    for soc in laSociedad:
        listbox.insert(END, (soc[0], "|", soc[3],"|", soc[1], ",", soc[2]))
   
    botonEliminar.config(state="normal")
    
def sel():
    datos=[miId.get(),miSociedad.get(),miTipo.get(),miCif.get(),miDireccion.get()]
    mySql="SELECT * FROM SOCIEDADES WHERE ID=" + miId.get()
    
    laSociedad=querys.buscarReg(dbName,mySql, datos)

    for soc in laSociedad:
        miId.set(soc[0])
        miSociedad.set(soc[1])
        miTipo.set(soc[2])
        miCif.set(soc[3])
        miDireccion.set(soc[4])
    
    botonEliminar.config(state="normal")

def cargaLista():
    miConexion=sqlite3.connect("jurQ_DB")
    miCursor=miConexion.cursor()

    mySql="SELECT * FROM SOCIEDADES"
    miCursor.execute(mySql)
    
    laSociedad=miCursor.fetchall()
    
    for soc in laSociedad:
        listbox.insert(END, (soc[0], "|", soc[3],"|", soc[1], ",", soc[2]))
    miConexion.close()

def eliminaRegistro():
    
    querys.eliminaReg(dbName, "DELETE FROM SOCIEDADES WHERE ID=" + miId.get())
    
    limpiarCampos()
    listbox.delete(0,END)
    cargaLista()
    
def salirAplicacion():
    valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicaión?")

    if valor=="yes":
        #sqlite3.connect("jurQ_DB").close()
        root.destroy()


querys.ConexionBBDD(dbName, "CREATE TABLE SOCIEDADES (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(50), TIPO VARCHAR(6), CIF VARCHAR(12), DIRECCION VARCHAR(50))")


#==========BARRA MENÚ==========
barraMenu=Menu(root)
root.config(menu=barraMenu)

MenuVentana=Menu(barraMenu, tearoff=0)
MenuVentana.add_command(label="Volver")
MenuVentana.add_command(label="Salir", command=salirAplicacion)

MenuDatos=Menu(barraMenu, tearoff=0)
MenuDatos.add_command(label="Nuevo", command=guardar)
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
cuadroNombre.bind("<FocusOut>", habilitaBoton)

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
cuadroCif.bind("<FocusOut>", habilitaBoton)

DirLabel=Label(miFrame4,fg = "blue", bg = "steelblue1", text="Dirección", font=("Speak Pro",11))
DirLabel.grid(row=0, column=0, sticky="e", padx=0, pady=5)
cuadroDir=Entry(miFrame4,bg = "khaki1", textvariable=miDireccion, font=("Speak Pro",11))
cuadroDir.grid(row=0, column=1, padx=5, pady=5)
cuadroDir.config(fg="black", justify="left", width=66)

#==========LIST BOX (PRUEBA)==========
miFrame6=Frame()
miFrame6.pack(fill="both", expand=True) #Fill usa nomenclatura deejes de coordenadas X, Y, both o none
miFrame6.config(bg="steelblue1", width=900)


listbox = Listbox(miFrame6,fg = "blue", bg = "steelblue1",
                   font=("Speak Pro",9), selectmode="browser")
listbox.grid(row=1,column=0,sticky="e", padx=10, pady=10)
#listbox.pack(fill="both",expand=True)
#listbox.pack()

scrollbar = Scrollbar(miFrame6, command=listbox.yview)
scrollbar.grid(row=1,column=2, sticky="nsew")
#scrollbar.pack(side=RIGHT, fill=Y)

listbox.config(width=90,yscrollcommand=scrollbar.set)

def prueba(event):
    cs = listbox.curselection()
    cadena=listbox.get(cs)
    buscoID=cadena[0]
    miId.set(buscoID)
    sel()

listbox.bind('<Double-1>', prueba)

cargaLista()
scrollbar.config(command=listbox.yview)
#==========BOTONES==========
""" miFrame5b=Frame()
miFrame5b.pack(fill="both", expand=True, side="left") #Fill usa nomenclatura deejes de coordenadas X, Y, both o none
miFrame5b.config(bg="steelblue2", width=450) """
miFrame5=Frame()
miFrame5.pack(fill="both", expand=True) #Fill usa nomenclatura deejes de coordenadas X, Y, both o none
miFrame5.config(bg="steelblue3", width=900)

botonLimpiar=Button(miFrame2,text="Limpiar", font=("Speak Pro",9), bg="darkolivegreen1",fg = "blue",
                     cursor="hand2", width=5, height=1, command=limpiarCampos)
botonLimpiar.grid(row=0,column=3,sticky="e", padx=10, pady=10)


botonCancelar=Button(miFrame5,text="Salir", font=("Speak Pro",11),fg = "blue", 
                     cursor="hand2", width=10, command=salirAplicacion)
botonCancelar.grid(row=1,column=0,sticky="e", padx=10, pady=10)

botonNuevo=Button(miFrame5,text="Nuevo", font=("Speak Pro",11),fg = "blue", 
                     cursor="hand2",width=10, command=nuevo)
botonNuevo.grid(row=1,column=1,sticky="e", padx=10, pady=10)

botonBuscar=Button(miFrame5,text="Buscar", font=("Speak Pro",11), fg = "blue",
                     cursor="hand2", width=10, command=buscar)
botonBuscar.grid(row=1,column=2,sticky="e", padx=10, pady=10)

botonGuardar=Button(miFrame5,text="Guardar", font=("Speak Pro",11), bg="darkolivegreen1",fg = "blue",
                     cursor="hand2", width=10, command=guardar)
botonGuardar.grid(row=1,column=3,sticky="e", padx=10, pady=10)

botonEliminar=Button(miFrame5,text="Eliminar", font=("Speak Pro",11),bg="orange",fg = "blue", 
                     cursor="hand2",width=10, command=eliminaRegistro, disabledforeground="gray30")
botonEliminar.grid(row=1,column=4,sticky="e", padx=10, pady=10)
botonEliminar.config(state="disabled")

""" boton = ttk.Button(text="¡Hola, mundo!", command=partial(saludar, root)) -->> Llamar a la función
del boton con parametro (en este caso, formulario) """
#==========EVENTOS==========


root.mainloop()


""" bind(self, sequence=None, func=None, add=None) 
Vinculado a este widget en el evento SEQUENCE una llamada a la función FUNC.

SECUENCIA es una cadena de patrones de eventos concatenados. Un patrón de evento tiene la forma <MODIFICADOR-MODIFICADOR-TIPO-DETALLE> 
donde MODIFICADOR es uno de:
Control, Mod2, M2, Shift, Mod3, M3, Lock, Mod4, M4, Button1, B1, Mod5, M5 Button2, B2, Meta, M, Button3, B3, Alt, Button4, B4, Double, Button5, B5 Triple, Mod1, M1.
El TIPO es uno de:
Activate, Enter, Map, ButtonPress, Button, Expose, Motion, ButtonRelease, FocusIn, MouseWheel, Circulate, FocusOut, Property, Colormap, Gravity Reparent, Configure, KeyPress, Key, Unmap, Deactivate, KeyRelease Visibility, Destroy, Leave 
y DETAIL es el número de botón para ButtonPress, ButtonRelease 
y DETAIL es el Keysym para KeyPress y KeyRelease. Algunos ejemplos son <Control-Button-1> para presionar Control y el botón 1 del mouse o <Alt-A> para presionar A y la tecla Alt (se puede omitir KeyPress). Un patrón de evento también puede ser un evento virtual de la forma <<AString>> donde AString puede ser arbitrario. Este evento puede ser generado por event_generate. Si los eventos están concatenados, deben aparecer poco después uno del otro.

Se llamará a FUNC si la secuencia del evento ocurre con una instancia de Evento como argumento. Si el valor de retorno de FUNC es "break", no se invoca ninguna función vinculada adicional.

Un parámetro booleano adicional ADD especifica si se llamará a FUNC además de la otra función vinculada o si reemplazará la función anterior.
Bind devolverá un identificador para permitir la eliminación de la función vinculada con desvinculación sin pérdida de memoria.
Si se omite FUNC o SEQUENCE, se devuelve la función vinculada o la lista de eventos vinculados. """
