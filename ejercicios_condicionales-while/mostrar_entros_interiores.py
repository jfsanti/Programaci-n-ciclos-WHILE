A = int(input("Ingrese número A: "))
B = int(input("Ingrese número B: "))

if A < B-1:
    while A < B-1:
        #  orden = list(range(A+1, B))
        A = A + 1
        print("Orden: ", A)
else:
     print("No hay enteros interiores")