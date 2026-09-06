
from models import Estudiante
from shared.json_manager import GestorJSON

# Crear un gestor para el archivo de estudiantes
gestor = GestorJSON('data/estudiantes.json')


# ===== CREATE (Crear) =====

def crear_estudiante(nombre, apellido, email, carnet):
    try:
        estudiantes_data = gestor.leer()

        if estudiantes_data:
            siguiente_id = max(c['id'] for c in estudiantes_data) + 1
        else:
            siguiente_id = 1

        # Uso de la clase Estudiante (con E mayúscula y 5 atributos)
        estudiante = Estudiante(siguiente_id, nombre, apellido, email, carnet)

        datos_estudiante = estudiante.a_diccionario()
        estudiantes_data.append(datos_estudiante)
        gestor.guardar(estudiantes_data)

        return True, f"Estudiante {estudiante.obtener_nombre_completo()} creado"

    except Exception as e:
        return False, f"Error: {str(e)}"


# ===== READ (Leer) =====

def obtener_todos():
    datos = gestor.leer()
    estudiantes = []

    for dato in datos:
        estudiante = Estudiante(
            dato['id'],
            dato['nombre'],
            dato['apellido'],
            dato['email'],
            dato['carnet']
        )
        # Se asignan las notas guardadas
        estudiante.notas = dato.get('notas', {})
        estudiantes.append(estudiante)

    return estudiantes


def obtener_estudiante(id):
    estudiantes = obtener_todos()
    for estudiante in estudiantes:
        if estudiante.id == id:
            return estudiante
    return None


def buscar_estudiantes(termino):
    estudiantes = obtener_todos()
    resultados = []
    termino = termino.lower()

    for estudiante in estudiantes:
        if (termino in estudiante.nombre.lower() or
                termino in estudiante.apellido.lower() or
                termino in estudiante.email.lower() or
                termino in estudiante.carnet.lower()):
            resultados.append(estudiante)

    return resultados


# ===== NOTAS =====

def agregar_nota(id, materia, nota):
    estudiante = obtener_estudiante(id)
    if not estudiante:
        return False, f"Estudiante con ID {id} no encontrado"

    estudiante.agregar_nota(materia, nota)

    estudiantes_data = gestor.leer()
    for i, dato in enumerate(estudiantes_data):
        if dato['id'] == id:
            estudiantes_data[i] = estudiante.a_diccionario()
            break

    gestor.guardar(estudiantes_data)
    return True, f"Nota {nota} agregada a {materia} para {estudiante.obtener_nombre_completo()}"


# ===== UPDATE (Actualizar) =====

def actualizar_estudiante(id, nombre=None, apellido=None, email=None, carnet=None):
    estudiante = obtener_estudiante(id)

    if not estudiante:
        return False, f"Estudiante con ID {id} no encontrado"

    if nombre:
        estudiante.nombre = nombre
    if apellido:
        estudiante.apellido = apellido
    if email:
        estudiante.email = email
    if carnet:
        estudiante.carnet = carnet

    estudiantes_data = gestor.leer()
    for i, dato in enumerate(estudiantes_data):
        if dato['id'] == id:
            estudiantes_data[i] = estudiante.a_diccionario()
            break

    gestor.guardar(estudiantes_data)
    return True, f"Estudiante {estudiante.obtener_nombre_completo()} actualizado"


# ===== DELETE (Eliminar) =====

def eliminar_estudiante(id):
    estudiante = obtener_estudiante(id)

    if not estudiante:
        return False, f"Estudiante con ID {id} no encontrado"

    estudiantes_data = gestor.leer()
    estudiantes_data = [c for c in estudiantes_data if c['id'] != id]

    gestor.guardar(estudiantes_data)
    return True, f"Estudiante {estudiante.obtener_nombre_completo()} eliminado"