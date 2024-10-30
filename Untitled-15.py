#15-Pero al agregar , / obtendrá un error si intenta enviar un argumento de palabra clave:
print("")#espacio en blanco 
print("Martinez Tagle Luis Angel 3w 1196 ") #imprime el nombre del programador
print("")#espacio en blanco 

def argumento(x, /):
 print(x)

argumento(x = 3)