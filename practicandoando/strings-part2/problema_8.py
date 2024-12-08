def separar_marca(texto):
    texto = texto.split("-")
    return texto

conversion_lista = "Rav4-Cross-Avanza-Yaris-Fortune"
resul = separar_marca(conversion_lista)
print(resul)