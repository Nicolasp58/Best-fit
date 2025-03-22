def best_fit(memoria, requerimiento, index):

    if not memoria or requerimiento <= 0:
        return None

    n = len(memoria)
    mejor_index = -1
    mejor_base = -1
    mejor_limite = float('inf')

    # Búsqueda en la memoria 
    for i in range(n):
        actual_index = (index + i) % n
        base, limite = memoria[actual_index]

        if limite >= requerimiento and limite < mejor_limite:
            mejor_index = actual_index
            mejor_base = base
            mejor_limite = limite

    if mejor_index == -1:
        return None  # No hay espacio suficiente

    nueva_memoria = memoria[:]

    # Si el espacio es igual al requerimiento
    if mejor_limite == requerimiento:
        nueva_memoria.pop(mejor_index)
        nuevo_indice = 0 if mejor_index == len(memoria) - 1 else mejor_index
    else:
        nueva_base = mejor_base + requerimiento
        nuevo_limite = mejor_limite - requerimiento
        nueva_memoria[mejor_index] = (nueva_base, nuevo_limite)
        nuevo_indice = mejor_index 

    return nueva_memoria, mejor_base, mejor_limite, nuevo_indice
