def remplazar(precio):
    nuevo_precio = precio.replace("-", ".")

    return nuevo_precio


mismo_precio = input("Ingresa el precio del producto: ")
resul = remplazar(mismo_precio)
print(resul)
