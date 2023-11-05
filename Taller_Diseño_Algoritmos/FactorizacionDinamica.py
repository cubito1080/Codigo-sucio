def factorizacion_dinamica(numero):
  divisores = [0] * (numero + 1)
  divisores[1] = 1

  for i in range(2, numero + 1):
    if divisores[i] == 0:
      divisores[i] = i
      for j in range(i * 2, numero + 1, i):
        if divisores[j] == 0:
          divisores[j] = i

  factores_primos = []
  while numero != 1:
    factores_primos.append(divisores[numero])
    numero //= divisores[numero]

  return factores_primos

numero = int(input("Introduce un número para factorizar: "))
factores_primos = factorizacion_dinamica(numero)
print(f"Los factores primos de {numero} son: {factores_primos}")
