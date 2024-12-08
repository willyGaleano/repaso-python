def modificar_productos():
    productos = [100, 200, 300, 400, 500]
    productos[1] = 250
    #productos.remove(200)
    #productos.insert(1, 250)
    productos.remove(400)
    print(productos)


modificar_productos()