# Escribir un programa que le pida al 
# usuario que ingrese un número entero positivo,
# y luego imprima 
# "El número ingresado es positivo" si el 
# número es mayor que cero, o
# "El número ingresado es cero o negativo"
# si el número es menor o igual a cero.

numero_entero = int( input("ingrese un numero : " ) )

if numero_entero > 0:
    print("El número ingresado es positivo")
    
elif numero_entero <= 0:
    print("El número ingresado es cero o negativo")


    