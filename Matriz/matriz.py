import random

# Crear matriz 5x5 randomizada
matriz = [[random.randint(0,9) for j in range(5)] for i in range(5)]

# Imprimir matriz
print("Matriz:")
for fila in matriz: 
    print(fila)
    
# Buscar secuencias de 4 números consecutivos horizontalmente
for fila in matriz:
    for j in range(len(fila) - 3):
        if fila[j] == fila[j+1] - 1 == fila[j+2] - 2 == fila[j+3] - 3:
            print(f"Secuencia encontrada en la fila {matriz.index(fila)} desde la columna {j} hasta la columna {j+3}")
            

# Buscar secuencias de 4 números consecutivos verticalmente
for j in range(5):
    for i in range(5 - 3):
        if matriz[i][j] == matriz[i+1][j] - 1 == matriz[i+2][j] - 2 == matriz[i+3][j] - 3:
            print(f"Secuencia encontrada en la columna {j} desde la fila {i} hasta la fila {i+3}")
