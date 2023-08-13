
def hallar_serie_derecha(cuantas_derecha):
    serie_derecha = []
    contador = 1

    for _ in range(cuantas_derecha-1):
        serie_derecha.append(contador)
        contador += 2

    serie_derecha.append(4)

    return serie_derecha


print(hallar_serie_derecha(3))