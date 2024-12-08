def son_mismos_objetos(objeto1: any, objeto2: any) -> bool:
    return objeto1 is objeto2


lista1 = ["hola"]#dirección de memoria ABC1
lista2 = ["hola"]#dirección de memoria ABC2
lista3 = lista1 #dirección de memoria ABC1, porque lista3 apunta a la misma dirección de memoria que lista1

print(son_mismos_objetos(lista1, lista3))