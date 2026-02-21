# crear una lista de 20 notas
import random
def crear_notas(cantidadNotas):
    notas = []
    for _ in range(cantidadNotas):
        #nota = random.randint(1,5)
        notas.append(random.randint(1,5))
    return notas

print(crear_notas(4))