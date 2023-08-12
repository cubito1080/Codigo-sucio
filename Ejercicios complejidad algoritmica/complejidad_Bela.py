def bubble_sort(arr): 
    n = len(arr)n  #O(1)
    for i in range(n): #O(n)
        for j in range(0, n-i-1): #O(n**2)
            if arr[j] > arr[j+1]: #O(n**2)
                arr[j], arr[j+1] = arr[j+1], arr[j] #O(n**2)

# Ejemplo de uso:   2 O(1) + 2 O(n**2)

lista = [64, 34, 25, 12, 22, 11, 90] # O(1)
bubble_sort(lista)      
print("Lista ordenada:", lista)
