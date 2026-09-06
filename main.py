from shared.herramientas import (
    imprimir_titulo, imprimir_exito, imprimir_error, imprimir_info
)
from views import (
    crear_estudiante, obtener_todos, obtener_estudiante, buscar_estudiantes,
    actualizar_estudiante, eliminar_estudiante
)


def mostrar_menu():
    imprimir_titulo("SISTEMA DE GESTIÓN DE ESTUDIANTES")
    print("  1. Crear nuevo estudiante")
    print("  2. Ver todos los estudiantes")
    print("  3. Buscar estudiante")
    print("  4. Ver estudiante por ID")
    print("  5. Actualizar estudiante")
    print("  6. Eliminar estudiante")
    print("  7. Salir")
    imprimir_info("-" * 60)


def opcion_crear():
    imprimir_titulo("CREAR NUEVO ESTUDIANTE")

    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = input("Email: ")
    carnet = input("Carnet: ")

    exito, mensaje = crear_estudiante(nombre, apellido, email, carnet)

    if exito:
        imprimir_exito(mensaje)
    else:
        imprimir_error(mensaje)

    input("\nPresione Enter para continuar...")


def opcion_ver_todos():
    imprimir_titulo("LISTA DE ESTUDIANTES")

    estudiantes = obtener_todos()

    if not estudiantes:
        imprimir_error("No hay estudiantes registrados")
    else:
        print(f"{'ID':<5} {'NOMBRE':<20} {'EMAIL':<25} {'CARNET':<15}")
        print("-" * 65)

        for estudiante in estudiantes:
            print(
                f"{estudiante.id:<5} {estudiante.obtener_nombre_completo():<20} {estudiante.email:<25} {estudiante.carnet:<15}")

        print("-" * 65)
        imprimir_info(f"Total: {len(estudiantes)} estudiante(s)")

    input("\nPresione Enter para continuar...")


def opcion_buscar():
    imprimir_titulo("BUSCAR ESTUDIANTE")

    termino = input("Ingrese nombre, email o carnet: ")
    resultados = buscar_estudiantes(termino)

    if not resultados:
        imprimir_error("No se encontraron estudiantes")
    else:
        imprimir_info(f"Se encontraron {len(resultados)} estudiante(s):\n")

        for estudiante in resultados:
            print(f"ID: {estudiante.id}")
            print(f"  Nombre: {estudiante.obtener_nombre_completo()}")
            print(f"  Email: {estudiante.email}")
            print(f"  Carnet: {estudiante.carnet}\n")

    input("Presione Enter para continuar...")


def opcion_ver_por_id():
    imprimir_titulo("BUSCAR POR ID")

    try:
        id = int(input("Ingrese ID del estudiante: "))
        estudiante = obtener_estudiante(id)

        if not estudiante:
            imprimir_error(f"Estudiante con ID {id} no encontrado")
        else:
            imprimir_info("DATOS DEL ESTUDIANTE:")
            print(f"  ID: {estudiante.id}")
            print(f"  Nombre: {estudiante.obtener_nombre_completo()}")
            print(f"  Email: {estudiante.email}")
            print(f"  Carnet: {estudiante.carnet}")

    except ValueError:
        imprimir_error("El ID debe ser un número")

    input("\nPresione Enter para continuar...")


def opcion_actualizar():
    imprimir_titulo("ACTUALIZAR ESTUDIANTE")

    try:
        id = int(input("Ingrese ID del estudiante: "))
        estudiante = obtener_estudiante(id)

        if not estudiante:
            imprimir_error(f"Estudiante con ID {id} no encontrado")
        else:
            imprimir_info(f"Estudiante actual: {estudiante.obtener_nombre_completo()}")
            print("Deje en blanco para no cambiar\n")

            nombre = input("Nuevo nombre (Enter para omitir): ")
            apellido = input("Nuevo apellido (Enter para omitir): ")
            email = input("Nuevo email (Enter para omitir): ")
            carnet = input("Nuevo carnet (Enter para omitir): ")

            exito, mensaje = actualizar_estudiante(
                id,
                nombre if nombre else None,
                apellido if apellido else None,
                email if email else None,
                carnet if carnet else None
            )

            if exito:
                imprimir_exito(mensaje)
            else:
                imprimir_error(mensaje)

    except ValueError:
        imprimir_error("El ID debe ser un número")

    input("\nPresione Enter para continuar...")


def opcion_eliminar():
    imprimir_titulo("ELIMINAR ESTUDIANTE")

    try:
        id = int(input("Ingrese ID del estudiante: "))
        estudiante = obtener_estudiante(id)

        if not estudiante:
            imprimir_error(f"Estudiante con ID {id} no encontrado")
        else:
            imprimir_info(f"Estudiante a eliminar: {estudiante.obtener_nombre_completo()}")
            confirmar = input("¿Está seguro? (si/no): ")

            if confirmar.lower() == 'si':
                exito, mensaje = eliminar_estudiante(id)
                if exito:
                    imprimir_exito(mensaje)
                else:
                    imprimir_error(mensaje)
            else:
                imprimir_info("Operación cancelada")

    except ValueError:
        imprimir_error("El ID debe ser un número")

    input("\nPresione Enter para continuar...")


def main():
    while True:
        mostrar_menu()

        opcion = input("Seleccione opción: ")

        if opcion == '1':
            opcion_crear()
        elif opcion == '2':
            opcion_ver_todos()
        elif opcion == '3':
            opcion_buscar()
        elif opcion == '4':
            opcion_ver_por_id()
        elif opcion == '5':
            opcion_actualizar()
        elif opcion == '6':
            opcion_eliminar()
        elif opcion == '7':
            imprimir_info("\n¡Hasta luego! 👋\n")
            break
        else:
            imprimir_error("Opción no válida")
            input("Presione Enter para continuar...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        imprimir_error("\n\n¡Programa interrumpido!\n")