def disminuye_en_uno(numero: int) -> int:
    return numero - 1


def agregar_elemento(lista_edades: list[int], edad: int) -> None:
    lista_edades.append(edad)

def agregar_elemento_v2(lista_edades: list[int], edad: int) -> list[int]:
    lista_edades_copia = lista_edades.copy()
    lista_edades_copia.append(edad)

    return lista_edades_copia


#Parametro por valor
numero = 20
numero_disminuido = disminuye_en_uno(numero)
print(f"numero: {numero}")
print(f"numero_disminuido: {numero_disminuido}")

#Parametro por referencia
edades = [10, 20, 30, 50, 60]
edad_snaider = 8
nuevas_edades = agregar_elemento_v2(edades, edad_snaider)
print(f"edades: {edades}")
print(f"nuevas edades: {nuevas_edades}")



