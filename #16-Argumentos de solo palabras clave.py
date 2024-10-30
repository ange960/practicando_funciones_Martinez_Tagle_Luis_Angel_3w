#16-Argumentos de solo palabras clave
#Para especificar que una función solo puede tener argumentos de palabras clave, agregue *, antes de los argumentos:

print("")#espacio en blanco 
print("Martinez Tagle Luis Angel 3w 1196 ") #imprime el nombre del programador
print("")#espacio en blanco 

def palabra_clave(*, x):
  print("EL valor de x es:" ,x )

palabra_clave(x = 90)