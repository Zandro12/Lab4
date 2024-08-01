

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

from datetime import datetime as dt
import productos as pro

Proveedores = [
    {"nombre":"Pablo Arias","Pais":"Colombia",},
    {"nombre":"Gerardo Umaña ","provincia":"alajuela",},
    {"nombre":"Mario Gomez","provincia":"alajuela",}
]

def seleccionar_proveedor():
    print("Seleccione un proveedor:")
    for idx, proveedor in enumerate(Proveedores, start=1):
        print(f"{idx}. {proveedor}")
    opcion = int(input("Ingrese el número del proveedor: "))
    return Proveedores[opcion - 1]

#from reportlab.lib.pagesizes import letter
#from productos import agregar_productos, buscar_productos, modificar_productos

def mostrar_menu():
    print(f" {BOLD} {BLUE} Bienvenido al sistema de inventario {RESET}")
    print(f" {BOLD} {BLUE} Menu Principal {RESET}")
    print(f" {BOLD} {YELLOW} 1. Agregar producto {RESET}")
    print(f" {BOLD} {YELLOW} 2. Eliminar producto {RESET}")
    print(f" {BOLD} {YELLOW} 3. Actualizar Precio de producto {RESET}")
    print(f" {BOLD} {YELLOW} 4. Listar productos {RESET}")
    print(f" {BOLD} {YELLOW} 5. Buscar producto {RESET}")
    print(f" {BOLD} {YELLOW} 6. Guardar inventario en archivo {RESET}")
    print(f" {BOLD} {YELLOW} 7. Cargar inventario desde archivo {RESET}")
    print(f" {BOLD} {YELLOW} 8. Salir {RESET}")

def main():
    while True:
        try:
            mostrar_menu()
            opcion = input(f" {BOLD} {CYAN} Seleccione una opcion: {RESET}")
            if opcion == "1":
                codigo = input("Codigo: ")
                nombre = input("Nombre: ")
                marca =  input("provedor: ")
                precio = float(input("Precio: "))
                existencias = int(input("Existencias: "))
                provedor = seleccionar_proveedor()
                pro.agregar_productos(codigo, nombre, marca, precio, existencias)

            elif opcion == "2":
                codigo = input("Codigo: ")
                if pro.eliminar_producto(codigo):
                    print("Producto eliminado.")
                else:
                    print("Producto no encontrado.")

            elif opcion == "3":
                codigo = input("Codigo: ")
                precio = float(input("Precio: "))
                pro.modificar_precios(codigo, precio)

            elif opcion == "4":
                print(f" {BOLD} {CYAN} Listado de productos {RESET}")
                pro.listar_producto()
                print(f" {BOLD} {CYAN} Fecha de actualizacion: {dt.now().strftime('%Y-%m-%d %H:%M:%S')} {RESET}")


            elif opcion == "5":
                codigo = input("Codigo: ")
                producto = pro.buscar_productos(codigo)
                if producto:
                    print(producto)
                else:
                    print("Producto no encontrado.")
        
            elif opcion == "6":
                guardar_inventario()
                print(f" {BOLD} {CYAN} Inventario guardado con exito {RESET}")
                                                             

            elif opcion == "7":
                cargar_inventario()
                print(f" {BOLD} {CYAN} Inventario cargado con exito {RESET}")

            elif opcion == "8":
                break
            else:
                print("Opcion no valida, intente de nuevo.")
        except ValueError:
            print("Opcion no valida, Intente de nuevo.")

def guardar_inventario():

    opcion = input("¿Desea guardar el inventario (txt)? ").lower()
    if opcion == "txt":
        with open("factura.txt", "w") as file:
            file.write(opcion)
        print("inventario guardado en TXT")
    else:
        print(f"{BOLD}{RED}Opción de formato de archivo no válida{RESET}")

def cargar_inventario():

    codigo = {}
    nombre = {}
    marca  = {}
    precio = {}
    existencias = {}

    try:
        archivo = input("Ingrese el nombre del archivo que desea cargar: ")
        with open(archivo, 'r') as f:
            for linea in f:
                tipo, valor = linea.strip().split(',')
                if 'codigo' in tipo:
                    codigotipo = tipo.split('')[1]
                    codigo[codigotipo] = int(valor)
                elif 'nombre' in tipo:
                    nombretipo = tipo.split('')[1]
                    nombre[nombretipo] = int(valor)
                elif 'marca' in tipo:
                    marcatipo = tipo.split('')[1]
                    marca[marcatipo] = int(valor)
                elif 'precio' in tipo:
                    preciotipo = tipo.split('')[1]
                    precio[preciotipo] = int(valor)
                elif 'existencias' in tipo:
                    existenciastipo = tipo.split('')[1]
                    existencias[existenciastipo] = int(valor)
    except FileNotFoundError:
        print(f"El archivo {archivo} no fue encontrado.")
        return codigo, nombre, marca, precio, existencias


if __name__ == "__main__":
    main()
