''''
Escribir un programa que le pida al usuario que ingrese dos números enteros, 
y luego imprima "Los dos números son iguales" si los dos números son iguales, 
"El primer número es mayor" si el primer número es mayor que el segundo,
o "El segundo número es mayor" si el segundo número es mayor que el primero.

'''
primer_entero = int( input("Ingrese el primer entero : " ) )
segundo_entero = int( input("Ingrese el segundo entero : " ) )

if primer_entero == segundo_entero :
     print("Los dos números son iguales")
elif primer_entero > segundo_entero:
    print("El primer número es mayor")
elif primer_entero < segundo_entero: 
    print("El segundo número es mayor")
