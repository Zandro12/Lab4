

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
                carnet = input("Carnet: ")
                promedio = pro.promedio_calificaciones(carnet)
                print(f"Promedio de calificaciones: {promedio}")

            elif opcion == "7":
                aprobados, reprobados = pro.lista_aprobados_reprobados()
                print("Aprobados:")
                for estudiante in aprobados:
                    print(estudiante)
                print("Reprobados:")
                for estudiante in reprobados:
                    print(estudiante)

            elif opcion == "8":
                break
            else:
                print("Opcion no valida, intente de nuevo.")
        except ValueError:
            print("Opcion no valida, Intente de nuevo.")

def cargarEspaciosYPrecios(archivo):
    codigo = {}
    nombre = {}
    marca  = {}
    precio = {}
    existencias = {}

    try:
        with open(archivo, 'r') as f:
            for linea in f: # Imprimir la línea actual
                tipo, valor = linea.strip().split(': ') #linea.strip() elimina cualquier espacio en blanco ,#split(': ') divide la cadena en dos partes usando la cadena
                if 'codigo' in tipo:
                    codigo = tipo.split('')[1]
                    codigo[codigotipo] = int(valor)
                elif 'precios' in tipo:
                    precio_tipo = tipo.split('')[1]
                    precios[precio_tipo] = int(valor)
    except FileNotFoundError:
        print(f"El archivo {archivo} no fue encontrado.")
    return espacios, precios

def guardarFactura(pfactura):
    opcion = input("¿En qué formato desea guardar la factura (txt o pdf)? ").lower()
    if opcion == "txt":
        with open("factura.txt", "w") as file:
            file.write(pfactura)
        print("Factura guardada en TXT")
    elif opcion == "pdf":
        c = canvas.Canvas("factura.pdf")
        width, height = letter
        c.drawString(100, height - 40, "Factura")
        y = height - 60
        for line in pfactura.split('\n'):
            c.drawString(100, y, line)
            y -= 20
        c.save()
        print("Factura guardada en PDF")
    else:
        print(f"{BOLD}{RED}Opción de formato de archivo no válida{RESET}")

if __name__ == "__main__":
    main()
