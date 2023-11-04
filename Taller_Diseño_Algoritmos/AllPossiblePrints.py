from typing import List


def generar_cadenas(input: str, index: int, output: str) -> None:
    n = len(input)

    if index == n:
        print(output)
        return

    output += input[index]
    generar_cadenas(input, index + 1, output)

    output = output[:-1]
    output += " " + input[index]

    generar_cadenas(input, index + 1, output)



generar_cadenas("AB c", 1, "A")
