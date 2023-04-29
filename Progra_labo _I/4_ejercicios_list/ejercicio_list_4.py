#Crea una lista vacía y pide al usuario que ingrese una palabra. 
# Luego, muestra la primera letra de la palabra. 
# Repite este proceso 
# hasta que el usuario ingrese una palabra que comience con la letra "z".


lista = []

salida = " "
i = 0
while salida != "z":
    palabra_ingresada = input("ingrese una palabra : ")
    
    if len(palabra_ingresada) > 0 :
        salida = palabra_ingresada[0]
        if salida != "z":
            print("La primera letra de la pablara es : {0}".format(salida))
            lista.append(palabra_ingresada)
  
   

