Inventario=[]

def agregar_productos(codigo, nombre, marca, precio, existencias):
    proveedor={
       "codigo" : codigo,
        "nombre" : nombre,
        "marca" : marca,
        "precio" : precio,
        "existencias" : existencias,
        "proveedor" : []
    }
    Inventario.append(proveedor)

def buscar_productos(codigo):
    for productos in Inventario:
        if productos["codigo"] == codigo:
            return productos
    return None

def eliminar_producto(codigo):
    productos=buscar_productos(codigo)
    if productos:
        productos.remove(Inventario)
        return True
    return False

def modificar_precios(precio):
    producto=buscar_productos(precio)
    if producto:
        producto["precio"] = precio
        return True
    return False

def listar_producto(agregar_productos):
    print(f"codigo: {agregar_productos.codigo}")
    print(f"codigo: {agregar_productos.codigo}")




Inventario = []

def agregar_productos(codigo, nombre, marca, precio, existencias):
    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "marca": marca,
        "precio": precio,
        "existencias": existencias
    }
    Inventario.append(producto)

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
agregar_productos(1, 'Manzana', 'Marca A', 0.5, 100)
agregar_productos(2, 'Banana', 'Marca B', 0.3, 150)

print(buscar_productos(1))
print(eliminar_producto(2))
print(modificar_precios(1, 0.6))
listar_productos()
