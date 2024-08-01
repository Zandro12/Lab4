inventario=[]

def agregar_productos(codigo, nombre, marca, precio, existencias):
    proveedor={
       "codigo":codigo,
        "nombre":nombre,
        "marca":marca,
        "precio":precio,
        "existencias":existencias,
        "proveedor":[]
    }
    proveedor.append(inventario)

def buscar_productos(codigo):
    for productos in inventario:
        if productos["codigo"]==codigo:
            return productos
    return None

def modificar_productos(carnet, nombre, edad, calificaciones):
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