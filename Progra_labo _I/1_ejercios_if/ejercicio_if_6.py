'''
Escribir un programa que le pida al usuario que ingrese su nombre y su edad,
y 
luego imprima "Puedes votar" si la edad es mayor o igual a 18 y menor o igual a 65, 
o "No puedes votar" si la edad es menor a 18 o mayor a 65.
'''
nombre_ingresado =  input(" Ingrese su nombre: " ) 
edad_ingresado = int (input(" Ingrese su edad: ") )

if edad_ingresado >= 18 and edad_ingresado <= 65:
    print("Puedes votar")
elif edad_ingresado <18 or edad_ingresado > 65:
    print("No puedes votar")