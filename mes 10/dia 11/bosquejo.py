class Matriz:
    def __init__(self, filas: int, columnas: int):
        if filas == columnas and filas % 2 != 0:
            self.filas = filas
            self.columnas = columnas
            self.lista_columnas = [[0] * columnas for _ in range(filas)]
        else:
            raise ValueError("La matriz debe ser cuadrada e impar")

    def agregar_numero(self, fila_objetivo: int, columna_objetivo: int, agregar_elemento: int):
        if 0 <= fila_objetivo < self.filas and 0 <= columna_objetivo < self.columnas:
            self.lista_columnas[fila_objetivo][columna_objetivo] = agregar_elemento
            return True
        else:
            return False

    def calcular_centro(self):
        centro_fila = self.filas // 2
        centro_columna = self.columnas // 2
        return centro_fila, centro_columna

    def calcular_rataciones_espirales(self):
        return self.filas // 2


    def girar_derecha(self, centro: list, numero_capa):
        centro = [self.filas][self.columnas + 1]

    def girar_izquierda(self, centro: list, numero_capa):
        centro = [self.filas][self.columnas - 1]

    def girar_arriba(self, centro: list, numero_capa):
        centro = [self.filas - 1][self.columnas]

    def girar_abajo(self, centro: list, numero):
        centro = [self.filas + 1][self.columnas]



    def imprimir_espiral(self):
        rotaciones = self.calcular_rataciones_espirales()
        centro_fila, centro_columna = self.calcular_centro()

        for _ in range(rotaciones):
            # Imprimir hacia la derecha
            for col in range(centro_columna, self.columnas - centro_columna):
                print(self.lista_columnas[centro_fila][col])

            # Imprimir hacia abajo
            for row in range(centro_fila + 1, self.filas - centro_fila):
                print(self.lista_columnas[row][self.columnas - centro_columna - 1])

            # Imprimir hacia la izquierda
            for col in range(self.columnas - centro_columna - 2, centro_columna - 1, -1):
                print(self.lista_columnas[self.filas - centro_fila - 1][col])

            # Imprimir hacia arriba
            for row in range(self.filas - centro_fila - 2, centro_fila, -1):
                print(self.lista_columnas[row][centro_columna])

            centro_fila += 1
            centro_columna += 1

# Crear una matriz cuadrada impar de 5x5
matriz = Matriz(5, 5)

# Agregar valores a la matriz
for i in range(1, 26):
    fila = (i - 1) // 5
    columna = (i - 1) % 5
    matriz.agregar_numero(fila, columna, i)

# Imprimir la espiral
matriz.imprimir_espiral()
