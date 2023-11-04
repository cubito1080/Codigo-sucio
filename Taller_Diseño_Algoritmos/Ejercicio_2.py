import random

"""
Le calculamos el Big O debido a que el ejercicio debe tener una complejidad específica,
la cual es O(N*N) = O(N**2).
"""

"""
De programación dinámica, en este algoritmo aplicamos la memoización, este método,
se utiliza para almacenar los resultados intermedios de subproblemas que han sido resueltos.
En este caso, la variable matriz_memoizacion es una lista de listas o para entenderlos mejor
una matriz NxN llena de ceros que se utiliza para almacenar la suma máxima posible 
desde cada celda en la matriz principal.
"""

def sumaCaminoMaximo(N, Matriz): 
    
    # Creamos una matriz llena de ceros para almacenar la suma maxima en cada
    # celda, es decir, Una "celda" se refiere a un elemento individual dentro de una matriz
    #lo podriamos entender como cada numero que se encuentra en la matriz

    matriz_memoizacion = [[0] * N for _ in range(N)] # O(N**2)

    # Inicializamos la primera fila de la matriz_memoizacion con los valores de la primera fila de la matriz original.
    for i in range(N): # O(N)
        matriz_memoizacion[0][i] = Matriz[0][i]

    # Llenamos la matriz_memoizacion con las filas que faltan.
    for i in range(1, N): 
        for j in range(N):
            # Determinamos los movimientos posibles.         
            movimiento_superior = matriz_memoizacion[i - 1][j] # O(1) 

            if j > 0:
                movimiento_izquierda = matriz_memoizacion[i - 1][j - 1] # O(1) 
            else:
                movimiento_izquierda = 0 # O(1)

            if j < N - 1:
                movimiento_derecha = matriz_memoizacion[i - 1][j + 1]  # O(1) 
            else:
                movimiento_derecha = 0 # O(1)

            # Determinamos el movimiento con la suma máxima.
            maximo_movimiento = max(movimiento_superior, movimiento_izquierda, movimiento_derecha) # O(1)
            matriz_memoizacion[i][j] = maximo_movimiento + Matriz[i][j] # O(1)

    # Encontramos el máximo en la última fila de la matriz_memoizacion.
    maximo_suma_camino = max(matriz_memoizacion[-1]) # O(N)

    return maximo_suma_camino # O(N**2)

#En caso de querer probar con otro valor de N, documentar las Matriz_2 y Matriz_3, esto fue para probar el con las matrices dadas en el ejercicio
# pero para usar otro valor de N, podemos utilizar la Matriz_1 unicamente 

N = 2
Matriz_1 = [[random.randint(1, 1001) for _ in range(N)] for _ in range(N)]
Matriz_2 = [[348, 391],
           [618, 193]] 
Matriz_3 = [[2, 2],
           [2, 2]]           

print("Pruebas")

print(f"Matriz 1 {Matriz_1}")  
camino_maximo_prueba_1 = sumaCaminoMaximo(N, Matriz_1)  
print(f"Suma maxima: {camino_maximo_prueba_1}")

print(f"Matriz 2 {Matriz_2}") 
camino_maximo_prueba_2 = sumaCaminoMaximo(N, Matriz_2)
print(camino_maximo_prueba_2)

print(f"Matriz 3 {Matriz_3}") 
camino_maximo_prueba_3 = sumaCaminoMaximo(N, Matriz_3)
print(camino_maximo_prueba_3 )
