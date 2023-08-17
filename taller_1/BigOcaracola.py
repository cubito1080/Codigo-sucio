class Matriz: #O(n**2)   Ecuación de la clase: 4O(1) + O(n) + O(n**2)

    def __init__(self, tamano: int): # O(1)
        self.tamano = tamano # O(1)
        self.matriz = [[0] * tamano for _ in range(tamano)] # O(n)

        self.centro = self.tamano // 2 # O(1)
        if self.tamano % 2 == 0: # O(1)
            self.centro -= 1 # O(1)

        self.llenar_matriz() # O(n)

    def llenar_matriz(self): # O(n)
        # Agregar valores a la matriz
        for i in range(self.tamano**2):  # O(n)
            fila = i // self.tamano  # O(n)
            columna = i % self.tamano  # O(n)
            self.agregar_numero(fila, columna, i+1)  # O(n)

    def imprimir_matriz(self): #O(1)
        for i in self.matriz: # O(n)
            print(i) # O(n)

    def agregar_numero(self, fila_objetivo: int, columna_objetivo: int, agregar_elemento: int): # O(1)
        if 0 <= fila_objetivo < self.tamano and 0 <= columna_objetivo < self.tamano: # O(1)
            self.matriz[fila_objetivo][columna_objetivo] = agregar_elemento # O(1)
            return True # O(1)
        else:
            return False # O(1)

    def obtener_tupla_de_direccion(self, contador: int): # O(1)
        codigo = contador % 4 # O(1)

        # La anterior operación puede devolver un número del 0 al 3, cada número representará una dirección
        # Se devuelve una tupla cuyo primer valor representa fila y el segundo columna

        # 0 -> Derecha
        if codigo == 0: # O(1)
            return 0, 1 # O(1)
        # 1 -> Abajo
        elif codigo == 1: # O(1)
            return 1, 0 # O(1)
        # 2 -> Izquierda
        elif codigo == 2: # O(1)
            return 0, -1 # O(1)
        else:
            return -1, 0 # O(1)

    def imprimir_caracola(self): #O(n**2)

        caracola = [] # O(1)

        apuntador_fila = self.centro # O(1)
        apuntador_columna = self.centro # O(1)

        caracola.append(self.matriz[apuntador_fila][apuntador_columna]) # O(1)
        contador = 0 # O(1)

        continua : bool = True # O(1)

        while continua: #O(n)
            cantidad_pasos = (contador // 2) + 1 # O(n)

            if cantidad_pasos == self.tamano: # O(n)
                cantidad_pasos -= 1 # O(n)
                continua = False # O(n)

            movimiento_fila, movimiento_columna = self.obtener_tupla_de_direccion(contador)

            for _ in range(cantidad_pasos): # O(n**2)
                apuntador_fila += movimiento_fila # O(n**2)
                apuntador_columna += movimiento_columna # O(n**2)
                caracola.append(self.matriz[apuntador_fila][apuntador_columna]) # O(n**2)

            contador += 1 # O(n)

        return caracola # O(1)


matriz = Matriz(7) # O(1)

matriz.imprimir_matriz() # O(1)
print("") # O(1)
print(matriz.imprimir_caracola()) # O(1)

# ECUACION  = 4 O(1) + O(n**2)

