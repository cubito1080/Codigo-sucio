from typing import List


def imprimir_sudoku(matriz_sudoku):
    for fila in matriz_sudoku:
        print("|", end="")
        for i in fila:
            if i is None:
                print(" ", end="|")
            else:
                print(i, end="|")
        print()


def validacion(matriz_sudoku, resultado_suma, i, j, numero_actual) -> bool:
    elementos_fila = list(filter(lambda x: x is not None, matriz_sudoku[i]))
    elementos_columna: List[int] = [matriz_sudoku[index][j] for index in range(len(matriz_sudoku))
                                    if matriz_sudoku[index][j] is not None]

    if len(elementos_fila) == len(matriz_sudoku) - 1 or len(elementos_columna) == len(matriz_sudoku) - 1:
        return numero_actual + sum(elementos_fila) == resultado_suma or \
               numero_actual + sum(elementos_columna) == resultado_suma

    return numero_actual + sum(elementos_fila) > resultado_suma or \
           numero_actual + sum(elementos_columna) > resultado_suma


def siguiente_llamado(matriz_sudoku, resultado_suma, i, j):
    if i + 1 < len(matriz_sudoku):
        succes = sudoku_sumas(matriz_sudoku, resultado_suma, i + 1, j)
    else:
        if j + 1 < len(matriz_sudoku):
            succes = sudoku_sumas(matriz_sudoku, resultado_suma, 0, j + 1)
        else:
            succes = True

    return succes


def sudoku_sumas(matriz_sudoku, resultado_suma: int, i: int = 0, j: int = 0):
    succes = False

    if matriz_sudoku[i][j] is not None:
        succes = siguiente_llamado(matriz_sudoku, resultado_suma, i, j)
        return succes

    numero_actual = 1
    while True:
        if validacion(matriz_sudoku, resultado_suma, i, j, numero_actual):
            matriz_sudoku[i][j] = numero_actual
            succes = siguiente_llamado(matriz_sudoku, resultado_suma, i, j)

        if numero_actual >= resultado_suma - 2 or succes:
            break

        numero_actual += 1

    return succes


def resolver_sudoku(matriz_sudoku, resultado_suma):
    succes = sudoku_sumas(matriz_sudoku, resultado_suma)
    if succes:
        return matriz_sudoku
    else:
        return "No tiene solución"


# sudoku = [
#     [5, None, 2],
#     [8, 5, None],
#     [None, 2, None]
# ]
sudoku = [
    [3, 6, 7],
    [None, 7, None],
    [8, None, 5]
]
suma = 16

imprimir_sudoku(sudoku)
print(f"Debe sumar: {suma}")
imprimir_sudoku(resolver_sudoku(sudoku, suma))
