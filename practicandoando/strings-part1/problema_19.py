def imprimir_subcadena(cadena, indice_inicio, indice_fin):
    subcadena = cadena[indice_inicio:indice_fin]
    return subcadena


texto = input("Ingresa un texto: ")
numero_1 = int(input("Introduce el primer número: "))
numero_2 = int(input("Introduce el segundo número: "))

resultado = imprimir_subcadena(texto, numero_1, numero_2)
print(resultado)