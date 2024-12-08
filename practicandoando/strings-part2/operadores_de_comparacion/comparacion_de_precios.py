def es_precio_menor(precio1: float, precio2: float) -> bool:
    if precio1 < precio2:
        return True
    else:
        return False

print(es_precio_menor(33, 22))