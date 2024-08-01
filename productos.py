Inventario = []

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
    producto = buscar_productos(codigo)
    if producto != "Producto no encontrado":
        Inventario.remove(producto)
        return "Producto eliminado"
    return "Producto no encontrado"

def modificar_precios(precio):
    producto=buscar_productos(precio)
    if producto:
        producto["precio"] = precio
        return True
    return False

def listar_producto(agregar_productos):
    print(f"codigo: {agregar_productos.codigo}")
    print(f"codigo: {agregar_productos.codigo}")








