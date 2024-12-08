def modificar_lista_tareas():
    tareas = ["tarea1", "tarea2", "tarea3"]
    tareas.append("tarea4")
    tareas.remove("tarea2")
    tareas.clear()
    print(tareas)


modificar_lista_tareas()    