from typing import List


class Nodo:
    def __init__(self, data: str):
        self.data = data
        self.hijos: List['Nodo'] = []

    def agregar_hijo(self, nodo: 'Nodo') -> None:
        self.hijos.append(nodo)


def generar_cadenas(input: str, index: int, output: str, raiz: Nodo) -> None:
    n = len(input)

    if index == n:
        raiz.agregar_hijo(Nodo(output))
        return

    output += input[index]
    generar_cadenas(input, index + 1, output, raiz)

    output = output[:-1]
    output += " " + input[index]

    generar_cadenas(input, index + 1, output, raiz)


raiz = Nodo("")
generar_cadenas("ABC", 1, "A", raiz)


for hijo in raiz.hijos:
    print(hijo.data)
