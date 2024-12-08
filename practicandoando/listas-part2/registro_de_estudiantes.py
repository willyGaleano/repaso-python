def modificar_lista_del_curso():
    estudiantes = ["Ana", "Luis", "Pedro"]
    estudiantes.insert(1, "María")
    del estudiantes[0]
    print(estudiantes)


modificar_lista_del_curso()