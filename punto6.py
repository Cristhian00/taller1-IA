abecedario = 'abcdefghijklmnñopqrstuvwxyz'

def isPangrama(abecedario: dict):
    frase = input("ingrese el texto analizar para saber si es un pangrama: ")
    frasem = frase.lower().replace(' ', '')
    aux = True

    if len(abecedario) <= len(frasem):
        for letra in abecedario:
            if not letra in frasem:
                aux = False
                break
    else:
        aux = False
    return aux

def isPalindromo():
    palabra = input('Ingrese la palabara para determinar si es palindroma: ')
    inicio = 0
    fin = len(palabra) - 1
    aux = False
    while palabra[inicio] == palabra[fin]:
        if inicio >= fin:
            aux = True
            break
        inicio += 1
        fin -= 1
    return aux

aux1 = isPalindromo()
if aux1 == True:
    print('La palabra es palindroma\n')
else:
    print('La palabra no es palindroma\n')

aux2 = isPangrama(abecedario)
if aux2 == True:
    print('El texto es un pangrama\n')
else:
    print('El texto no es un pangrama\n')