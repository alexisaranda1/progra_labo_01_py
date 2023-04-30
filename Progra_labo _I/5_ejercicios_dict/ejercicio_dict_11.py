

#Crea un diccionario que represente una lista de tareas por hacer.
# Cada clave del diccionario debe ser el nombre de una tarea y 
# cada valor debe ser su estado
# (los estados son:  pendiente, en proceso, completada). 
# Imprimir todas las tareas seguido de su estado

dic_tareas = {
    "Comprar leche": "pendiente",
    "Ir al gimnasio": "en proceso",
    "Preparar la cena": "completada",
    "Llamar al banco": "pendiente",
    "Limpiar el baño": "en proceso"
}


for clave, valor in dic_tareas.items():
    print("Tarea : {0}, estado : {1}".format(clave,valor))