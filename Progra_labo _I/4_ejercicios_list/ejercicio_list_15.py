#Crea una lista de números enteros y
# luego encuentra la suma de los números en índices impares.

lista_numeros =[0,1,2,3,4,5,6,11,8,9 ]


acumalador = 0

for i in range(len(lista_numeros)):
    
    if i %2 != 0:
        acumalador += lista_numeros[i]
        
        
        
print("la suma de los numeros en el indice impar: {0}".format(acumalador))