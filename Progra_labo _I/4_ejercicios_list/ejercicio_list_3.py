#Crea una lista vacía y pide al usuario que ingrese
# números enteros hasta que ingrese un número negativo. 
# Luego, muestra la suma de todos los números ingresados.

lista = []

numero = 0
suma = 0


while numero >= 0: 
    numero = int ( input("ingrese un número : "))
    if numero >= 0:
        lista.append(numero)
        suma += numero 
    
print("lista de numeros es {0} y la suma de todos los numeros : {1}".format
      (lista,suma))
