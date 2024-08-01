

RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

import gestor_estudiantes as ge

def mostrar_menu():
    print(f" {BOLD} {BLUE} Bienvenido al sistema de gestion de estudiantes {RESET}")
    print(f" {BOLD} {BLUE} Menu Principal {RESET}")
    print(f" {BOLD} {YELLOW} 1. Agregar estudiante {RESET}")
    print(f" {BOLD} {YELLOW} 2. Buscar estudiante {RESET}")
    print(f" {BOLD} {YELLOW} 3. Modificar estudiante {RESET}")
    print(f" {BOLD} {YELLOW} 4. Eliminar estudiante {RESET}")
    print(f" {BOLD} {YELLOW} 5. Agregar calificaciones {RESET}")
    print(f" {BOLD} {YELLOW} 6. Mostrar promedio de calificaciones {RESET}")
    print(f" {BOLD} {YELLOW} 7. Mostrar lista de aprobados y reprobados {RESET}")
    print(f" {BOLD} {YELLOW} 8. Salir {RESET}")

def main():
    while True:
        try:
            mostrar_menu()
            opcion = input(f" {BOLD} {CYAN} Seleccione una opcion: {RESET}")
            if opcion == "1":
                carnet = input("Carnet: ")
                nombre = input("Nombre: ")
                edad = int(input("Edad: "))
                ge.agregar_estudiante(carnet, nombre, edad)

            elif opcion == "2":
                carnet = input("Carnet: ")
                estudiante = ge.buscar_estudiante(carnet)
                if estudiante:
                    print(estudiante)
                else:
                    print("Estudiante no encontrado.")

            elif opcion == "3":
                carnet = input("Carnet: ")
                nombre = input("Nuevo nombre: ")
                edad = int(input("Nueva edad: "))
                calificaciones = input("Calificaciones: ")
                if ge.modificar_estudiante(carnet, nombre, edad, calificaciones):
                    print("Estudiante modificado.")
                else:
                    print("Estudiante no encontrado.")

            elif opcion == "4":
                carnet = input("Carnet: ")
                if ge.eliminar_estudiante(carnet):
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
                if ge.calificar_estudiante(carnet, calificaciones):
                    print("Notas agregadas con exito!")
                else:
                    print("Estudiante no encontrado.")

            elif opcion == "6":
                carnet = input("Carnet: ")
                promedio = ge.promedio_calificaciones(carnet)
                print(f"Promedio de calificaciones: {promedio}")

            elif opcion == "7":
                aprobados, reprobados = ge.lista_aprobados_reprobados()
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