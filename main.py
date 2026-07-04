while True:
    print("===GESTOR DE TAREAS===")
    print("1. Ver tarea")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")
    opcion= input("Elige una opcion:")
    if opcion == "1":
        print("Abrinedo tarea...")
    elif opcion == "2":
        print("Agregando tarea...")
    elif opcion == "3":
        print("Eliminando tarea...")
    elif opcion == "4":
        print("Saliendo del sistema...")
        break
    else:
        print("Opcion invalida, intentelo otra ves.")
