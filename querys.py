from tkinter import messagebox
import sqlite3

def ConexionBBDD(dbName, myQuery):
    #print("entrada función ConexionBBDD")
    miConexion=sqlite3.connect(dbName)

    miCursor=miConexion.cursor()
    
    try:
        miCursor.execute(myQuery)
        messagebox.showinfo("BBDD", "BBDD Creada con éxito.")
    except:
        a=0
        #messagebox.showwarning("¡ATENCIÓN!", "La BBDD ya existe")
    miConexion.close()

