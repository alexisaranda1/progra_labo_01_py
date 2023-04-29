'''Escribir un programa que le pida al usuario que ingrese un número entero,
y luego imprima "El número ingresado es par" si el número es divisible por 2,
o "El número ingresado es impar" si el número no es divisible por 2.
'''
numero_entero = int( input("ingrese un numero : " ) )

if numero_entero % 2 == 0:
    print("El número ingresado es par")
    
elif numero_entero % 2 != 0:  
    print( "El número ingresado es impar")

  