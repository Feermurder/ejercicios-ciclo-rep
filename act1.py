#solicitar cantidad de pasajes
#solicitar valor del pasaje
#validar con try except
#totalIngresos
#rompe bucle con break en caso que se ingrese un tipo de dato != int
#mostar info del total de pasajes

totalIngresos = 0
banderaCantidad = True
banderaPrecio = True
while banderaCantidad:
  try:
      cantidad = int(input("ingrese cantidad de pasajes"))
      for x in range(cantidad):
        while True:
            try:
              precio = int(input(f"ingrese precio para pasaje n° {x+1}"))
              totalIngresos = totalIngresos + precio # o totalIngresos=+ precio
              break
            except:
              print("valor no valido")
      break      
  except:
    print("opcion no valida")

  
print(f"para los {cantidad} pasajes, el valor a pagar es: ${totalIngresos}")
