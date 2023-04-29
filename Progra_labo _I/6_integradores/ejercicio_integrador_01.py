
ids = []
nombres = []
edades = []
membresias = []


while True:
    # Mostrar menú de opciones
    print("Menú de opciones:")
    print("1. Agregar un nuevo miembro")
    print("2. Mostrar la informacion de todos los miembros")
    print("3. Actualizar el tipo de membresía de un miembro")
    print("4. Buscar información de un miembro")
    print("5. Calcular el promedio de edad de los miembros")
    print("6. Buscar el miembro más joven y el más viejo")
    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")
    
    # Opción 1: Agregar un nuevo miembro
    if opcion == "1":
        id_nuevo = int(input("Ingrese el número de identificación"
                         " del nuevo miembro: "))

        nombre_nuevo = input("Ingrese el nombre del nuevo miembro: ")
        edad_nuevo = int(input("Ingrese la edad del nuevo miembro: "))
        membresia_opcion = int(input("Ingrese el tipo de membresía: "
                                "1 para (anual) o 2 para (mensual) "))
        
        membresia_nueva = "mensual"
        if membresia_opcion ==1:
            membresia_nueva = "anual"
            
        # Agrego la informacion
        ids.append(id_nuevo)
        nombres.append(nombre_nuevo)
        edades.append(edad_nuevo)
        membresias.append(membresia_nueva)
        print("Miembro agregado exitosamente.")
    
     # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
        print("Número de identificación\tNombre\t\tEdad\tTipo de membresía")
        for i in range(len(ids)):
           print('\t',ids[i], '\t\t\t', nombres[i], '\t',
                 edades[i], '\t\t', membresias[i])
           
    # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        id = int(input("Ingrese el número de identificación : "))
        # Busqueda por id 
        indice_encontrado = -1
        for i in range(len(ids)):
            if ids[i] == id:
                indice_encontrado = i
                break
        
        # si encontro el id actualizo la mebresia
        if indice_encontrado != -1:
            membresia_opcion = int(input("Ingrese el tipo de membresía: "
                                "1 para (anual)o 2 para (mensual) "))
            membresia_nueva = "mensual"
            if membresia_opcion == 1:
                membresia_nueva = "anual"
            membresias[indice_encontrado] = membresia_nueva
            print("La membresía se actualizó correctamente")
        else:
            print("No se encontró el miembro con el número de "
                  "identificación ingresado")
        
        #
        
    
    # Opción 4: Buscar información de un miembro
    elif opcion == "4":
        id = int(input("Ingrese el número de identificación : "))
         # Busqueda por id 
        indice_encontrado = -1
        for i in range(len(ids)):
            if id == ids[i]:
                indice_encontrado = i
                break
        if indice_encontrado !=-1:
            print("\tNombre: {0} \n\tEdad: {1} \n\tMembresia: {2}"
                  .format(nombres[i],edades[i],membresias[i]))
        else :
          print("No se encontró el miembro con el número de "
                  "identificación ingresado")
    # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        
        cantidad_edades = len(edades)
        total_edades = 0
        
        for edad in edades:
            total_edades += edad
        promedio = total_edades / cantidad_edades
        print("El promedio de edades es : {0}".format(promedio))
         
    # Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":
        
        edad_mas_joven = edades[0]
        edad_mas_vieja = edades[0]
        
        for edad in edades:
            if edad < edad_mas_joven:
                edad_mas_joven = edad
            if edad > edad_mas_vieja:
                edad_mas_vieja = edad
                
            print("La edad más joven es:", edad_mas_joven)
            print("La edad más vieja es:", edad_mas_vieja)
    # Opcion 0: Salir
    elif opcion == "0":
        break
    
    else:
        print("Opción inválida. Intente de nuevo.")