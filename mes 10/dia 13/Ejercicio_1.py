#Siempre que al multiplicar por 2 el resultado sea mayor que sumar 1, se escogerá ese camino siempre y cuando el resultado no se pase de la meta 

def num_min(meta):
  numero = 0
  contador_operaciones = 0

  while numero < meta:
    if numero * 2 > numero + 1 and numero * 2 <= meta:
      numero *=2
    else:
      numero +=1
    contador_operaciones += 1

  return contador_operaciones

print(num_min(11))
