def bubble_sort(arr):
    n = len(arr) #0(1)
    for i in range(n): #O(n)
        for j in range(0, n-i-1): #O(n2)
            if arr[j] > arr[j+1]: #o(n2)
                arr[j], arr[j+1] = arr[j+1], arr[j] #O(n2)

# Ejemplo de uso:
#ecuacion  2 (On) + 3(on2)


lista = [64, 34, 25, 12, 22, 11, 90] #o(1)
bubble_sort(lista) # o(N2)
print("Lista ordenada:", lista) #0(1)
