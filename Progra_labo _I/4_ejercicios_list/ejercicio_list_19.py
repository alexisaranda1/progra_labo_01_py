#Crea una lista vacía y pide al usuario que ingrese una palabra.
# Luego, agrega la palabra a la lista si no se encuentra 
# ya en la lista. Repite este proceso hasta que la lista 
# tenga al menos 5 palabras.

palabra_ingresado = ""
lista_palabras = []


while len(lista_palabras) < 5:
    
    palabra_ingresado = input("ingrese una palabra : ")
    if  palabra_ingresado not in lista_palabras:
        print("{} , no esta en la lista".format(palabra_ingresado))
        lista_palabras.append(palabra_ingresado)
    elif palabra_ingresado in lista_palabras:     
        print("{} , si esta en la lista".format(palabra_ingresado))
        
        
print(lista_palabras)
        
