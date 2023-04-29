#Dado un número entero n, imprimir todos los números impares menores o iguales a n.
import os
def clear_console() -> None:
    """
    It waits for the user to hit enter 
    to clear the console and redisplay the appropriate thing.
    """
    _ = input('Press a key to continue...')
    os.system('cls')
numero_ingresado = input("ingrese un numero entero: ")
numero = int (numero_ingresado)

i = 0

while i < numero:
    i += 1
    if i % 2 != 0:
        print(i)
    
clear_console()
    
