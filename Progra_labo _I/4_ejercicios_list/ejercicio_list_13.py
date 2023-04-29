#Crea una lista de números y encuentra el promedio de 
# todos los números en la lista.
lista_numeros = [7,8,9,6,4,5]
suma = 0
contador = 0
for i in lista_numeros:
    suma += i
    contador += 1
    print("la suma es : {0}, y la cantidad es : {1}".format(suma,contador))   
promedio = suma / contador
print("el promedio es : {0}".format(promedio))