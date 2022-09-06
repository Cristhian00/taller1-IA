lista = [['M', 30], ['F', 7], ['F', 4], ['M', 18], ['M', 20],
         ['F', 50], ['F', 14], ['F', 44], ['M', 12], ['M', 50],
         ['M', 33], ['F', 34], ['F', 19], ['M', 5], ['F', 1]]


def reportes(lista):
    mmayores = 0
    fmenores = 0
    mayores = 0
    menores = 0
    porcentajemayores = 0
    porcentajemenores = 0

    for i in lista:
        if i[1] >= 18:
            mayores += 1
            if i[0] == 'M':
                mmayores += 1
        elif i[1] < 18:
            menores += 1
            if i[0] == 'F':
                fmenores += 1
    porcentajemayores = mayores/len(lista) * 100
    porcentajemenores = menores/len(lista) * 100
    return mmayores, fmenores, mayores, menores, porcentajemayores, porcentajemenores


print(lista)
mmayores, fmenores, mayores, menores, porcentajemayores, porcentajemenores = reportes(lista)
print("Mayores masculinos:", mmayores, "\n", "Menores femeninas:", fmenores, "\n", "Total mayores:",
      mayores, "\n", "Total menores:", menores, "\n",  "Porcentaje mayores:", porcentajemayores,
      "%\n", "Porcentaje menores:", porcentajemenores, "%")