
miembros = []

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
        id = int(input("Ingrese el número de identificación del "
                       "nuevo miembro: "))
        nombre = input("Ingrese el nombre del nuevo miembro: ")
        edad = int(input("Ingrese la edad del nuevo miembro: "))
        membresia_opcion = int(input("Ingrese el tipo de membresía: "
                                    "1 para (anual) o 2 para (mensual) "))
        membresia = "mensual"
        if membresia_opcion == 1:
            membresia = "anual"
        
        nuevo_miembro = {'id': id, 'nombre': nombre,
                        'edad': edad, 'membresia': membresia}
        miembros.append(nuevo_miembro)
        print("El nuevo miembro ha sido agregado exitosamente.")

    # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
        print("Nro ID.\tNombre\tEdad\tTipo membresia")
        
        for miembro in miembros:
            print("{0}\t {1} \t {2} \t {3}"
            .format(miembro['id'], miembro['nombre'], miembro['edad'],
            miembro['membresia']))
                    
    # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        id = int(input("Ingrese el número de identificación : "))
        # Busqueda por id 
        indice_encontrado = -1
        for i in range(len(miembros)):
            if miembros[i]['id'] == id:
               indice_encontrado = i
               break
        

        if indice_encontrado != -1:
            membresia_opcion = int(input("Ingrese el tipo de membresía: "
                                    "1 para (anual) o 2 para (mensual) "))
            membresia_nueva = "mensual"
            if membresia_opcion == 1:
                membresia_nueva = "anual"
            miembros[indice_encontrado]['membresia'] = membresia_nueva
            print("La membresía del miembro ha sido actualizada exitosamente.")
        
        else:
            print("No se ha encontrado ningún miembro con el número de "
                  "identificación ingresado.")
        
    # Opción 4: Buscar información de un miembro
    elif opcion == "4":
         id = int(input("Ingrese el número de identificación : "))
        # Busqueda por id 
         indice_encontrado = False
         for miembro in miembros:
            if miembros[i]['id'] == id:
                print("Nombre:", miembro['nombre'])
                print("Edad:", miembro['edad'])
                print("Tipo de membresía:", miembro['membresia'])
                indice_encontrado = True
                break
                
         if indice_encontrado != True:
            print("No se ha encontrado ningún miembro con el número de "
                  "identificación ingresado.")
        
    # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        cantidad_edades = len(miembros)
        total_edades = 0
        
        for miembro in miembros:
            total_edades +=  miembro['edad']
            
        promedio = total_edades / cantidad_edades
        print("El promedio de edades es : {0}".format(promedio))
        
    # Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":
                
        edad_mas_joven = miembros[0]['edad']
        edad_mas_vieja =miembros[0]['edad']
        
        for miembro in miembros:
            if  miembro['edad'] < edad_mas_joven:
                edad_mas_joven =  miembro['edad']
            if  miembro['edad'] > edad_mas_vieja:
                edad_mas_vieja =  miembro['edad']
                
        print("La edad más joven es:", edad_mas_joven)
        print("La edad más vieja es:", edad_mas_vieja)

    # Opcion 0: Salir
    elif opcion == "0":
        break
    
    else:
          print("Opción inválida. Intente de nuevo.")
