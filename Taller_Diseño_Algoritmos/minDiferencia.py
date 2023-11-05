def minDiferencia(N, arr):
    suma_total = sum(arr)
    suma_objetivo = suma_total // 2

    tabla = [[float('inf')] * (suma_objetivo + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        tabla[i][0] = 0

    for i in range(1, N + 1):
        for j in range(1, suma_objetivo + 1):
            if arr[i - 1] <= j:
                tabla[i][j] = min(tabla[i - 1][j], tabla[i - 1][j - arr[i - 1]] + 1)
            else:
                tabla[i][j] = tabla[i - 1][j]

    minima_diferencia = float('inf')
    for j in range(suma_objetivo, -1, -1):
        if tabla[N][j] != float('inf'):
            minima_diferencia = min(minima_diferencia, abs(suma_total - 2 * j))

    return minima_diferencia

print(minDiferencia(4, [1, 6, 11, 5]))
print(minDiferencia(2, [1, 4]))
print(minDiferencia(3, [1, 4, 6]))
print(minDiferencia(3, [4, 3, 5]))
