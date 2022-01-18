import os
import pyfiglet
from tabulate import tabulate

from contacto import *

#funcionalidad para crear la tabla
con = conectar()
crear_tabla(con)

#menu
def iniciar():
    os.system("cls")
    while True:
        titulo = 'Agenda'
        a = pyfiglet.figlet_format(titulo)
        print(a)
        print("**************************")
        print(':: Selecione una opción ::')
        print('**************************')
        print()
        print('\t1. Añadir un contacto')
        print('\t2. Mostrar todos los contactos')
        print('\t3. Buscar un contacto')
        print('\t4. Modificar un contacto')
        print('\t5. Eliminar un contacto')
        print('\t6. Salir de la aplicación')
        print()
        opcion = input('\t:: Ingrese una opción: ')

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


# 1. creacion de contacto nuevo
def nuevo_contacto():
    nombre = input('Ingrese el nombre: ')
    apellido = input('Ingrese el apellido: ')
    empresa = input('Ingrese la empresa: ')
    telephone = input('Ingrese el telefono: ')
    email = input('Ingrese email: ')
    address = input('Ingrese su dirección: ')
    respuesta = registrar(nombre, apellido, empresa, telephone, email, address)
    os.system("cls")
    print(25*"-")
    print(respuesta)
    print(25*"-")
    input("presione enter para continuar... ")
    os.system("cls")


# 2. funcion para mostrar todos los contactos
def ver_contacto():
    dato = mostrar()
    headers = ['Id','Nombre', 'Apellido', 'Empresa', 'Telefono', 'Email', 'Dirección']
    tabla = tabulate(dato, headers=headers, tablefmt='fancy_grid')
    #os.system('cls')
    print(tabla)
    input("presione enter para continuar... ")
    os.system('cls')

#funcion para mostrar un contacto
def buscar_contacto():
    id = input('Ingrese el id del contacto: ')
    dato = buscar(id)
    if dato != []:
        headers = ['id','Nombre', 'Apellido', 'Empresa', 'Telefono', 'Email', 'Dirección']
        tabla = tabulate(dato,headers=headers, tablefmt='fancy_grid')
        print(tabla)
        input("presione enter para continuar... ")
        os.system('cls')
    else:
        print("----------------------------")
        print(":: El contacto no esxiste ::")
        print("----------------------------")
        input("presione enter para continuar... ")
        os.system('cls')

def mostrar_contacto(id):
    dato = buscar(id)
    if dato != []:
        headers = ['id', 'Nombre', 'Apellido', 'Empresa', 'Telefono', 'Email', 'Dirección']
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

    except sqlite3.Error as error:
        print("Ha ocurrido un error: ",error)
    return datos

def modificar_contacto():
    id = input('Ingrese el id del contacto: ')
    if buscar(id) == []:
        print("------------------------------------")
        print("El contacto a modificar no existe...")
        print("------------------------------------")
        input("presione enter para salir...")
        os.system("cls")
    else:
        mostrar_contacto(id)
        print()
        nombre = input('\tIngrese el nombre: ')
        apellido = input('\tIngrese el apellido: ')
        empresa = input('\tIngrese la empresa: ')
        telephone = input('\tIngrese el telefono: ')
        email = input('\tIngrese email: ')
        address = input('\tIngrese su dirección: ')
        respuesta = modificar(id, nombre, apellido, empresa, telephone, email, address)
        os.system("cls")
        print(len(respuesta)*"-")
        print(respuesta)
        print(len(respuesta) * "-")
        input("presione enter para continuar... ")
        os.system('cls')

def eliminar_contacto():
    id = input('Ingrese el id del contacto: ')
    dato = buscar(id)
    if dato == []:
        print("------------------------------------")
        print("El contacto a eliminar no existe...")
        print("------------------------------------")
        input("presione enter para salir...")
        os.system("cls")

    os.system("cls")

    if dato != []:
        respuesta = eliminar(id)
        print(len(respuesta)*"-")
        print(respuesta)
        print(len(respuesta) * "-")
        input("presione enter para salir...")
        os.system("cls")



if __name__ == '__main__':
    iniciar()