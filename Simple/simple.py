import random

def generar_lista_edades():
    lista = []
    for i in range(10):
        edad = random.randint(1, 100)
        diccionario = {'id': i+1, 'edad': edad}
        lista.append(diccionario)
    return lista

lista_edades = generar_lista_edades()
print(lista_edades)