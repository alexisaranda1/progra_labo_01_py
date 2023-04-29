'''
Escribir un programa que le pida al usuario que ingrese una letra, 
y luego imprima "Es una vocal" si la letra es una vocal (a, e, i, o, u), 
o "Es una consonante" si la letra es una consonante.
'''


letra = input("Ingresa una letra: ")

if letra in ['a', 'e', 'i', 'o', 'u']:
    print("Es una vocal")
else:
    print("Es una consonante")






'''
letra_ingresada =  input("Ingrese una letra: " ) 
vocal = False

if letra_ingresada == "a" or letra_ingresada == "e" or letra_ingresada == "i" :
    vocal = True
    
if  letra_ingresada == "o" or letra_ingresada == "u":
    vocal = True

if vocal:
    print("Es una vocal")
else :
    print("Es una consonante")
     '''