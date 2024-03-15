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

def devReg(dbName, myQuery, dev=False, datos=""):
    """Parametros de la función:
        dbName: Nombre de la base de datos
        myQuery: Consulta completa. Comoponer antes de hacer la llamada
        dev: 
        datos: lista de datos con valores de consulta. Parámetro opcional"""
    miConexion=sqlite3.connect(dbName)
    miCursor=miConexion.cursor()

    if dev==True:
        if datos!="":
            miCursor.execute(myQuery, (datos))
            laSociedad=miCursor.fetchall()
            miConexion.commit()
            miConexion.close()
            return laSociedad
        else:
            miCursor.execute(myQuery)
            laSociedad=miCursor.fetchall()
            miConexion.commit()
            miConexion.close()
            return laSociedad
    else:
        miCursor.execute(myQuery)
        miConexion.commit()
        miConexion.close()
        


def buscarReg(dbName, myQuery, datos):
    
    miConexion=sqlite3.connect(dbName)
    miCursor=miConexion.cursor()

    miCursor.execute(myQuery)
    
    laSociedad=miCursor.fetchall()
    
    miConexion.commit()
    miConexion.close()

    return laSociedad

def seleccionarReg(dbName, myQuery, datos):

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