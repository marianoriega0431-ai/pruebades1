import csv
import os

def guardar_estudiantes_csv(estudiantes):
    with open("estudiantes.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["ID", "name", "age", "plan", "status"])

        for estudiante in estudiantes:
            escritor.writerow([
                estudiante["ID"],
                estudiante["nombre"],
                estudiante["edad"],
                estudiante["plan"],
                estudiante["estado"]
            ])

def cargar_estudiantes_csv():
    estudiantes = []

    if os.path.exists("estudiantes.csv"):
        with open("estudiantes.csv", "r", newline="", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                estudiante = {
                    "ID": fila["ID"],
                    "nombre": fila["name"],
                    "edad": int(fila["age"]),
                    "plan": fila["plan"],
                    "estado": fila["status"]
                }
                estudiantes.append(estudiante)

    return estudiantes

def crear_estudiante(estudiantes):
    id_estudiante = input("ID: ")
    existe = False

    for estudiante in estudiantes:
        if estudiante["ID"] == id_estudiante:
            existe = True
            break

    if existe:
        print("THIS ID ALREADY EXISTS IN THE DATABASE")
        return

    nombre = input("Name: ")
    edad = int(input("Age: "))
    plan = input("Plan: ")
    estado = input("Status: ")

    estudiante = {
        "ID": id_estudiante,
        "nombre": nombre,
        "edad": edad,
        "plan": plan,
        "estado": estado
    }

    estudiantes.append(estudiante)
    guardar_estudiantes_csv(estudiantes)
    print("STUDENT ADDED SUCCESSFULLY")

def ver_estudiante(estudiantes):
    if len(estudiantes) == 0:
        print("There are no students in the database")
    else:
        print("------ STUDENT LIST -----")
        for estudiante in estudiantes:
            print(f"ID: {estudiante['ID']}")
            print(f"Name: {estudiante['nombre']}")
            print(f"Age: {estudiante['edad']}")
            print(f"Plan: {estudiante['plan']}")
            print(f"Status: {estudiante['estado']}")
            print("--------------------------------")

def buscar_estudiante(estudiantes):
    buscar_id = input("ENTER THE STUDENT ID: ")
    encontrado = False

    for estudiante in estudiantes:
        if estudiante["ID"] == buscar_id:
            print("------ STUDENT FOUND ------")
            print(f"ID: {estudiante['ID']}")
            print(f"Name: {estudiante['nombre']}")
            print(f"Age: {estudiante['edad']}")
            print(f"Plan: {estudiante['plan']}")
            print(f"Status: {estudiante['estado']}")
            print("-----------------------------------")
            encontrado = True
            break

    if not encontrado:
        print("STUDENT NOT FOUND")

def actualizar_estudiante(estudiantes):
    buscar_id = input("ENTER THE STUDENT ID TO UPDATE: ")
    encontrado = False

    for estudiante in estudiantes:
        if estudiante["ID"] == buscar_id:
            print("------- STUDENT FOUND ------")
            print("ENTER THE NEW DATA")

            estudiante["nombre"] = input("UPDATED NAME: ")
            estudiante["edad"] = int(input("UPDATED AGE: "))
            estudiante["plan"] = input("UPDATED PLAN: ")
            estudiante["estado"] = input("STATUS (ACTIVE OR INACTIVE): ")

            guardar_estudiantes_csv(estudiantes)
            print("------ STUDENT UPDATED SUCCESSFULLY ------")
            encontrado = True
            break

    if not encontrado:
        print("STUDENT NOT FOUND")

def eliminar_estudiante(estudiantes):
    buscar_id = input("ENTER THE STUDENT ID YOU WANT TO DELETE: ")
    encontrado = False

    for estudiante in estudiantes:
        if estudiante["ID"] == buscar_id:
            confirmar = input("ARE YOU SURE YOU WANT TO DELETE THIS STUDENT (YES/NO)?: ").lower()

            if confirmar == "yes":
                estudiantes.remove(estudiante)
                guardar_estudiantes_csv(estudiantes)
                print("------ STUDENT DELETED SUCCESSFULLY ------")

            encontrado = True
            break

    if not encontrado:
        print("STUDENT NOT FOUND")

estudiantes = cargar_estudiantes_csv()

while True:
    print("\n------ SCHOOL -------")
    print("1. Create student")
    print("2. List students")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")

    opcion = int(input("Choose the option you want to perform: "))

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
        print("Exiting program...")
        break

    else:
        print("Invalid operation")
