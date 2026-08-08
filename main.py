def cargar_tareas():
    tareas = []
    with open("tareas.txt", "r") as archivo:
        for tarea in archivo:
            tareas.append(tarea.strip())
    return tareas
def guardar_tareas(tareas):
    with open("tareas.txt" , "w") as archivo:
        for tarea in tareas:
            archivo.write(f"{tarea}\n")
def ver_tarea(tareas):
    print("abriendo tareas")
    for tarea in tareas:
        print(f"- {tarea}")
def agregar_tarea(tareas):
    nueva_tarea = input("Ingrese la nueva tarea: ")
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    print(f"Tarea '{nueva_tarea}' agregada.") 
def eliminar_tareas(tareas):
    print("Abriendo lista de tareas")
    eliminando = input("Ingrese la tarea a eliminar: ")
    if eliminando in tareas:
        tareas.remove(eliminando)
        print(f"Tarea '{eliminando}' eliminada.")
    else:
        print(f"Tarea '{eliminando}' no encontrada.")
tareas = cargar_tareas()
while True:
    print("===GESTOR DE TAREAS===")
    print("1. Ver tarea")
    print("2. Agregar tarea")
    print("3. Eliminar tarea")
    print("4. Salir")
    opcion= input("Elige una opcion:")
    if opcion == "1":
        ver_tarea(tareas)    
    elif opcion == "2":
        agregar_tarea(tareas)
    elif opcion == "3":
        eliminar_tareas(tareas)
    elif opcion == "4":
        print("Saliendo del sistema...")
        break
    else:
        print("Opcion invalida, intentelo otra ves.")
print("Gracias por usar el gestor de tareas.")