def factorial_dinamico(n, diccionario_memoizacion={}):

#Los factoriales ya calculados se guardan en el diccionario.

    if n == 0 or n == 1: #Caso Base
        return 1

    if n in diccionario_memoizacion:
        return diccionario_memoizacion[n]

    if n > 1:
        factorial = n * factorial_dinamico(n - 1, diccionario_memoizacion)

    diccionario_memoizacion[n] = factorial
    return factorial

n = 3
resultado = factorial_dinamico(n)
print(f"Factorial de {n} es {resultado}")
