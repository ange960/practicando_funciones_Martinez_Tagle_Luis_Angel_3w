 # practicando_funciones_Martinez_Tagle_Luis_Angel_3w

1- En Python una funcion es definida usando la palabra def como palabra clave 
2- Para llamar a una funcion, use la funcion nombrada y seguida de parentesis:

![image](https://github.com/user-attachments/assets/49b42295-9d06-4582-b981-6261346b7d34)

![image](https://github.com/user-attachments/assets/1e4088a3-411c-4e32-b24c-523c9f7848a7)

3- El siguiente ejemplo tiene una función con un argumento (fname). Cuando se llama a la función, pasamos un nombre, que se usa dentro de la función para imprimir el nombre completo:

![image](https://github.com/user-attachments/assets/ea756430-c261-45ec-b211-cc24103cdc4d)

![image](https://github.com/user-attachments/assets/7928f263-b1e6-4a5c-a2d6-3bf0bc22fcaf)

4- De forma predeterminada, se debe llamar a una función con la cantidad correcta de argumentos. Lo que significa que si su función espera 2 argumentos, debe llamar a la función con 2 argumentos, ni más ni menos.

![image](https://github.com/user-attachments/assets/1d2798f7-2bf7-453d-a8a0-f803d78a480c)

![image](https://github.com/user-attachments/assets/a69dd3b6-6d82-4c73-bbd2-5ac68e2297a1)

5- Esta función espera 2 argumentos, pero solo obtiene 1:

![image](https://github.com/user-attachments/assets/c47e0add-08e9-4ff1-b63a-2ea39395ddd7)

![image](https://github.com/user-attachments/assets/562a7f2c-b461-48f2-b71d-4d599622fa8b)

6- Si no sabe cuántos argumentos se pasarán a su función, agregue un * antes del nombre del parámetro en la definición de la función.
De esta manera, la función recibirá una tupla de argumentos y podrá acceder a los elementos en consecuencia:
Si se desconoce el número de argumentos, agregue un * antes del nombre del parámetro:

![image](https://github.com/user-attachments/assets/bff93620-5144-45a1-800b-8b66f5b1d62d)

![image](https://github.com/user-attachments/assets/27974b0e-04b1-403b-9ae3-121fc42aa536)

7- También puede enviar argumentos con la sintaxis clave = valor.

![image](https://github.com/user-attachments/assets/ee6f3bc5-247b-40e7-b8ab-a21a74ddbd73)

![image](https://github.com/user-attachments/assets/5be7c585-68a0-40a8-975c-60ff08859dcc)


8- Argumentos arbitrarios de palabras clave, **kwargs
Si no sabe cuántos argumentos de palabras clave se pasarán a su función, agregue dos asteriscos: ** antes del nombre del parámetro en la definición de la función.
De esta manera, la función recibirá un diccionario de argumentos y podrá acceder a los elementos en consecuencia:
Si se desconoce el número de argumentos de palabras clave, agregue un doble ** antes del nombre del parámetro:


![image](https://github.com/user-attachments/assets/a161b5bc-6408-4c68-9b46-19181ced4c95)

![image](https://github.com/user-attachments/assets/c6d3b048-d746-4b4b-8f60-ee6712090a3b)

9- Valor de parámetro predeterminado
El siguiente ejemplo muestra cómo utilizar un valor de parámetro predeterminado.
![image](https://github.com/user-attachments/assets/057986c8-a850-4405-a38b-7f8b880f242d)

![image](https://github.com/user-attachments/assets/45a550f6-e5a3-47b5-a925-3be6739532de)

10- Pasar una lista como argumento
Puede enviar cualquier tipo de argumento de datos a una función (cadena, número, lista, diccionario, etc.) y será tratado como el mismo tipo de datos dentro de la función.

![image](https://github.com/user-attachments/assets/4f7e0de6-a11c-44d1-b2ed-9e3c4da12827)

![image](https://github.com/user-attachments/assets/c1e559a4-988b-42fd-9a92-f2406ea951d5)

11- Regresa Valores
Para permitir que una función devuelva un valor, utilice la declaración de retorno:
def my_function(x):

![image](https://github.com/user-attachments/assets/a977dca3-1db2-491a-a3aa-29868daf91c4)

![image](https://github.com/user-attachments/assets/1521b1fe-6fff-4df6-9a48-9dc7e384470c)

12- La declaración del pass
Las definiciones de función no pueden estar vacías, pero si por alguna razón tiene una definición de función sin contenido, ingrese la instrucción pass para evitar recibir un error.


![image](https://github.com/user-attachments/assets/4868e9ac-475b-44c5-bf72-e84da575dbe9)

![image](https://github.com/user-attachments/assets/5e36c826-cb46-49df-a060-97d5f5b6631b)


13- Argumentos sólo posicionales 
Puede especificar que una función pueda tener SÓLO argumentos posicionales o SÓLO argumentos de palabras clave.


![image](https://github.com/user-attachments/assets/8013ab2a-10be-4027-955b-cf2ce02944fc)

![image](https://github.com/user-attachments/assets/1cb867fe-c7e8-46e3-bcb8-8754f6bb6f30)


14
Sin , / en realidad se le permite usar argumentos de palabras clave incluso si la función espera argumentos posicionales:

![image](https://github.com/user-attachments/assets/62f4c202-cae7-46fb-ad9c-40022ab291fd)

![image](https://github.com/user-attachments/assets/b46d52b9-d408-4df9-97b1-5d2ce305d85d)


15
Pero al agregar , / obtendrá un error si intenta enviar un argumento de palabra clave:
def my_function(x, /):

![image](https://github.com/user-attachments/assets/b98f710b-f916-4449-ac15-08f363b36ee5)


![image](https://github.com/user-attachments/assets/bc353adc-71ae-4651-97be-db852f396416)

16
Argumentos de solo palabras clave
Para especificar que una función solo puede tener argumentos de palabras clave, agregue *, antes de los argumentos:

![image](https://github.com/user-attachments/assets/f5bc2e93-7adc-48d0-b8b0-fdecec646cf3)

![image](https://github.com/user-attachments/assets/1283db28-1dcd-4621-b615-3f777cbc6429)


17
Sin el *, se le permite utilizar argumentos posicionales incluso si la función espera argumentos de palabras clave:

![image](https://github.com/user-attachments/assets/618f5298-1a5a-4544-ba5f-589a044a6376)

![image](https://github.com/user-attachments/assets/ecacc0bf-8775-4e90-a091-ecb7682ad163)

18
Pero al agregar *, / obtendrás un error si intentas enviar un argumento posicional:

![image](https://github.com/user-attachments/assets/43463642-3a31-4d6d-b9c8-4a4813e91436)

![image](https://github.com/user-attachments/assets/7bc82b00-f2fc-4139-acbd-79b9c3cbe174)

19
Combine solo posicional y solo palabras clave
Puede combinar los dos tipos de argumentos en la misma función.

![image](https://github.com/user-attachments/assets/db32ab26-df66-405d-bbde-84dd38f88e91)

![image](https://github.com/user-attachments/assets/03c13c73-9576-4bd9-88f5-24ac6aeca03d)

20
Recursividad
Python también acepta la recursividad de funciones, lo que significa que una función definida puede llamarse a sí misma.

![image](https://github.com/user-attachments/assets/2ce75112-ad67-4101-8a57-8ebc11acf78e)

![image](https://github.com/user-attachments/assets/30da0707-6ffa-4995-b7d5-e73b494d05a7)

























