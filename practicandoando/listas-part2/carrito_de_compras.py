def modificar_carrito_compras():
    carrito = ["manzana", "banana"]
    de_compras = ["pera", "uva"]
    carrito.append("naranja")
    carrito.extend(de_compras)
    carrito.remove("banana")
    print(carrito)

modificar_carrito_compras()