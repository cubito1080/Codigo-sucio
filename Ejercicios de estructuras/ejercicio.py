def calcular_longitud(longitud: str, contador: int = 0):

    if not longitud:
        return

    else:
        contador += 1
        print(longitud[-1])
        return calcular_longitud(longitud[:-1], contador)



calcular_longitud("HOLA")
