def comprobrar_numeros(numero_cliente):
    codigo_pais = numero_cliente[0:3]
    if "+51" == codigo_pais:
        return False
    else:
        return True

numero_cliente = input("ingresa tu número: ")
resul = comprobrar_numeros(numero_cliente)
print(resul)

