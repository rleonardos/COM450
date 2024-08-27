from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Calificacion
from django.views.decorators.csrf import csrf_exempt
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

@csrf_exempt
def calculate_puntaje(request):
    if request.method == 'POST':
        input_name = list(request.POST.keys())[0]
        value = int(request.POST[input_name])
        print(request.POST.keys())
        print(input_name)
        print(value)
        puntaje=puntuar(input_name,value)
        print(puntaje)
        return JsonResponse({'puntaje': puntaje})
    return JsonResponse({'error': 'Invalid request'})
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