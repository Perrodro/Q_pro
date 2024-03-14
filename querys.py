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

def buscarReg(dbName, myQuery, datos):
    
    miConexion=sqlite3.connect(dbName)
    miCursor=miConexion.cursor()

    miCursor.execute(myQuery)
    
    laSociedad=miCursor.fetchall()
    
    miConexion.commit()
    miConexion.close()

    return laSociedad

def eliminaReg(dbName, myQuery):
    miConexion=sqlite3.connect(dbName)
    miCursor=miConexion.cursor()

    miCursor.execute(myQuery)

    miConexion.commit()

    messagebox.showinfo("BBDD", "Registro eliminado con éxito")

    miConexion.close()

def insertaReg (dbName, myQuery, datos):
    miConexion=sqlite3.connect(dbName)
    miCursor=miConexion.cursor()

    miCursor.execute (myQuery, (datos))
    miConexion.commit()

    miConexion.close()

def actualizaReg(dbName, myQuery, datos):
    miConexion=sqlite3.connect(dbName)
    miCursor=miConexion.cursor()

    miCursor.execute (myQuery, (datos))
    miConexion.commit()

    miConexion.close()