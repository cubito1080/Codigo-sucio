# Accedemos al maximo y minimo de la lista para realizar el producto de estos dos, y el resultado 
# de esta multiplicación se va sumando al total, borrando de la lista el máximo y el mínimo accedido para evitar que se repitan

#FORMA 1
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




#FORMA 2
import random


def formula(array_1: list, array_2: list):
    valor = []

    for combinaciones in range(len(array_1)):
        minimo_1, posicion_1 = condiciones_inicial_minimo(array_1)
        maximo_2, posicion_2 = condiciones_iniciales_maximo(array_2)

        operacion_actual = array_1[posicion_1] * array_2[posicion_2]
        valor.append(operacion_actual)

        array_1.pop(posicion_1)
        array_2.pop(posicion_2)

    acumulador = sum(valor)
    print(acumulador)


def condiciones_inicial_minimo(array_1: list):
    minimo = array_1[0]

    for combinaciones in range(len(array_1)):
        if array_1[combinaciones] < minimo:
            minimo = array_1[combinaciones]

    posicion = array_1.index(minimo)

    return minimo, posicion


def condiciones_iniciales_maximo(array_2: list):
    maximo = array_2[0]

    for combinaciones in range(len(array_2)):
        if array_2[combinaciones] > maximo:
            maximo = array_2[combinaciones]

    posicion = array_2.index(maximo)

    return maximo, posicion


array_1 = [6, 1, 9, 5, 4]
array_2 = [3, 4, 8, 2, 4]

formula(array_1, array_2)

