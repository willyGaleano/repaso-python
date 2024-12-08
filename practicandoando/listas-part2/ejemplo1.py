'''
Ejercicio
Escribe una función llamada modify_list que tome una lista y un valor como argumentos. La función debe hacer lo siguiente:

1. Si el valor está en la lista, eliminar la primera aparición del valor usando el método remove.
2. Si el valor no está en la lista, eliminar el último elemento de la lista usando el método pop.
3. Retornar la lista modificada.

'''


def modify_list(lista_frutas: list[str], fruta: str) -> list[str]:
    if(fruta in lista_frutas):
        lista_frutas.remove(fruta)
    else:
        lista_frutas.pop()

    return lista_frutas


lista_frutas_input = ["manzana", "pera", "fresa", "melón", "plátano", "fresa"]
fruta_a_buscar = "fresa"

lista_frutas_input_modificada_1 = modify_list(lista_frutas_input, fruta_a_buscar)
print(f"lista_frutas_input: {lista_frutas_input}")
print(f"lista_frutas_input_modificada_1: {lista_frutas_input_modificada_1}")


