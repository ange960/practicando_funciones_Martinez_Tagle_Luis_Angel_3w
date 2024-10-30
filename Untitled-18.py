#18-Pero al agregar *, / obtendrás un error si intentas enviar un argumento posicional:
print("")#espacio en blanco 
print("Martinez Tagle Luis Angel 3w 1196 ") #imprime el nombre del programador
print("")#espacio en blanco 


def my_function(*, x):
    print(x)
pass 
my_function(3)