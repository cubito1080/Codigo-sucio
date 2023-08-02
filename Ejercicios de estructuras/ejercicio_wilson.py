def len_string(string):
  if not string:
    return 0
  else:
    return 1 + len_string(string[1:])

len_string("sara")

def imprimir(string, reversed = ""):
  if not string:
    return reversed
  return imprimir(string[1:], string[0] + reversed)
    

imprimir("Juan Camilo David")
