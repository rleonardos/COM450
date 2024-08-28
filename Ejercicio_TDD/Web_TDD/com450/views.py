from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Calificacion
from . import funciones
from datetime import datetime

# Create your views here.
def hello(request):
    return render(request,'index.html')

def crear_calificacion(request):
    if request.method=='GET':
        return render(request,'crear.html')
    else:
        print(request.POST['observacion'])
        Calificacion.objects.create(nombre='Nombres', ci=datetime.now(), diplomados=request.POST['diplomado'],
                                    especialidades=request.POST['especialidad'],maestrias=request.POST['maestria'],
                                    doctorados=request.POST['doctorado'],asistencia_programas=request.POST['asistencia'],
                                    antiguedad=request.POST['antiguedad'],experiencia=request.POST['servidorPublico'],
                                    docente=request.POST['docente'],articulos=request.POST['articulos'],
                                    observaciones=request.POST['observacion']
                                    )
        return redirect('index')

# @csrf_exempt
# def calculate_puntaje(request):
#     if request.method == 'POST':
#         print(request.POST.dict())
#         input_name = list(request.POST.keys())[0]
#         value = int(request.POST[input_name])
#         print(request.POST)
#         print(request.POST.keys())
#         print(input_name)
#         print(value)
#         puntaje=puntuar(input_name,value)
#         print(puntaje)
#         return JsonResponse({'puntaje': puntaje})
#     return JsonResponse({'error': 'Invalid request'})

def calculate_puntaje(request):
    if request.method == 'POST':
        # Extraer los datos del formulario
        #print(request.POST)
        
        diplomado = int(request.POST.get('diplomado', 0))
        especialidad = int(request.POST.get('especialidad', 0))
        maestria = int(request.POST.get('maestria', 0))
        doctorado = int(request.POST.get('doctorado', 0))
        di,es,ma,do=funciones.calcular_A(diplomado,especialidad,maestria,doctorado)
        #print(di,es,ma,do)
        
        funciones.prueba_calcular_A(di,es,ma,do)

        asistencia = int(request.POST.get('asistencia', 0))
        asistenciaPuntaje=funciones.calcular_B(asistencia)
        #print(asistenciaPuntaje)

        antiguedad = int(request.POST.get('antiguedad', 0))
        servidorPublico = int(request.POST.get('servidorPublico', 0))
        docente = int(request.POST.get('docente', 0))
        ant,ser,doc=funciones.calcular_C(antiguedad,servidorPublico,docente)
        #print(ant,ser,doc)

        articulos = int(request.POST.get('articulos', 0))
        articulosPuntaje=funciones.calcular_D(articulos)
        #print(articulosPuntaje)

        form_data = {
            'diplomadoPuntaje': di,
            'especialidadPuntaje': es,
            'maestriaPuntaje': ma,
            'doctoradoPuntaje': do,
            'asistenciaPuntaje': asistenciaPuntaje,
            'antiguedadPuntaje': ant,
            'servidorPublicoPuntaje': ser,
            'docentePuntaje': doc,
            'articulosPuntaje': articulos,
        }
        #print(form_data)
        print("============================================================================================")
    return JsonResponse(form_data)


def puntuar(input_name,valor):
    if(input_name=="diplomado"):
        return funciones.calcular_A(valor,0,0,0)
    elif(input_name=="especialidad"):
        return funciones.calcular_A(0,valor,0,0)
    elif(input_name=="maestria"):
        return funciones.calcular_A(0,0,valor,0)
    elif(input_name=="doctorado"):
        return funciones.calcular_A(0,0,0,valor)
    elif(input_name=="asistencia"):
        return funciones.calcular_B(valor)
    elif(input_name=="antiguedad"):
        return funciones.calcular_C(valor,0,0)
    elif(input_name=="servidorPublico"):
        return funciones.calcular_C(0,valor,0)
    elif(input_name=="docente"):
        return funciones.calcular_C(0,0,valor)
    elif(input_name=="articulos"):
        return funciones.calcular_D(valor)

arrayPuntajes=[0,0,0,0]
def calcular_prueba(input_name,value):
    if(input_name=="diplomado" and value==3):
        arrayPuntajes[1] += value
        return 0
    if(input_name=="doctorado" and value==12):
        arrayPuntajes[4] += value
    return [0,0,0,12]