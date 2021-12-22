from conexion import *

#funcion para registrar un contacto
def registrar(nombre, apellido, empresa, telephone, email, address):
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = '''INSERT INTO contacto(
        nombre, apellido, empresa, telephone, email, address)
        values (?,?,?,?,?,?)
        '''
        datos = (nombre, apellido, empresa, telephone, email, address)
        cursor.execute(sentencia_sql, datos)
        con.commit()
        con.close()
        return 'Registro correcto'
    except sqlite3.Error as error:
        print('Ha ocurrido un error al registrar ', error)


def mostrar():
    datos = []
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = '''SELECT * FROM contacto'''
        cursor.execute(sentencia_sql)
        datos = cursor.fetchall()
        con.close()
    except sqlite3.Error as error:
        print('Error al mostrar los contactos ', error)
    return datos


def modificar(id,nombre, apellido, empresa, telephone, email, address):
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = '''UPDATE contacto SET nombre = ?, apellido = ?, empresa = ?,
         telephone = ?, email = ?, address = ? WHERE id = ?'''
        datos = (nombre, apellido, empresa, telephone, email, address, id)
        cursor.execute(sentencia_sql, datos)
        con.commit()
        con.close()
        return 'Modificacion correcta'

    except sqlite3.Error as error:
        print('Error al modificar los contactos ', error)
    pass

def eliminar(id):
    try:
        con = conectar()
        cursor = con.cursor()
        sentencia_sql = '''DELETE FROM contacto WHERE id = ?'''
        cursor.execute(sentencia_sql, (id,))
        con.commit()
        con.close()
        return 'Eliminacion correcta'
    except sqlite3.Error as error:
        print('Error al eliminar los contactos ', error)
