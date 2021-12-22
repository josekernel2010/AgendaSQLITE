import sqlite3

#método de conecion a la base de datos
def conectar():
    try:
        conexion = sqlite3.connect('contactos.db')
        print('Se ha conectado a la base de datos')
        return conexion
    except sqlite3.Error as error:
        print('Ha ocurrido un error en la coneccion ', error)

#creando sentencia sql
def crear_tabla(conexion):
    cursor = conexion.cursor()
    sentencia_sql = ''' CREATE TABLE IF NOT EXISTS contacto(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre VARCHAR(80) NOT NULL,
    apellido VARCHAR(80) NOT NULL,
    empresa VARCHAR(150) NOT NULL,
    telephone VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL
    )'''
    #ejecutando sentencia sql
    cursor.execute(sentencia_sql)
    #guardando cambios
    conexion.commit()