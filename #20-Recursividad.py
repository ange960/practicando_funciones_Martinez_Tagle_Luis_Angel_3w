#20-Recursividad
#Python también acepta la recursividad de funciones, 
#lo que significa que una función definida puede llamarse a sí misma.
print("")#espacio en blanco 
print("Martinez Tagle Luis Angel 3w 1196 ") #imprime el nombre del programador
print("")#espacio en blanco


def suma_recursiva(n):
    if n > 0:
        result = n + suma_recursiva(n - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nEjemplo de Resultados de Recursión")
suma_recursiva(5)
