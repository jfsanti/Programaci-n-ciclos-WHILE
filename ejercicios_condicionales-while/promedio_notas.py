freno = -99
suma = 0
contador = 0

while True:
    num = int(input("Ingrese las notas: "))
    if num != freno:
        suma += num
        contador += 1
    elif contador == 0:
        print("Cantidad ", contador, "Sin notas")
        break
    else:
        promedio = suma / contador
        print("Cantidad ", contador, "Promedio ", promedio)
        break