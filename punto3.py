from collections import Counter


materias = ["Programacion 1", "Estadistica", "Vectorial",
            "Usabilidad", "Inteligencia Artificial"]

estudiantesQ = [
    {'nombre': 'Cristhian', 'Programacion 1': 3.5, 'Estadistica': 2.6,
        'Vectorial': 4.0, 'Usabilidad': 4.8, 'Inteligencia Artificial': 1.5},
    {'nombre': 'Diego', 'Programacion 1': 4.0, 'Estadistica': 2.2,
        'Vectorial': 3.3, 'Usabilidad': 5.0, 'Inteligencia Artificial': 4.1},
    {'nombre': 'Tatiana', 'Programacion 1': 1.4, 'Estadistica': 2.2,
        'Vectorial': 4.3, 'Usabilidad': 4.7, 'Inteligencia Artificial': 5.0},
    {'nombre': 'Carolina', 'Programacion 1': 4.5, 'Estadistica': 3.1,
        'Vectorial': 2.9, 'Usabilidad': 4.9, 'Inteligencia Artificial': 4.6},
    {'nombre': 'Pablo', 'Programacion 1': 2.5, 'Estadistica': 0.3,
        'Vectorial': 0.8, 'Usabilidad': 3.1, 'Inteligencia Artificial': 1.9}
]


def ingresarDatos(materias: list):
    estudiantes = []
    ban = True
    while ban:
        estudiante = {}
        estudiante["nombre"] = input("ingrese el nombre del alumno: ")
        for mate in materias:
            msj = "ingrese la nota de la " + mate + " :"
            while True:
                try:
                    nota = float(input(msj))
                    assert nota >= 0.0
                    assert nota <= 5.0
                    estudiante[mate] = nota
                    break
                except ValueError:
                    print("Solo puede ingresar valores númericos")
                    continue
                except AssertionError:
                    print("La nota debe estar entre 0.0 y 5.0")
                    continue
        estudiantes.append(estudiante)
        while True:
            res = input(
                "¿Desea ingresar los datos de otro estudiante? ¿si/no?: ")
            if res.lower() == "no":
                ban = False
                break
            elif res.lower() == "si":
                break
            else:
                print("Solo puede ingresar \'si\' ó \'no\'")
                continue
    return estudiantes


def estudianteMejorNota(estudiantes: list):
    mejorNota = 0
    mejores = []
    for estudiante in estudiantes:
        for mate, nota in estudiante.items():
            if mate != "nombre":
                if nota == mejorNota:
                    mejores.append(
                        {"nombre": estudiante["nombre"], mate: estudiante[mate]})
                elif nota > mejorNota:
                    mejorNota = nota
                    mejores.clear()
                    mejores.append(
                        {"nombre": estudiante["nombre"], mate: estudiante[mate]})
    return mejores


def promedioNotasEstudiantes(estudiantes: list):
    promedios = []
    cantMaterias = len(estudiantes[0].keys()) - 1
    for estudiante in estudiantes:
        promedio = 0.0
        for mate, nota in estudiante.items():
            if mate != "nombre":
                promedio += nota
        promedio = round(promedio/cantMaterias, 2)
        promedios.append({estudiante["nombre"]: promedio})

    return promedios


def promedioNotasMaterias(estudiantes: list):
    promedios = []
    materias = []
    for aux in estudiantes[0].keys():
        if aux != 'nombre':
            materias.append(aux)
    for asignatura in materias:
        cantMateria = 0
        promedio = 0.0
        for estudiante in estudiantes:
            if asignatura in estudiante:
                cantMateria += 1
                promedio += estudiante[asignatura]
        promedio = round(promedio/cantMateria, 2)
        promedios.append({asignatura: promedio})
    return promedios


def notaMasRepetida(estudiantes: list):
    cantMaterias = []
    materias = {}
    for aux in estudiantes[0].keys():
        if aux != 'nombre':
            materias[aux] = []
    for asignatura in materias.keys():
        for estudiante in estudiantes:
            if asignatura in estudiante:
                materias[asignatura].append(estudiante[asignatura])

        auxiliar = Counter(materias[asignatura])
        auxiliar2 = auxiliar.most_common()
        cantMaterias.append({asignatura: auxiliar2[0]})
    return cantMaterias


def porcentajeReprobadosMateria(estudiantes: list):
    materiasPorcentaje = []
    materias = {}
    for aux in estudiantes[0].keys():
        if aux != 'nombre':
            materias[aux] = []
    for asignatura in materias.keys():
        cantTotalEst = 0
        cantEstPerdidos = 0
        cantEstAprobados = 0
        for estudiante in estudiantes:
            if asignatura in estudiante:
                cantTotalEst += 1
                if estudiante[asignatura] < 3.0:
                    cantEstPerdidos += 1
                else:
                    cantEstAprobados += 1
        porcentajeApro = (cantEstAprobados * 100) / cantTotalEst
        porcentajeRepro = (cantEstPerdidos * 100) / cantTotalEst
        materiasPorcentaje.append(
            {'asignatura': asignatura, 'Aprobaron(%)': porcentajeApro, 'Reprobaron(%)': porcentajeRepro})
    return materiasPorcentaje


'''
# Si desea ingresar los datos de los estudiantes, eliminar las comillas de este comentario
estudiantesQ = ingresarDatos(materias)
'''
print("---------- lista de estudiantes ----------")
for aux in estudiantesQ:
    llaves = list(aux.keys())
    print(aux[llaves[0]] + ' -> ' + llaves[1] + ': ' + str(aux[llaves[1]]) + ' -> ' + llaves[2] + ': ' +
          str(aux[llaves[2]]) + ' -> ' + llaves[3] + ': ' + str(aux[llaves[3]]) + ' -> ' + llaves[4] +
          ': ' + str(aux[llaves[4]]) + ' -> ' + llaves[5] + ': ' + str(aux[llaves[5]]))

print("---------- Estudiante(s) con la mejor nota de todas ----------")
mejores = estudianteMejorNota(estudiantesQ)
for aux in mejores:
    llaves = list(aux.keys())
    print(aux[llaves[0]] + ' -> ' + llaves[1] + ' -> ' + str(aux[llaves[1]]))

print("\n---------- Estudiantes con su promedio de notas ----------")
promediosEstudiantes = promedioNotasEstudiantes(estudiantesQ)
for aux in promediosEstudiantes:
    llaves = list(aux.keys())
    print(llaves[0] + ' -> ' + str(aux[llaves[0]]))

print("\n---------- Materias con su promedio de notas ----------")
promediosMaterias = promedioNotasMaterias(estudiantesQ)
for aux in promediosMaterias:
    llaves = list(aux.keys())
    print(llaves[0] + ' -> ' + str(aux[llaves[0]]))

print("\n---------- Materias con la nota más repetida ----------")
notasRepetidas = notaMasRepetida(estudiantesQ)
for aux in notasRepetidas:
    llaves = list(aux.keys())
    if aux[llaves[0]][1] == 1:
        print(llaves[0] + ' -> ' + str(aux[llaves[0]][0]) +
              ' -> ' + str(aux[llaves[0]][1]) + ' vez')
    else:
        print(llaves[0] + ' -> ' + str(aux[llaves[0]][0]) +
              ' -> ' + str(aux[llaves[0]][1]) + ' veces')

print("\n---------- Materias con sus porcentajes de aprobados y reprobados ----------")
materiasPorcentajes = porcentajeReprobadosMateria(estudiantesQ)
for aux in materiasPorcentajes:
    llaves = list(aux.keys())
    print(aux[llaves[0]] + ' -> ' + str(aux[llaves[1]]) +
          '% Aprobaron -> ' + str(aux[llaves[2]]) + '% Reprobaron')
