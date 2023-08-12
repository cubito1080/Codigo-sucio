def calcular_longitud(longitud: str, contador: int = 0, vacio = ""):

    if not longitud:
        print(vacio)
        return vacio

    else:
        contador += 1
        #print(longitud[-1])
        vacio = vacio + longitud[-1]
        return calcular_longitud(longitud[:-1], contador, vacio)



(calcular_longitud("juan david"))
