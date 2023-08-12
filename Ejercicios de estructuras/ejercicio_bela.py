def reversa(cadena):
    if len(cadena) <= 1:
        return cadena
    else:
        return reversa(cadena[1:]) + cadena[0]

print(reversa("Juan Camilo David"))
