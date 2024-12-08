

'''
def buscar_producto(producto):
    productos_disponibles = ["laptop", "mouse", "teclado", "monitor", "webcam"]

    if producto in productos_disponibles:
        return True
    else:
        return False

'''

def buscar_producto(producto) -> bool:
    productos_disponibles = ["laptop", "mouse", "teclado", "monitor", "webcam"]

    existe_en_la_lista: bool = producto in productos_disponibles

    return existe_en_la_lista

resul = buscar_producto("mouse2")
print(resul)

