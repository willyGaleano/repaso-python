def calcular_promedio(notas: list) -> float:
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

print(calcular_promedio([3, 1, 4, 2]))