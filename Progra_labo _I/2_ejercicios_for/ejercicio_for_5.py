#Dada una lista de números, imprimir el número más pequeño de la lista.

lista_enteros = [1,2,50,5]
numero_min = 0
flag = False

for numero in lista_enteros:
    
    if (flag == False or numero < numero_min) :
       numero_min = numero
       flag = True
       
print("numero", numero_min)

'''
lista_numeros = [5, 2, 8, 1, 9, 4]

numero_mas_pequeno = min(lista_numeros)

print("El número más pequeño es:", numero_mas_pequeno)
 
'''