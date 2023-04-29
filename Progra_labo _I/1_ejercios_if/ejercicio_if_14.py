'''
Escribir un programa que le pida al usuario que ingrese un número entero,
y luego imprima "El número es múltiplo de 4 y de 6" 
si el número es múltiplo de 4 y de 6, o "El número no es múltiplo de 4 y de 6" 
si el número no es múltiplo de 4 y de 6.
'''
numero_ingresado = int( input("Ingrese un número entero: "))

if numero_ingresado % 4 == 0 and numero_ingresado % 6 == 0 :
    print("El número es divisible por 4 y por 6")
else :
    print("El número no es divisible por 4 y por 6")
