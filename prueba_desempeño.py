import csv
import os
def guardar_estudiantes_csv(estudiantes):
    with open ("estudiantes.csv", "w", newline= "", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["ID", "nombre", "edad", "plan", "estado"])

        for estudiante in estudiantes:
            escritor.writerow([
                estudiante["ID"],
                estudiante["nombre"],
                estudiante["edad"],
                estudiante["plan"],
                estudiante["estado"]
            ])
def cargar_estudiantes_csv():
    estudiante =[]
    if os.path.exists("estudiantes.csv"):
        with open("estudiantes.csv", "r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                estudiante = {
                    "ID": fila ["ID"],
                    "nombre": fila ["nombre"],
                    "edad": int(fila ["edad"]),
                    "plan": fila ["plan"],
                    "estado": fila ["estado"]
                }
                estudiante.append(estudiante)

    return estudiante


def crear_estudiante(estudiantes):
        id_estudiante = input("ID: ")
        existe = False
        for estudiante in estudiantes:
            if estudiante ["ID"] == id_estudiante:
                existe = True
                break
        if existe:
                print("ESE ID YA EXISTE EN LA BASE DE DATOS")
                return
        nombre = input("nombre: ")
        edad = int(input("edad: "))
        plan = input("plan: ")
        estado = input("estado: ")

        estudiante ={
            "ID": id_estudiante,
            "nombre": nombre,
            "edad": edad,
            "plan": plan,
            "estado": estado
        }
        estudiantes.append(estudiante)
        guardar_estudiantes_csv(estudiantes)
        print("ESTUDIANTE AGREGADO CON EXITO")
def ver_estudiante(estudiantes):
    if len (estudiantes) == 0:
        print("No hay estudiantes en la base de datos")
    else:
        print("------LISTA DE ESTUDIANTES -----")
        for estudiante in estudiantes:
                print(f"ID: {estudiante['ID']}")
                print(f"nombre: {estudiante['nombre']}")
                print(f"edad: {estudiante['edad']}")
                print(f"plan: {estudiante['plan']}")
                print(f"estado: {estudiante['estado']}")
        print("--------------------------------")
def buscar_estudiante(estudiantes):
        buscar_id= input("INGRESA EL ID DEL ESTUDIANTE: ")
        encontrado = False
        for estudiante in estudiantes:
            if estudiante ["ID"] == buscar_id:
                print("------ ESTUDIANTE ENCONTRADO ------")
                print(f"ID: {estudiante['ID']}")
                print(f"nombre: {estudiante['nombre']}")
                print(f"edad: {estudiante['edad']}")
                print(f"plan: {estudiante['plan']}")
                print(f"estado: {estudiante['estado']}")
                print("-----------------------------------")

                encontrado = True
                break
        if not encontrado:
            print("ESTUDIANTE NO ENCONTRADO")
def actualizar_estudiante(estudiantes):
        buscar_id= input("INGRESA EL ID DEL ESTUDIANTE A ACTUALIZAR: ")
        encontrado = False
        for estudiante in estudiantes:
            if estudiante ["ID"] == buscar_id:
                print("------- ESTUDIANTE ENCONTRADO ------")
                print("INGRESA LOS NUEVOS DATOS ")
                estudiante["nombre"] = input ("NOMBRE ACTUALIZADO: ")
                estudiante["edad"] = int(input("EDAD ACTUALIZADA: "))
                estudiante["plan"] = input ("PLAN ACTUALIZADO: ")
                estudiante["estado"] = input ("ESTADO (ACTIVO O INACTIVO): ")
                guardar_estudiantes_csv(estudiantes)
                print ("------ ESTUDIANTE ACTUALIZADO CORRECTAMENTE ------")
                encontrado = True
                break
        if not encontrado:
            print("ESTUDIANTE NO ENCONTRADO")
def eliminar_estudiante(estudiantes):
        buscar_id= input ("INGRESA EL ID DEL estudiante QUE DESEA ELIMINAR: ")
        encontrado = False
        for estudiante in estudiantes:
            if estudiante["ID"] == buscar_id:
                confirmar= input("¿SEGURO QUE DESEA ELIMINAR ESTE estudiante (SI/NO)?: ").lower()
                if confirmar == "si":
                    estudiantes.remove(estudiante)
                    guardar_estudiantes_csv(estudiantes)
                    print("------ estudiante ELIMINADO CORRECTAMENTE ------")

                    encontrado = True
                    break
        if not encontrado:
            print("estudiante NO ENCONTRADO")
estudiantes= cargar_estudiantes_csv()
while True:
    print("------ SCHOOL -------")

    print("1. crear estudiante")
    print("2. listar estudiantes")
    print("3. buscar estudiante")
    print("4. actualizar estudiante")
    print("5. eliminar estudiante")
    print("6. salir")

    opcion= int(input("elige la opcion que deseas realizar: "))

    if opcion == 1:
            crear_estudiante(estudiantes)


    elif opcion == 2:
            ver_estudiante(estudiantes)

    elif opcion == 3:
            buscar_estudiante(estudiantes)

    elif opcion == 4:
            actualizar_estudiante(estudiantes)


    elif opcion == 5:
            eliminar_estudiante(estudiantes)


    elif opcion == 6:
        break

    else:
        print("operacion no valida")