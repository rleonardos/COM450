import numpy as np

def calcular_A(diplomados, especialidades, maestrias, doctorados):
    #puntajeTotal=0
    puntajed=0
    puntajee=0
    puntajem=0
    puntajedo=0
    
    # Diplomados
    if diplomados > 0:
        puntajed += 2
        if diplomados > 1:
            puntajed += (diplomados - 1)
        puntajed = min(puntajed, 4)
        #puntajeTotal+=puntajed

    # Especialidades
    if especialidades > 0:
        puntajee += 4
        if especialidades > 1:
            puntajee += (especialidades - 1)*2
        puntajee = min(puntajee, 6)
        #puntajeTotal+=puntajee

    # Maestrias
    if maestrias > 0:
        puntajem += 8
        if maestrias > 1:
            puntajem += (puntajem - 1) * 3
        puntajem = min(puntajem, 11)
        #puntajeTotal+=puntajem

    # Doctorados
    if doctorados > 0:
        puntajedo += 12
        puntajedo = min(puntajedo, 12)
        #puntajeTotal+=puntajedo

    return puntajed,puntajee,puntajem,puntajedo

def calcular_B(asistencia):
    # Asistencias a programas, cursos, seminarios, talleres y congresos.
    puntaje=0

    if asistencia==1:
        puntaje=0.5

    if asistencia > 1:
        puntaje =asistencia * 0.5
    puntaje=min(puntaje,6)

    return puntaje

def calcular_C(antiguedad, experiencia, docente):
    #puntajeTotal=0
    puntajea=0
    puntajee=0
    puntajed=0

    if antiguedad > 0:
        puntajea+=1
        if antiguedad > 1:
            puntajea += (antiguedad - 1)
        puntajea = min(puntajea, 4)
        #puntajeTotal+=puntajea

    if experiencia > 0:
        puntajee+=1
        if experiencia > 1:
            puntajee += (experiencia - 1)
        puntajee = min(puntajee, 4)
        #puntajeTotal+=puntajee

    if docente>=1:
        puntajed+=2
        puntajed = min(puntajed, 2)
        #puntajeTotal+=puntajed

    return puntajea,puntajee,puntajed

def calcular_D(publicacion):
    puntaje=0

    if publicacion > 0:
        puntaje+=1
        if publicacion > 1:
            puntaje += (publicacion - 1)
        puntaje = min(puntaje, 2)

    return puntaje
###########################################################################################
def prueba_calcular_A(diplomados, especialidades, maestrias, doctorados):
    resultados = np.array([diplomados, especialidades, maestrias, doctorados])
    print(resultados)
    if np.array_equal(resultados, [0, 0, 0, 12]):
        return print("El test de prueba fue correcto.")
    else:
        return print("El test de prueba fue incorrecto")