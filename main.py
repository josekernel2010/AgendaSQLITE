import os

from  tabulate import tabulate

from contacto import *

#funcionalidad para crear la tabla
con = conectar()
crear_tabla(con)

#menu
def iniciar():
    while True:

        print('Selecione una opción:')
        print('\t1. Añadir un contacto')
        print('\t2. Mostrar todos los contactos')
        print('\t3. Buscar un contacto')
        print('\t4. Modificar un contacto')
        print('\t5. Eliminar un contacto')
        print('\t6. Salir de la aplicación')
        opcion = input('Ingrese una opción: ')
        os.system('cls')

        if opcion == '1':
            nuevo_contacto()
        elif opcion == '2':
            ver_contacto()
        elif opcion == '3':
            buscar_contacto()
        elif opcion == '4':
            modificar_contacto()
        elif opcion == '5':
            eliminar_contacto()
        elif opcion == '6':
            break


#creacion de contacto nuevo
def nuevo_contacto():
    nombre = input('Ingrese el nombre: ')
    apellido = input('Ingrese el apellido: ')
    empresa = input('Ingrese la empresa: ')
    telephone = input('Ingrese el telefono: ')
    email = input('Ingrese email: ')
    address = input('Ingrese su dirección: ')
    respuesta = registrar(nombre, apellido, empresa, telephone, email, address)
    print(respuesta)

#funcion para mostrar todos los contactos
def ver_contacto():
    dato = mostrar()
    headers = ['Nombre', 'Apellido', 'Empresa', 'Telefono', 'Email', 'Dirección']
    tabla = tabulate(dato, headers=headers, tablefmt='fancy_grid')
    print(tabla)


#funcion para mostrar un contacto
def buscar_contacto():
    id = input('Ingrese el id del contacto: ')
    dato = buscar(id)
    headers = ['id','Nombre', 'Apellido', 'Empresa', 'Telefono', 'Email', 'Dirección']
    tabla = tabulate(dato, headers=headers, tablefmt='fancy_grid')
    print(tabla)


#funcion por medio de id para mostrar un contacto
def buscar(id):
    datos =[]
    try:
        con = conectar()
        cursor = con.cursor()
        cursor.execute('''SELECT * FROM contacto WHERE id =?''', (id,))
        datos = cursor.fetchall()
        con.close()
        print(datos)
    except sqlite3.Error as error:
        print("Ha ocurrido un error: ",error)
    return datos

def modificar_contacto():
    id = input('Ingrese el id del contacto: ')
    nombre = input('Ingrese el nombre: ')
    apellido = input('Ingrese el apellido: ')
    empresa = input('Ingrese la empresa: ')
    telephone = input('Ingrese el telefono: ')
    email = input('Ingrese email: ')
    address = input('Ingrese su dirección: ')
    respuesta = modificar(id, nombre, apellido, empresa, telephone, email, address)
    print(respuesta)

def eliminar_contacto():
    id = input('Ingrese el id del contacto: ')
    respuesta = eliminar(id)
    print(respuesta)
    

if __name__ == '__main__':
    iniciar()