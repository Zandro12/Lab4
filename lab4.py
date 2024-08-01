estudiantes=[]

def agregar_estudiante(carnet, nombre, edad):
    estudiante={
        "carnet":carnet,
        "nombre":nombre,
        "eda":edad,
        "calificaciones":[]
    }
    estudiantes.append(estudiante)

def buscar_estudiante(carnet):
    for estudiante in estudiantes:
        if estudiante["carnet"]==carnet:
            return estudiante
    return None

def modificar_estudiante(carnet, nombre, edad, calificaciones):
    estudiante=buscar_estudiante(carnet)
    if estudiante:
        estudiante["nombre"]=nombre
        estudiante["edad"]=edad
        estudiante["calificaciones"]=calificaciones
        return True
    return False

def eliminar_estudiante(carnet):
    estudiante=buscar_estudiante(carnet)
    if estudiante:
        estudiantes.remove(estudiante)
        return True
    return False