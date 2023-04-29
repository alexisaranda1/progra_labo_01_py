#Crea una lista de números enteros y pide al usuario que ingrese otro número entero.
# Luego, busca el número ingresado en la lista y muestra la posición 
# en la que se encuentra. Si el número no se encuentra en la lista, muestra
# un mensaje indicando que no se encontró



lista_numeros = [12, 5, 10, 500, 8, 7, 2, 6]

numero_ingresado = int(input("Ingrese un número entero: "))

flag = False

for i in range(len(lista_numeros)):
    if numero_ingresado == lista_numeros[i]:
       posicion = i
       flag = True
       break
    
if flag == True:
    print("El número {0} se encuentra en la posición {1} de la lista."
        .format(numero_ingresado, posicion))
else:
    print("El número {} no se encuentra en la lista."
              .format(numero_ingresado))
       
