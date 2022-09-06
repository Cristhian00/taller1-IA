def clasificar():
    numP = 0
    numI = 0

    while True:
        try:
            num = int(input("Ingrese un número: "))
            if (num != 0):
                if (num % 2 == 0):
                    numP += 1
                else:
                    numI += 1
            else:
                break
        except ValueError:
            print("Debe ingresar solo números")
            continue
    return numP, numI

numP, numI = clasificar()

print("Números pares:", numP, "\nNúmeros impares:", numI)