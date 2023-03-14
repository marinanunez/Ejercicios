import random

def generar_lista_edades():
    lista = []
    for i in range(10):
        edad = random.randint(1, 100)
        diccionario = {'id': i+1, 'edad': edad}
        lista.append(diccionario)
    return lista

def ordenar_lista_edades(lista):
    lista_ordenada = sorted(lista, key=lambda x: x['edad'], reverse=True)
    id_persona_mas_joven = lista[-1]['id']
    id_persona_mas_vieja = lista[0]['id']
    print(f"La persona mas joven tiene el id {id_persona_mas_joven}")
    print(f"La persona mas vieja tiene el id {id_persona_mas_vieja}")
    return lista_ordenada

lista_edades = generar_lista_edades()
lista_ordenada = ordenar_lista_edades(lista_edades)
print(lista_ordenada)