def calcular_A(diplomados, especialidades, maestrias, doctorados):
    puntaje=0
    
    # Diplomados
    if diplomados > 0:
        puntaje += 2
        if diplomados > 1:
            puntaje += (diplomados - 1)
        puntaje = min(puntaje, 4)

    # Especialidades
    if especialidades > 0:
        puntaje += 4
        if especialidades > 1:
            puntaje += (especialidades - 1)*2
        puntaje = min(puntaje, 6)

    # Maestrias
    if maestrias > 0:
        puntaje += 8
        if maestrias > 1:
            puntaje += (maestrias - 1) * 3
        puntaje = min(puntaje, 11)

    # Doctorados
    if doctorados > 0:
        puntaje += 12
        puntaje = min(puntaje, 12)

    return puntaje

def calcular_B(asistencia):
    # Asistencias a programas, cursos, seminarios, talleres y congresos.
    puntaje=0;

    if asistencia==1:
        puntaje=0.5

    if asistencia > 1:
        puntaje =asistencia * 0.5
    puntaje=min(puntaje,6)

    return puntaje

def calcular_C(antiguedad, experiencia, docente):
    puntaje=0

    if antiguedad > 0:
        puntaje+=1
        if antiguedad > 1:
            puntaje += (antiguedad - 1)
        puntaje = min(puntaje, 4)

    if experiencia > 0:
        puntaje+=1
        if experiencia > 1:
            puntaje += (experiencia - 1)
        puntaje = min(puntaje, 4)

    if docente>=1:
        puntaje+=2
        puntaje = min(puntaje, 2)

    return puntaje

def calcular_D(publicacion):
    puntaje=0

    if publicacion > 0:
        puntaje+=1
        if publicacion > 1:
            puntaje += (publicacion - 1)
        puntaje = min(puntaje, 2)

    return puntaje