def verificar_numero_celular(numero_celular):
    if numero_celular[0:3] == "+51":
        return numero_celular[3:]
    else:
        return numero_celular

number_celular = input("Ingresa tu número de celular: ")
resultado = verificar_numero_celular(number_celular)
print(resultado)



