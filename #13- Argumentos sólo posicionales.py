#13- Argumentos sólo posicionales 
#Puede especificar que una función pueda tener SÓLO argumentos posicionales o SÓLO argumentos de palabras clave.

#Para especificar que una función solo puede tener argumentos posicionales, agregue , / después de los argumentos:

#Ícono de validado por la comunidad
print("")#espacio en blanco 
print("Martinez Tagle Luis Angel 3w 1196 ") #imprime el nombre del programador
print("")#espacio en blanco 

def my_function(x, /):
    print("El valor de x es:", x)

# Llamamos a la función pasando el valor solo por posición
my_function(5)  # Esto imprimirá "El valor de x es: 5"