

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

import productos as pro
#from productos import agregar_productos, buscar_productos, modificar_productos

def mostrar_menu():
    print(f" {BOLD} {BLUE} Bienvenido al sistema de gestion de estudiantes {RESET}")
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
                marca =  input("Marca: ")
                precio = float(input("Precio: "))
                existencias = int(input("Existencias: "))
                pro.agregar_productos(codigo, nombre, marca, precio, existencias)

            elif opcion == "2":
                carnet = input("Carnet: ")
                estudiante = pro.buscar_productos(carnet)
                if estudiante:
                    print(estudiante)
                else:
                    print("Estudiante no encontrado.")

            elif opcion == "3":
                carnet = input("Carnet: ")
                nombre = input("Nuevo nombre: ")
                edad = int(input("Nueva edad: "))
                calificaciones = input("Calificaciones: ")
                if pro.modificar_produtos(carnet, nombre, edad, calificaciones):
                    print("Estudiante modificado.")
                else:
                    print("Estudiante no encontrado.")

            elif opcion == "4":
                carnet = input("Carnet: ")
                if pro.eliminar_estudiante(carnet):
                    print("Estudiante eliminado.")
                else:
                    print("Estudiante no encontrado.")

            elif opcion == "5":
                carnet = input("Agregar Carnet de estudiante: ")
                calificaciones = []
                while True:
                    materia = input("Agregar nueva materia o 'fin' para terminar: ")
                    if materia.lower() == 'fin':
                        break
                    nota = float(input("Nota: "))
                    calificaciones.append((materia, nota))
                if pro.calificar_estudiante(carnet, calificaciones):
                    print("Notas agregadas con exito!")
                else:
                    print("Estudiante no encontrado.")

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

if __name__ == "__main__":
    main()