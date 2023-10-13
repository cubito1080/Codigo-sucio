# Accedemos al maximo y minimo de la lista para realizar el producto de estos dos, y el resultado 
# de esta multiplicación se va sumando al total, borrando de la lista el máximo y el mínimo accedido para evitar que se repitan

from typing import List

def suma_minima(arreglo1: List[int], arreglo2: List[int]) -> int:
    suma_total = 0
    while len(arreglo1) > 0:
        max_arreglo1 = max(arreglo1)
        min_arreglo2 = min(arreglo2)

        arreglo1.remove(max_arreglo1)
        arreglo2.remove(min_arreglo2)

        suma_total += min_arreglo2 * max_arreglo1

    return suma_total


A = [6, 1, 9, 5, 4]
B = [3, 4, 8, 2, 4]

print(suma_minima(A, B))
