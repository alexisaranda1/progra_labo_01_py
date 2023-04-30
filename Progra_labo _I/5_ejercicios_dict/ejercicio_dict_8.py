

#Crea un diccionario que represente las edades de varias 
# personas, donde las claves son los nombres de 
# las personas y los valores son sus edades. 
# Imprime la edad de la persona más joven.


dicionario_personas = {
  "Juan": 25,
  "María": 35,
  "Pedro": 42,
  "Luisa": 18,
  "Carlos": 50
}

clave_minimo = 0

for clave , valor in dicionario_personas.items():
    
    if clave_minimo == 0 or dicionario_personas[
        clave] < dicionario_personas [clave_minimo]:
        
       clave_minimo = clave
       
print("La persona mas joven es: {0} y su edad es {1}"
      .format(clave_minimo, dicionario_personas[clave_minimo]))  
