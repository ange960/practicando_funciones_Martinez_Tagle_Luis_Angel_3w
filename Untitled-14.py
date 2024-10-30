#14-Sin , / en realidad se le permite usar argumentos de palabras clave incluso
# si la función espera argumentos posicionales:
print("")#espacio en blanco 
print("Martinez Tagle Luis Angel 3w 1196 ") #imprime el nombre del programador
print("")#espacio en blanco 

def my_function(x):
    print("El valor de x es:", x)

# Llamamos a la función pasando el valor con el nombre del parámetro
my_function(x=3)  # Esto imprimirá "El valor de x es: 3"
