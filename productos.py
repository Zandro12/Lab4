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
    return None

def modificar_precios(precio):
    producto=buscar_productos(precio)
    if producto:
        producto["precio"] = precio
        return True
    return False

def mostrar_productos(agregar_productos):
    print(f"codigo: {agregar_productos.codigo}")
    print(f"codigo: {agregar_productos.codigo}")





