import math


class Matriz:
    def __init__(self, filas: int, columnas: int):
        if filas == columnas and filas % 2 != 0:
            self.filas = filas
            self.columnas = columnas
            self.lista_columnas = [[0] * columnas for _ in range(filas)]
        else:
            raise ValueError("La matriz debe ser cuadrada e impar")

        # revisar miro
        self.cuantas_derecha = math.ceil(self.filas / 2)

        # revisar miro , patron matematico
        self.cuantas_arriba = math.floor(self.filas / 2)
        self.cuantas_abajo = math.floor(self.filas / 2)
        self.cuantas_izquierda = math.floor(self.filas / 2)

        self.almacenar_impresion = []

        self.saltos_derecha = len(self.lista_columnas) - 1

    def agregar_numero(self, fila_objetivo: int, columna_objetivo: int, agregar_elemento: int):
        if 0 <= fila_objetivo < self.filas and 0 <= columna_objetivo < self.columnas:
            self.lista_columnas[fila_objetivo][columna_objetivo] = agregar_elemento
            return True
        else:
            return False

    def calcular_centro_fila(self):
        centro_fila = math.floor(self.filas / 2)
        return centro_fila

    def calcular_centro_columna(self):
        centro_columna = math.floor(self.filas / 2)
        return centro_columna

    """def calcular_rotaciones_espirales(self):
        return self.filas // 2"""

    def hallar_serie_izquierda_y_arriba(self):
        serie_izquierda_y_arriba = []
        contador = 2

        for _ in range(self.cuantas_izquierda):
            serie_izquierda_y_arriba.append(contador)
            contador += 2

        return serie_izquierda_y_arriba

    def hallar_serie_derecha(self):
        serie_derecha = []
        contador = 1

        for _ in range(self.cuantas_derecha-1):
            serie_derecha.append(contador)
            contador += 2

        serie_derecha.append(self.saltos_derecha)

        return serie_derecha

    def hallar_serie_abajo(self):
        serie_abajo = []
        contador = 1

        for _ in range(self.cuantas_abajo):
            serie_abajo.append(contador)
            contador += 2

        return serie_abajo

    def imprimir_caracola(self):

        # calcular centro incial

        centro_fila = self.calcular_centro_fila()
        centro_columna = self.calcular_centro_columna()

        # hallar series

        serie_derecha: list = self.hallar_serie_derecha()  # 7
        serie_abajo: list = self.hallar_serie_abajo()  # 6

        serie_izquierda: list = self.hallar_serie_izquierda_y_arriba()
        serie_arriba: list = self.hallar_serie_izquierda_y_arriba()

        # patron de impresion
        # primero derecha
        # segundo abajo
        # tercero izquierda
        # cuarto arriba

        # repetir

        while self.cuantas_derecha > 0:


            if self.cuantas_derecha == 0:
                for girar_derechas in range(serie_derecha[0]):  # 1 3 5 7 9 11 12 para una matriz 13 x 13
                    self.almacenar_impresion.append(self.lista_columnas[centro_fila][centro_columna + 1])
                    centro_columna = centro_columna + 1

                return self.imprimir_caracola()

            # hacer derecha primero
            for girar_derechas in range(serie_derecha[0]): # 1 3 5 7 9 11 12 para una matriz 13 x 13
                self.almacenar_impresion.append(self.lista_columnas[centro_fila][centro_columna + 1])
                centro_columna = centro_columna + 1

            serie_derecha.pop(0)

            self.cuantas_derecha = self.cuantas_derecha - 1

            # luego hacer abajos
            for girar_abajos in range(serie_abajo[0]): # 1 3 5 7 9 11
                self.almacenar_impresion.append(self.lista_columnas[centro_fila + 1][centro_columna])
                centro_fila = centro_fila + 1

            serie_abajo.pop(0)

            # luego hacer izquierda
            for girar_izquierda in range(serie_izquierda[0]): # 2 4 6 8 10 12
                self.almacenar_impresion.append(self.lista_columnas[centro_fila][centro_columna - 1])
                centro_columna = centro_columna - 1

            serie_izquierda.pop(0)

            # finalmente girar arribas
            for girar_arribas in range(serie_arriba[0]): # 2 4 6 8 10 12
                self.almacenar_impresion.append(self.lista_columnas[centro_fila - 1][centro_columna])
                centro_fila = centro_fila - 1

            serie_arriba.pop(0)


# Crear una instancia de la clase Matriz
matriz = Matriz(5, 5)
contador = 1
for i in range(5):
    for j in range(5):
        matriz.agregar_numero(i, j, contador)
        contador += 1

# Imprimir la matriz original
print("Matriz original:")
for fila in matriz.lista_columnas:
    print(fila)

# Imprimir la matriz en forma de caracola
print("Matriz en forma de caracola:")
print(matriz.imprimir_caracola())
