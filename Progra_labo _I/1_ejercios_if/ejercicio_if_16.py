''''
Escribir un programa que le pida al usuario que ingrese su nombre y su edad,
y luego imprima "Eres adolescente" si la edad está entre 13 y 17 inclusive, 
"Eres adulto" si la edad está entre 18 y 64 inclusive, o "Eres adulto mayor" 
si la edad es mayor o igual a 65.
'''

nombre_ingresado =  input(" Ingrese su nombre: " ) 
edad_ingresada = int (input(" Ingrese su edad: ") )

if edad_ingresada < 12 :
    print("Eres un niño")
elif edad_ingresada >=13 and edad_ingresada <=17:
    print("Eres adolescente")
elif edad_ingresada >=18 and edad_ingresada <=64:
     print("Eres adulto")
elif edad_ingresada > 65:
      print("Eres adulto mayor")
    