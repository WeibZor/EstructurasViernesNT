def crear_lista_estudiantes(cantidadEstudiantes):
    estudiantes = []
    for i in range(cantidadEstudiantes):
        estudiante = {}
        estudiante ["id"] = input("id: ")
        estudiante ["nombres"] = input("nombres: ")
        estudiante ["documento"] = input("documentos: ")
        estudiante ["correo"] = input("correo: ")
        estudiante ["telefono"] = input("telefono: ")
        estudiante ["promedio"] = input("promedio: ")
        estudiante ["semestre"] = input("semestre: ")
        estudiante ["esBecado"] = input("Tienes beca?: ")
        estudiantes.append(estudiante)
    return estudiantes

# Invocar la función

resultado_lista = crear_lista_estudiantes(2)

print(resultado_lista)