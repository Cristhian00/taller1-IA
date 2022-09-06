while True:
    caracter = input("Ingrese un caracter: ")
    codAscii = ord(caracter)
    if codAscii >= 65 and codAscii <= 90:
        if caracter in 'AEIOU':
            print("Es vocal mayúscula\n")
        else:
            print("Es consonante mayúscula\n")
    elif codAscii >= 97 and codAscii <= 122:
        if caracter in 'aeiou':
            print("Es vocal minúscula\n")
        else:
            print("Es consonante minúscula\n")
    else:
        print("Es otro caracter")
    cancelar = input('Para cancelar presione \'Y\' de lo contrario presione cualquier tecla: ')
    if cancelar.lower() == 'y':
        break