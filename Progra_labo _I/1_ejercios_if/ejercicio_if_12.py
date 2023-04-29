'''
Escribir un programa que le pida al usuario que ingrese dos números enteros,
y luego imprima "El primer número es positivo" si el primer número es mayor que cero,
"El segundo número es positivo" si el segundo número es mayor que cero, 
o "Ambos números son negativos" si los dos números son negativos.
'''

primer_entero = int( input("Ingrese el primer entero : " ) )
segundo_entero = int( input("Ingrese el segundo entero : " ) )


if primer_entero > 0 :
    print("El primer número es positivo")
if segundo_entero > 0 :
    print("El segundo número es positivo")
elif primer_entero < 0 and segundo_entero < 0 :
     print("Ambos números son negativos")
 