import math


class Matriz: # O(1)
    def __init__(self, tamano: int): # O(1)

        if tamano % 2 != 0: # O(1)
            self.tamano = tamano # O(1)
            self.lista_tamano = [[0] * tamano for _ in range(tamano)] # O(n)
        else:
            raise ValueError("La matriz debe ser cuadrada e impar") # O(1)

        # revisar miro
        self.cuantas_derecha = math.ceil(self.tamano / 2) # O(1)

        # revisar miro , patron matematico
        self.cuantas_arriba = math.floor(self.tamano / 2) # O(1)
        self.cuantas_abajo = math.floor(self.tamano / 2) # O(1)
        self.cuantas_izquierda = math.floor(self.tamano / 2) # O(1)

        self.almacenar_impresion = [] # O(1)

        self.saltos_derecha = len(self.lista_tamano) - 1 # O(1)

        self.llenar_matriz()

    def llenar_matriz(self):
        # Agregar valores a la matriz
        for i in range(1, (self.tamano**2) + 1):  # O(n)
            fila = (i - 1) // self.tamano  # O(n)
            columna = (i - 1) % self.tamano  # O(n)
            self.agregar_numero(fila, columna, i)  # O(n)

    def imprimir_matriz(self):
        for i in  self.lista_tamano:
            print(i)


    def agregar_numero(self, fila_objetivo: int, columna_objetivo: int, agregar_elemento: int): # O(1)
        if 0 <= fila_objetivo < self.tamano and 0 <= columna_objetivo < self.tamano: # O(1)
            self.lista_tamano[fila_objetivo][columna_objetivo] = agregar_elemento # O(1)
            return True # O(1)
        else:
            return False # O(1)

    def calcular_centro_fila(self): # O(1)
        centro_fila = math.floor(self.tamano / 2) # O(1)
        return centro_fila # O(1)

    def calcular_centro_columna(self): # O(1)
        centro_columna = math.floor(self.tamano / 2) # O(1)
        return centro_columna # O(1)

    def hallar_serie_izquierda_y_arriba(self): # O(n)
        serie_izquierda_y_arriba = [] # O(1)
        contador = 2 # O(1)

        for _ in range(self.cuantas_izquierda): # O(n)
            serie_izquierda_y_arriba.append(contador) # O(n)
            contador += 2 # O(n)

        return serie_izquierda_y_arriba # O(1)

    def hallar_serie_derecha(self): # O(n)
        serie_derecha = [] # O(1)
        contador = 1 # O(1)

        for _ in range(self.cuantas_derecha - 1): # O(n)
            serie_derecha.append(contador) # O(n)
            contador += 2 # O(n)

        serie_derecha.append(self.saltos_derecha) # O(1)

        return serie_derecha # O(1)

    def hallar_serie_abajo(self): # O(n)
        serie_abajo = [] # O(1)
        contador = 1 # O(1)

        for _ in range(self.cuantas_abajo): # O(n)
            serie_abajo.append(contador) # O(n)
            contador += 2 # O(n)

        return serie_abajo # O(1)

    def imprimir_caracola(self):

        # calcular centro incial

        centro_fila = self.calcular_centro_fila() # O(1)
        centro_columna = self.calcular_centro_columna() # O(1)


        self.almacenar_impresion.append(self.lista_tamano[centro_fila][centro_columna]) # O(1)

        # hallar series

        serie_derecha: list = self.hallar_serie_derecha() # O(1)
        serie_abajo: list = self.hallar_serie_abajo() # O(1)

        serie_izquierda: list = self.hallar_serie_izquierda_y_arriba() # O(1)
        serie_arriba: list = self.hallar_serie_izquierda_y_arriba() # O(1)

        # patron de impresion
        # primero derecha
        # segundo abajo
        # tercero izquierda
        # cuarto arriba

        # repetir

        while self.cuantas_derecha > 0:

            if self.cuantas_derecha == 1:
                for girar_derechas in range(serie_derecha[0]):
                    self.almacenar_impresion.append(self.lista_tamano[centro_fila][centro_columna + 1])
                    centro_columna = centro_columna + 1

                return self.almacenar_impresion

            # hacer derecha primero
            for girar_derechas in range(serie_derecha[0]):
                self.almacenar_impresion.append(self.lista_tamano[centro_fila][centro_columna + 1])
                centro_columna = centro_columna + 1

            serie_derecha.pop(0)

            self.cuantas_derecha = self.cuantas_derecha - 1

            # luego hacer abajos
            for girar_abajos in range(serie_abajo[0]):
                self.almacenar_impresion.append(self.lista_tamano[centro_fila + 1][centro_columna])
                centro_fila = centro_fila + 1

            serie_abajo.pop(0)

            # luego hacer izquierda
            for girar_izquierda in range(serie_izquierda[0]):
                self.almacenar_impresion.append(self.lista_tamano[centro_fila][centro_columna - 1])
                centro_columna = centro_columna - 1

            serie_izquierda.pop(0)

            # finalmente girar arribas
            for girar_arribas in range(serie_arriba[0]):
                self.almacenar_impresion.append(self.lista_tamano[centro_fila - 1][centro_columna])
                centro_fila = centro_fila - 1

            serie_arriba.pop(0)

matriz = Matriz(7) # O(1)

matriz.imprimir_matriz() # O(1)
print("")
print(matriz.imprimir_caracola()) # O(1)
