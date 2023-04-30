
#Crea un diccionario que contenga las capitales de los países
# de América del Sur. Luego, pide al usuario que ingrese el 
# nombre de un país y muestra su capital correspondiente.

dicionario_paises = {
    
    "Argentina" : "Buenos Aires",
    "Bolivia" : "La paz",
    "Brasil" : "Brasilia" ,
    "Chile" : "Santiago" ,
    "Colombia" : "Bogotá" ,
    "Ecuador" : "Quito" ,
    "Guyana" : "Georgetown" ,
    "Paraguay" : "Asunción" ,
    "Perú" : "Lima" ,
    "Surinam" : "Paramaribo" ,
    "Uruguay" : "Montevideo" ,
    "Venezuela": "Caracas" ,
    
}

pais = input("Ingrese un pais: ")

print("la capital de : {0} es {1}".format(pais, dicionario_paises[pais]))