def es_elegible_para_descuento(membresia: bool, cantidad_compra: float) -> bool:
    if membresia or cantidad_compra > 100:
        return True
    else:
        return False

print(es_elegible_para_descuento(False, 10))



