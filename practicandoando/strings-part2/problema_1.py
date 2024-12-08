def verificar_apellido_paterno(apellido_paterno):
    vocales = "aeiouAEIOU"
    contador = 0
    for letter in apellido_paterno:
        if letter in vocales:
            contador = contador + 1

    if contador > 2:
        return True
    else:
        return False





apellido = input("Ingresa tu apellido paterno: ")
resul = verificar_apellido_paterno(apellido)
print(resul)