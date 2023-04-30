
#Crea un diccionario que represente las notas de un examen
# de varios estudiantes, donde las claves son los nombres de
# los estudiantes y los valores son sus notas.
# Imprime el promedio de las notas.

notas_examenes = {
    "Juan": 8.5,
    "Maria": 9.0,
    "Pedro": 7.2,
    "Ana": 6.5,
    "Luis": 8.9
}

acumulador_notas = 0
cantidad_notas = len(notas_examenes)
for clave in notas_examenes:
    acumulador_notas += notas_examenes[clave]
    
promedio = acumulador_notas / cantidad_notas
print("EL total de las notas es {}".format(acumulador_notas))
print("EL promedio de las notas es {0}".format(promedio))   

    
    
    