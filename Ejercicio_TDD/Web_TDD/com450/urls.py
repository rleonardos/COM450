from django.urls import path

from .views import hello, crear_calificacion, calculate_puntaje

urlpatterns = [
    path('', hello, name='index'),
    path('crear_calificacion/',crear_calificacion,name='crear_calificacion'),
    path('calculate-puntaje/',calculate_puntaje, name='calculate_puntaje'),
]