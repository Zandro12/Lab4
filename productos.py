Inventario = []
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

def agregar_productos(codigo, nombre, marca, precio, existencias):
    for producto in Inventario:
        if producto["codigo"] == codigo:
            return "Error: El código ya está en uso"
    proveedor={
       "codigo" : codigo,
        "nombre" : nombre,
        "marca" : marca,
        "precio" : precio,
        "existencias" : existencias,

    }
    Inventario.append(proveedor)
    for producto in Inventario:
        if producto["codigo"] == codigo:
            return "Error: El código ya existe"
def buscar_productos(codigo):
    for productos in Inventario:
        if productos["codigo"] == codigo:
            return productos
    return None

def eliminar_producto(codigo):
    producto = buscar_productos(codigo)
    if producto != "Producto no encontrado":
        Inventario.remove(producto)
        return "Producto eliminado"
    return "Producto no encontrado"

def modificar_precios(codigo, nuevo_precio):
    producto = buscar_productos(codigo)
    if producto != "Producto no encontrado":
        producto["precio"] = nuevo_precio
        return "Precio modificado"
    return "Producto no encontrado"

def listar_producto():
    for producto in Inventario:
        print(producto)




"""
Inventario = []

def agregar_productos(codigo, nombre, marca, precio, existencias):
    # Verificar si el código ya existe
    for producto in Inventario:
        if producto["codigo"] == codigo:
            return "Error: El código ya está en uso"
    
    nuevo_producto = {
        "codigo": codigo,
        "nombre": nombre,
        "marca": marca,
        "precio": precio,
        "existencias": existencias
    }
    Inventario.append(nuevo_producto)
    return "Producto agregado"

def buscar_productos(codigo):
    for producto in Inventario:
        if producto["codigo"] == codigo:
            return producto
    return "Producto no encontrado"

def eliminar_producto(codigo):
    producto = buscar_productos(codigo)
    if producto != "Producto no encontrado":
        Inventario.remove(producto)
        return "Producto eliminado"
    return "Producto no encontrado"

def modificar_precios(codigo, nuevo_precio):
    producto = buscar_productos(codigo)
    if producto != "Producto no encontrado":
        producto["precio"] = nuevo_precio
        return "Precio modificado"
    return "Producto no encontrado"

def listar_productos():
    for producto in Inventario:
        print(f"Código: {producto['codigo']}, Nombre: {producto['nombre']}, Marca: {producto['marca']}, Precio: {producto['precio']}, Existencias: {producto['existencias']}")

# Ejemplo de uso
print(agregar_productos(1, 'Manzana', 'Marca A', 0.5, 100))
print(agregar_productos(2, 'Banana', 'Marca B', 0.3, 150))
print(agregar_productos(1, 'Naranja', 'Marca C', 0.4, 200))  # Intento de agregar un producto con un código existente

print(buscar_productos(1))
print(eliminar_producto(2))
print(modificar_precios(1, 0.6))
listar_productos()
"""











