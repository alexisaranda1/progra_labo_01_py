'''
Escribir un programa que le pida al usuario que ingrese un número entero positivo, 
y luego imprima "El número es un cuadrado perfecto" si el número es un cuadrado perfecto,
o "El número no es un cuadrado perfecto" si el número no es un cuadrado perfecto.
'''
numero = int(input("Ingrese un número entero positivo: "))
flag= False
if numero > 0:
    
    for i in range(1, numero):
    
        if i * i == numero:
            print("El número es un cuadrado perfecto\n")
            flag = True
    if flag == False:
        print("El número no es un cuadrado perfecto\n")
else :
    print("Numero incorrecto...")
 