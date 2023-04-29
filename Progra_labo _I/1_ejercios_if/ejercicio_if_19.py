'''
Escribir un programa que le pida al usuario que ingrese su edad,
y luego imprima "Eres mayor de edad" si la edad es mayor o igual a 18,
"Eres adolescente" si la edad está entre 13 y 17 inclusive, 
o "Eres menor de edad"si la edad es menor que 13.

'''

edad_ingresada = int (input(" Ingrese su edad: ") )

if edad_ingresada >=18 and edad_ingresada <=64:
     print("Eres mayor de edad")
     
elif edad_ingresada >=13 and edad_ingresada <=17:
    print("Eres adolescente")
    
if edad_ingresada < 13 :
    print("Eres menor de edad")
