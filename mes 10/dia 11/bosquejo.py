import math


class Matriz:
    def __init__(self, filas: int, columnas: int):
        if filas == columnas and filas % 2 != 0:
            self.filas = filas
            self.columnas = columnas
            self.lista_columnas = [[0] * columnas for _ in range(filas)]
        else:
            raise ValueError("La matriz debe ser cuadrada e impar")


        self.cuantas_derecha = math.ceil(self.filas/2)

        self.cuantas_arriba = math.floor(self.filas/2)
        self.cuantas_izquierda = math.floor(self.filas / 2)
        self.cuantas_izquierda = math.floor(self.filas / 2)


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

    def calcular_rotaciones_espirales(self):
        return self.filas // 2

    def girar_derecha(self, centro: list, numero_capa):
        centro = [self.filas][self.columnas + 1]

    def girar_izquierda(self, centro: list, numero_capa):
        centro = [self.filas][self.columnas - 1]

    def girar_arriba(self, centro: list, numero_capa):
        centro = [self.filas - 1][self.columnas]

    def girar_abajo(self, centro: list, numero):
        centro = [self.filas + 1][self.columnas]

    def hallar_serie_izquierda_y_arriba(self):
        serie_izquierda_y_arriba = []
        contador = 2

        for _ in range(self.filas - 1):
            serie_izquierda_y_arriba.append(contador)
            contador += 2

        return serie_izquierda_y_arriba


    def hallar_serie_derecha_abajo(self):
        serie_derecha_abajo = []
        contador = 1

        for _ in range(self.filas - 1):
            serie_derecha_abajo.append(contador)
            contador += 2

        return serie_derecha_abajo



# Crear una matriz cuadrada impar de 5x5
matriz = Matriz(5, 5)

# Agregar valores a la matriz
for i in range(1, 26):
    fila = (i - 1) // 5
    columna = (i - 1) % 5
    matriz.agregar_numero(fila, columna, i)

# Imprimir la espiral
matriz.imprimir_espiral()
